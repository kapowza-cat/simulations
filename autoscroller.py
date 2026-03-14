import pyautogui
import time

# Safety: small delay before starting
time.sleep(2)

try:
    while True:
        pyautogui.scroll(-500000000)  # Negative = scroll down, positive = scroll up
        time.sleep(0.00001)
except KeyboardInterrupt:
    print("Stopped.")