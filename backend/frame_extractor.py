import cv2

import cv2

def extract_frames(video_path, fps=2):
    vidcap = cv2.VideoCapture(video_path)
    if not vidcap.isOpened():
        raise ValueError(f"Error opening video file: {video_path}")
    frames = []
    frame_rate = vidcap.get(cv2.CAP_PROP_FPS)
    if frame_rate == 0:
        frame_rate = 30  # default fallback fps if unable to read
    interval = max(1, int(frame_rate / fps))
    success, image = vidcap.read()
    count = 0
    while success:
        if count % interval == 0:
            frames.append(image)
        success, image = vidcap.read()
        count += 1
    vidcap.release()
    return frames
