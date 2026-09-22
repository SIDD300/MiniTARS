import cv2
import time
from datetime import datetime
from pathlib import Path


def take_photo():
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        return "Camera could not be opened."

    success, frame = camera.read()

    camera.release()

    if not success:
        return "Failed to capture image."

    output_dir = Path("camera/photos")
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = output_dir / f"photo_{timestamp}.jpg"

    cv2.imwrite(str(file_path), frame)

    return f"Photo captured successfully: {file_path}"


def record_video(duration=40):
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        return "Camera could not be opened."

    width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fps = camera.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 20.0

    output_dir = Path("camera/videos")
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = output_dir / f"video_{timestamp}.mp4"

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(
        str(file_path),
        fourcc,
        fps,
        (width, height)
    )

    start_time = time.time()

    while time.time() - start_time < duration:
        success, frame = camera.read()

        if not success:
            break

        video_writer.write(frame)

    camera.release()
    video_writer.release()

    return f"Video recording completed: {file_path}"