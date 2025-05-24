#!/home/q0hisroot/faceenv/bin/python3

import numpy as np
import cv2 as cv
import face_recognition
import os

cap = cv.VideoCapture("./main.mp4")
if not cap.isOpened():
    print("Can't open the file!")
    exit()


width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv.CAP_PROP_FPS))
known_faces = []
writers = {} # videoWriter objects corresponding to the face_id
frames_remaining = {} # count frames remaining corresponding to the face_id
face_counter = 0

fourcc = cv.VideoWriter_fourcc(*'mp4v')
output = cv.VideoWriter('output1.mp4', fourcc, fps, (width, height)) # videowriter object
                                                                     # create one for each face

while cap.isOpened():
    ret, frame = cap.read()
    face_locations = []

    if not ret:
        print("end of file or cant open")
        exit
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)
    if not face_locations:
        continue
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    for encoding in face_encodings:
        matches = [face_recognition.compare_faces([known_face[0]], encoding)[0] for known_face in known_faces]
    '''
    this was quite confusing for me to write
    known_faces is an array of tuples containing (face_encoding, face_id) tuples
    so known[0] is the face_encoding of the face
    face_encoding is the face_encoding of the face found
    '''

    if any(matches): # if any known_face matches in the known_face array,
        face_id = known_faces[matches.index(True)][1] # find the face_id of the face that matched, by indexing
    # this will only be applicable when the known_faces array is not populated
    # or when faces change
    else:
        face_counter += 1
        face_id = f"face_{face_counter}"
        known_faces.append((encoding, face_id)) # appending a tuple to an array
        out_path = f"{face_id}.mp4"
        writers[face_id] = cv.VideoWriter(out_path, fourcc, fps, (width, height))
        frames_remaining[face_id] = int(fps * 10)

    if frames_remaining[face_id] > 0:
        writers[face_id].write(frame)
        print(f"Written {face_id}")
        frames_remaining[face_id] -= 1

cap.release()
for writer in writers.values():
    writers.release()
cv.destroyAllWindows()

