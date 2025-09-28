from backend.frame_extractor import extract_frames
from backend.object_detector import detect_objects
from backend.audio_mapper import generate_sonic_pi_code
from backend.osc_sender import send_to_sonic_pi

def process_video(video_path):
    frames = extract_frames(video_path)
    for frame in frames:
        detected = detect_objects(frame)
        code = generate_sonic_pi_code(detected)
        send_to_sonic_pi(code)
