#!/home/q0hisroot/faceenv/bin/python3

# the way i fixed the face_recognition module import error was by 
# pip install setuptools
# pip install git+https://github.com/ageitgey/face_recognition_models
# then pip install opencv-python

import numpy as np
import cv2 as cv
import face_recognition

cap = cv.VideoCapture("./trimmed.mp4") # it needs to be in cwd or else it doesnt work
if not cap.isOpened():
    print("cant open the file!")
    exit()

width = int(cap.get(3)) # capture.get(cv.CAP_PROP_FRAME_WIDTH)
height = int(cap.get(4)) # capture.get(cv.CAP_PROP_FRAME_HEIGHT)
fps = int(cap.get(cv.CAP_PROP_FPS)) # fps

# create a video_writer
fourcc = cv.VideoWriter_fourcc(*'mp4v')
output = cv.VideoWriter('new_video.mp4', fourcc, fps, (width, height)) # creating the videowriter object

reference_face_encodings = None # initially empty but used later to iterate for test cases

while cap.isOpened():
    ret, frame = cap.read()
    face_locations = []

    if not ret:
        print("Can't receive")
        break
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB) # convert bgr frame to rgb for face recognition library
                                                     # also, just using frame[:, :, ::-1] breaks the face_encodings method
    face_locations = face_recognition.face_locations(rgb_frame)
    if face_locations:
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    else:
        face_encodings = [] # face_encodings[0] represents the first face, or the reference face
                            # face_encodings is already list itself.
    print(f"faces detected: {len(face_locations)}")

    for top, right, bottom, left in face_locations:
        cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    # first test case
    if len(face_locations) == 1:  # exactly one face in the frame 
        #cv.imshow('video', frame)
        print("ts is written to the file")
        output.write(frame)

    # second test case
    elif len(face_locations) == 2: # mirror case, but im hardcoding the value. ideally, this should be "i"
        if reference_face_encodings is None and face_encodings:
            reference_face_encodings = [face_encodings[0]] # ideally, this would iterate over all the face_encodings to match faces
        match_results = [
                        face_recognition.compare_faces(reference_face_encodings, encoding)[0] 
                        for encoding in face_encodings[1:] # for future modifications
                        ] # checks the second element becasue the first element is always going to be true
        #cv.imshow('video', frame)
        if match_results and all(match_results):
            print('Unique person multiple images (mirror)')
            output.write(frame)
        else:
            print('not matching so not written')

    # third case
    else:
        print(f"skipping frame with {len(face_locations)} faces")

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()