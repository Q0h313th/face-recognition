# face-recognition
project for internship application

test files used are also uploaded

Features implemented as of now:
1. Takes a video as an input (hardcoded the video file) and writes the resulting processed output to an mp4 file
2. Performs facial recognition through the facial_recognition library's inbuilt models.
3. Checks for the number of faces in each frame, if there is more than one face found, compares them to check if its the same face (right now only checks for 2 faces)
4. If the faces are not the same, skips the frames, if they're the same, writes the output to the file
5. captures 10-second videos of one unique face and writes them to a file

Precautions:
1. Its takes a really really long time to do all the face-recognition. Im assuming this is because the [face_recognition](https://github.com/ageitgey/face_recognition) library ive used is written in python. you can probably optimize it by [doing this] (https://face-recognition.readthedocs.io/en/latest/readme.html#installation) but i haven't tried yet.
2. While I was able to get the 10-second stitching thing done, it also captured a whole lot of garbage videos for me each containing 1-2 frames, and I think its because the expression of the
person in the frame was really different causing the `compare_faces` function to return a `False` value. 
