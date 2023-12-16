import pyautogui
import time
import platform
import subprocess

# Function to move the mouse cursor
def move_mouse():
    # Get the current mouse position
    x, y = pyautogui.position()

    # Move the mouse cursor slightly to simulate activity
    pyautogui.moveTo(x + 1, y)

# Function to prevent the computer from going to sleep (Windows)
def prevent_sleep_windows():
    try:
        import ctypes
        # Set the thread execution state to prevent sleep
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)  # 0x80000002 corresponds to ES_CONTINUOUS | ES_SYSTEM_REQUIRED
    except ImportError:
        pass

# Function to prevent the computer from going to sleep (MacOS)
def prevent_sleep_macos():
    try:
        subprocess.run(["caffeinate", "-t", "3600"])  # Prevent sleep for 1 hour
    except FileNotFoundError:
        pass

# Function to prevent the computer from going to sleep (Linux)
def prevent_sleep_linux():
    try:
        subprocess.run(["xdg-screensaver", "reset"])
    except FileNotFoundError:
        pass

# Function to prevent the computer from going to sleep based on the operating system
def prevent_sleep():
    current_platform = platform.system()

    if current_platform == "Windows":
        prevent_sleep_windows()
    elif current_platform == "Darwin":  # MacOS
        prevent_sleep_macos()
    elif current_platform == "Linux":
        prevent_sleep_linux()

# Main loop
try:
    while True:
        move_mouse()
        prevent_sleep()
        time.sleep(60)  # Adjust the sleep interval as needed
except KeyboardInterrupt:
    print("Mouse jiggling and sleep prevention stopped.")
