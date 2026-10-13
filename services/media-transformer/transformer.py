import subprocess

def convert_to_vertical(input_path: str, output_path: str):
    # Crop and scale 16:9 video to 9:16 vertical short format (1080x1920)
    cmd = [
        "ffmpeg", "-i", input_path,
        "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",
        "-c:v", "libx264", "-preset", "fast", "-crf", "22",
        "-c:a", "aac", "-b:a", "128k",
        output_path
    ]
    
    print(f"[*] Re-framing {input_path} to 9:16 vertical...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Media transformation failed: {result.stderr}")
    print(f"[+] Output ready at {output_path}")
