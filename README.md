# Screen Recording Using OpenCv
I don't want to keep using zoom to screen record so this project is my solution to that problem. 😊

Let's get started! 

## Required Programs and Libraries 
To this process a lot easier I've saved them in `requirements.txt`
What you need to do to install the libraries needed for this project, in the terminal run `pip install -r requirement.txt`.

However, before running `pip install -r requirements.txt` in your terminal you must:
1. Clone the repo 
2. Create a virtual environment in your terminal 
   + `python -m venv .venv` 
3. Activate you virtual environment
   + **Windows:** `.\.venv\Scripts\activate`
   + **macOS/Linux:** `source .venv/bin/activate`
     + Once it's activated, your terminal should look similar to the following:
       + `(.venv) C:\path\to\project>`
4. You can now finally run `pip install -r requirements.txt` 

Your're now good to go! 🎉

## Create a Directory 
> **Note:** This directory will be used to save the screen recording video as `.mp4` file

```py
output_dir = "./Screen Record"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
```

## Screen Recording Program 
```py
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
```

### To Do Lists
+ [x] Create `requirements.txt`
+ [x] Create a virtual environment (`venv`)
+ [x] Complete README
#### Troublshoot
+ [ ] Having issues delaying the video to real-time speed
+ [ ] Give users the ablity to resize the `cv2.imshow()` visualization too