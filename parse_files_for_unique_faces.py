from collections import defaultdict
import os
from shutil import move
from random import choice
import re
import threading

source_path_for_greater_vids = r"D:\Video_Datasets\more_vids"
source_path_for_lesser_vids = r"D:\Video_Datasets\less_vids"
dest_path_1 = r"D:\Video_Datasets\filtered_vids\more_vids_filtered"
dest_path_2 = r"D:\Video_Datasets\filtered_vids\less_vids_filtered"

def move_unique_files(source_path, dest_path):

    os.makedirs(dest_path, exist_ok=True)

    face_groups = defaultdict(list)
    for file in os.listdir(source_path):
        if file.endswith(".mp4"):
            match = re.match(r"(.+)_\d+\.mp4$", file) # :O
            if match:
                face_id = match.group(1)
                face_groups[face_id].append(file)
            else:
                face_groups[file].append(file)

    # move a random file from each group to the destination
    for face_id, files in face_groups.items():
        if files:
            file_to_move = choice(files)
            source_file = os.path.join(source_path, file_to_move)
            dest_file = os.path.join(dest_path, file_to_move)
            move(source_file, dest_path)
            print(f"Moved {file_to_move} to {dest_file}")

t1 = threading.Thread(target=move_unique_files, args=(source_path_for_greater_vids, dest_path_1))
t2 = threading.Thread(target=move_unique_files, args=(source_path_for_lesser_vids, dest_path_2))

t1.start()
t2.start()

t1.join()
t2.join()

print("All unique files have been copied to the destination directory.")