from backend.config import OBJECT_TO_SAMPLE

def generate_sonic_pi_code(detected_objects):
    if not detected_objects:
        # No detections: play nature ambient sound (e.g. water)
        return "sample :ambi_water\nsleep 1\n"
    
    code = ""
    for obj in detected_objects:
        sample = OBJECT_TO_SAMPLE.get(obj)
        if sample:
            code += f"sample :{sample}\nsleep 0.5\n"

    return code
