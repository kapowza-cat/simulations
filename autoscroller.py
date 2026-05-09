import pyautogui
import keyboard
import time

# Configuration
scroll_amount = -10  # Initial scroll speed/direction (Negative is down)
step = 5             # How much to increase/decrease speed per key press
active = True

keyboard.wait('x')
print("--- Auto-Scroller Active ---")


try:
    while active:
        # Perform the scroll
        pyautogui.scroll(scroll_amount)
        
        # Check for keyboard inputs to adjust speed
        if keyboard.is_pressed('c'):
            scroll_amount -= step  # Make the negative number "larger" to go faster
            print(f"Speed increased: {scroll_amount}")
            time.sleep(0.1) # Small delay to prevent runaway speed
            
        if keyboard.is_pressed('v'):
            # Prevent it from flipping to upward scroll unless you want that
            if True:
                scroll_amount += step
                print(f"Speed decreased: {scroll_amount}")
            time.sleep(0.1)

        if keyboard.is_pressed('z'):
            active = False
            
        # Control the refresh rate of the loop
        time.sleep(0.05)

except Exception as e:
    print(f"An error occurred: {e}")

print("Stopped.")