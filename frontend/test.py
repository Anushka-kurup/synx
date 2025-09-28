from pythonosc import udp_client
import time


client = udp_client.SimpleUDPClient("192.168.0.242", 4560)  # Sonic Pi IP and port

client.send_message("/play/sample", "elec_blip")


# Your Sonic Pi code to play
code = """
sample :elec_blip
sleep 0.5
sample :bass_dnb_f
sleep 0.5
"""

# Send /run-code message (Sonic Pi specific)
client.send_message("/run-code", code)

# Optional: wait to ensure Sonic Pi has time to play sounds before script ends
time.sleep(2)
