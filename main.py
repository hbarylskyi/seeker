from camera import take_picture, record_video

def main():
    # Example usage
    take_picture("image.jpg")
    record_video("video.h264", 5000)  # Record a 5-second video

if __name__ == "__main__":
    main()
