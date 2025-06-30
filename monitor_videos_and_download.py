import pyperclip
import time
import os
import subprocess

DOWNLOAD_HISTORY_FILE = 'downloaded_links.txt'
DOWNLOAD_DIR = 'misc_videos'
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

if os.path.exists(DOWNLOAD_HISTORY_FILE):
     with open(DOWNLOAD_HISTORY_FILE, 'r') as o:
          stored_videos = set(line.strip() for line in o if line.strip())
else:
     stored_videos = set()

changed_value = ""
pyperclip.copy('')

try:
    while True:
        tmp_value = pyperclip.paste().strip()
        if tmp_value != changed_value:
            changed_value = tmp_value
            #print(stored_videos)
            if tmp_value in stored_videos:
                print("This video was already downloaded!")
            else:
                stored_videos.add(changed_value)
                with open(DOWNLOAD_HISTORY_FILE, 'a') as o:
                    o.write(tmp_value + '\n')
                
                print("Downloading the video...")
                try:
                    subprocess.run(["yt-dlp", "-P", DOWNLOAD_DIR, tmp_value])
                    print('Download complete.')
                except subprocess.CalledProcessError as e:
                    print(f"Error downloading video: {e}")

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nExiting the loop.")


