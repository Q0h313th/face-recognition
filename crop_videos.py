from video_list import video_segments
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

OUTPUT_DIR = "Hindi_audios"


def convert_to_seconds(time_str):
    """Convert time string in format 'MM:SS' to seconds"""
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds

def start_and_end_times(video_segments):
    """Extract start and end times from video segments"""
    for segment in video_segments:
        start = convert_to_seconds(segment["start"])
        end = convert_to_seconds(segment["end"])
        yield start, end


def download_and_crop_video(url, start, end, output_dir):
    duration = end - start
    os.makedirs(output_dir, exist_ok=True)
    cmd = [
        'yt-dlp',
        url,
        '--external-downloader', 'ffmpeg',
        '--external-downloader-args', f'-ss {start} -t {duration}',
        '-x',
        '--audio-format', 'mp3',
        '--audio-quality', '0',
        '-o', f'{output_dir}/%(title)s.%(ext)s',
        '--no-check-certificates',
        '--quiet'
    ]
    print(f"Downloading and cropping video: {url} from {start} for {duration} seconds")
    try:
        result = subprocess.run(cmd, check=True, capture_output=True)
        if result.returncode == 0:
            print(f"Successfully downloaded and cropped: {url}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error downloading {url}: {e.stderr.decode().strip()}")
        return False
    
def main():
    output_directory = OUTPUT_DIR
    max_workers = 8

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(download_and_crop_video, segment["url"], start, end, output_directory)
                   for segment, (start, end) in zip(video_segments, start_and_end_times(video_segments))]
        for future in futures:
            future.result()

    print("All downloads completed.")

if __name__ == "__main__":
    main()
