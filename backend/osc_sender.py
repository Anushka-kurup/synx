# from pythonosc import udp_client
# from backend.config import OSC_IP, OSC_PORT

# client = udp_client.SimpleUDPClient(OSC_IP, OSC_PORT)

# def send_to_sonic_pi(code):
#     client.send_message("/run-code", code)


from pythonosc import udp_client
import time

# Use your Sonic Pi IP and port
client = udp_client.SimpleUDPClient("192.168.0.242", 4560)

samples_to_test = ["elec_blip", "bass_dnb_f", "drum_bass_hard", "elec_blip", "bass_dnb_f", "drum_bass_hard", "elec_blip", "bass_dnb_f", "drum_bass_hard",]

for sample_name in samples_to_test:
    print(f"Sending sample: {sample_name}")
    client.send_message("/osc/play/sample", sample_name)
    time.sleep(1)  # wait so you can hear each sample
