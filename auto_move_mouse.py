import pyautogui
import random
import time

# Function to move the mouse randomly
def move_mouse_randomly():
    screen_width, screen_height = pyautogui.size()  # Get screen size

    while True:
        # Generate random x and y coordinates within the screen size
        x = random.randint(0, screen_width - 1)
        y = random.randint(0, screen_height - 1)

        # Move the mouse to the random position
        pyautogui.moveTo(x, y, duration=0.5)  # Smooth movement
        print(f"Mouse moved to ({x}, {y})")

        # Wait for 5 seconds before moving again
        time.sleep(5)

# Run the function
if __name__ == "__main__":
    move_mouse_randomly()