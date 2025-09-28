from ultralytics import YOLO
from backend.config import YOLO_MODEL_PATH

model = YOLO(YOLO_MODEL_PATH)

def detect_objects(frame):
    results = model(frame)
    detected_objects = []
    for r in results:
        for cls_id in r.boxes.cls:
            detected_objects.append(r.names[int(cls_id)])
    return detected_objects
