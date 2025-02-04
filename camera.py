import subprocess

def take_picture(filename):
    """Take a picture and save it to the specified filename."""
    subprocess.run(["libcamera-still", "-o", filename])

def record_video(filename, duration):
    """Record a video for the specified duration and save it to the filename."""
    subprocess.run(["libcamera-vid", "-t", str(duration), "-o", filename])
