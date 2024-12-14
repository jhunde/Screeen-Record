import cv2
import numpy as np
import mss
import time
import os

output_dir = "./Screen Record"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


try:
    with mss.mss() as sct:
        monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}
        codec = cv2.VideoWriter_fourcc(*"MP4V")
        file_name = os.path.join(output_dir, "screen_record.mp4")
        fps = 30
        screen_resolution = (monitor["width"], monitor["height"])

        output = cv2.VideoWriter(file_name, codec, fps, screen_resolution)

        frame_interval = 1 / fps  # Target time between frames
        last_frame_time = time.time()

        while True:
            current_time = time.time()
            if current_time - last_frame_time >= frame_interval:
                last_frame_time += frame_interval

                # Capture screen and process frame
                img = np.array(sct.grab(monitor))
                img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
                output.write(img)

                # Display frame
                cv2.imshow("Screen Record", img)

                # Check if the window is still open
                if cv2.getWindowProperty("Screen Record", cv2.WND_PROP_VISIBLE) < 1:
                    break

            # Allow OpenCV to process GUI events
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
finally:
    output.release()
    cv2.destroyAllWindows()
