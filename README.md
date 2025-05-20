# face-recognition
project for internship application

test files used are also uploaded

Features implemented as of now:
1. Takes a video as an input (hardcoded the video file) and writes the resulting processed output to an mp4 file
2. Performs facial recognition through the facial_recognition library's inbuilt models.
3. Checks for the number of faces in each frame, if there is more than one face found, compares them to check if its the same face (right now only checks for 2 faces)
4. If the faces are not the same, skips the frames, if they're the same, writes the output to the file

To do:
1. Add a 10-second limit to the number of frames being captured.
2. Add stitching of frames where 2 video sections can be stitched together to form one singular 10 second long video.
