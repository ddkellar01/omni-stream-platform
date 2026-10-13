import os
import subprocess
import time

def transcode_video(input_path: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    playlist_path = os.path.join(output_dir, "playlist.m3u8")
    
    cmd = [
        "ffmpeg", "-i", input_path,
        "-profile:v", "main", "-level", "4.0", "-s", "1280x720",
        "-start_number", "0", "-hls_time", "6", "-hls_list_size", "0",
        "-f", "hls", playlist_path
    ]
    
    print(f"[*] Starting transcoding for {input_path}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"FFmpeg failed: {result.stderr}")
    print("[+] Transcoding complete.")

if __name__ == "__main__":
    print("[*] Transcoding worker online. Waiting for queue tasks...")
    time.sleep(1)
