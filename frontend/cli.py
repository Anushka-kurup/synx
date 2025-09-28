# frontend/cli.py
import sys
from backend.pipeline import process_video
from backend.audio_mapper import generate_sonic_pi_code

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m frontend.cli <video_file>")
        sys.exit(1)

    video_path = sys.argv[1]
    process_video(video_path)

    detected = ["dog", "sheep", "car"]
    sonic_pi_code = generate_sonic_pi_code(detected)
    print(sonic_pi_code)
