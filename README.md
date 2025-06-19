# face-recognition
My internship repository

test files used are also uploaded

Features implemented as of now:
1. Takes a video as an input (hardcoded the video file) and writes the resulting processed output to an mp4 file
2. Performs facial recognition through the facial_recognition library's inbuilt models.
3. Checks for the number of faces in each frame, if there is more than one face found, compares them to check if its the same face (right now only checks for 2 faces)
4. If the faces are not the same, skips the frames, if they're the same, writes the output to the file
5. captures 10-second videos of one unique face and writes them to a file
6. `count_time_and_copy.py` is used to seperate a video based on its duration into respective directories. it COPIES the file hence increasing the storage. DONT USE THIS FOR PARSING THROUGH A HUGE AMOUNT OF FILES
7. `count_time_and_move.py` is used to do the same thing as above, except it MOVES the file, which is why the storage stays constant. 
8. `run_all_videos.ps1` iterates over the files in a directory and runs the `count_time.py` script. (right now the directories are hardcoded but ill change that)
9. `parse_files_for_unique_faces.py` searches for unique files with matching a particular regex pattern and moves it to dest_directory.
10. `crop_videos.py` is written to crop a multitude of videos given their url, start time and end time. It reads this data from video_list.py to prevent convoluting code with data, ive uploaded the test file too. Also, i used to perplexity to format the video_list.py according to the what it is now, i'd formatted it a bit weirdly but yeah perplexity worked


Precautions:
1. Its takes a really really long time to do all the face-recognition. Im assuming this is because the [face_recognition](https://github.com/ageitgey/face_recognition) library ive used is written in python. you can probably optimize it by looking over here (https://face-recognition.readthedocs.io/en/latest/readme.html#) but i haven't tried yet.
2. While I was able to get the 10-second stitching thing done, it also captured a whole lot of garbage videos for me each containing 1-2 frames, and I think its because the expression of the
person in the frame was really different causing the `compare_faces` function to return a `False` value. 
3. `main_face_recognition_script.py` is NOT meant to be used as a tool, there is no support for cli arguments whatsoever, all the arguments are hard coded
4. the whole counting the duration of each file thing could be made faster with ffmpeg but i havent tried it.

TODO:
1. add command line support for ps1 file
2. rewrite the ps1 file into a bash script
