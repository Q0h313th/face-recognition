import sys
import cv2
import os
import shutil

more_video_path = r'C:\Users\Chinmay\py_tools\processor_vids' # for videos longer than 10 seconds
less_video_path = r'C:\Users\Chinmay\py_tools\less_vids' # for videos shorter than 10 seconds
MAX_VIDEO_LENGTH = 10  # seconds

def safe_copy(src, dst_dir):
    os.makedirs(dst_dir, exist_ok=True)
    dst_path = os.path.join(dst_dir, os.path.basename(src))
    if os.path.exists(dst_path):
        print(f"File {dst_path} already exists. Not copying.")
    else:
        shutil.copy(src, dst_path)
        print(f"Video copied to {dst_path}")



if len(sys.argv) != 2:
    print("Usage: python count_time.py <video_path>")
    sys.exit(1)

video_path = sys.argv[1]
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Error: Could not open video file {video_path}")
    sys.exit(1)
else:
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps
    print(f"Video duration: {duration:.2f} seconds")

    if duration > MAX_VIDEO_LENGTH:
        safe_copy(video_path, more_video_path)
    else:
        safe_copy(video_path, less_video_path)
    
