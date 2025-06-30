import sys
import cv2
import os
import shutil

more_video_path = r'C:\Users\Chinmay\py_tools\more_vids' # for videos longer than 10 seconds
less_video_path = r'C:\Users\Chinmay\py_tools\less_vids' # for videos shorter than 10 seconds
THRESHOLD_VIDEO_LENGTH = 10  # seconds

def safe_move(src, dst_dir):
    os.makedirs(dst_dir, exist_ok=True)
    dst_path = os.path.join(dst_dir, os.path.basename(src))
    if os.path.exists(dst_path):
        print(f"File {dst_path} already exists. Skipping.")
    else:
        shutil.move(src, dst_path)
        print(f"Video moved to {dst_path}")



if len(sys.argv) != 2:
    print("Usage: python3 get_video_length <video_path>")
    sys.exit(1)

video_path = sys.argv[1]
video_name = os.path.basename(video_path)

dst_more = os.path.join(more_video_path, video_name)
dst_less = os.path.join(less_video_path, video_name)

if os.path.exists(dst_more) or os.path.exists(dst_less):
    print(f"Video {video_name} already processed. Skipping.")
    sys.exit(0)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Error: Could not open video file {video_path}")
    sys.exit(1)
else:
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps
    print(f"Video duration: {duration:.2f} seconds")
    cap.release()

    if duration > MAX_VIDEO_LENGTH:
        safe_move(video_path, more_video_path)
    else:
        safe_move(video_path, less_video_path)
    
