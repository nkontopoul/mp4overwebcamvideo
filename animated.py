from os.path import sep
import cv2 as cv2
from numpy import *
#You must have a video file called fun.mp4 in the same folder
#make sure that you have opencv installed with python
#tested with python 3.10.6 on windows 11

video_name = 'fun.mp4'
img = cv2.VideoCapture(video_name)


img.set(cv2.CAP_PROP_FRAME_WIDTH, 450)  # float `width`
img.set(cv2.CAP_PROP_FRAME_HEIGHT, 450)
width = 150
height = 150


cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_FPS, 30)

# frame_vid = img.read()



x = 0
y = 0

video_frame_counter = 0

while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        ret_video, frame_video = img.read()
        video_frame_counter += 1

        if video_frame_counter == img.get(cv2.CAP_PROP_FRAME_COUNT):
            video_frame_counter = 0
            img.set(cv2.CAP_PROP_POS_FRAMES, 0)

        if ret_video:
            # add image to frame
            frame_video = cv2.resize(frame_video, (width, height))
            frame[y:y + width, x:x + height] = frame_video


            # Display the resulting frame
            cv2.imshow('Live video overlayed by streamed video', frame)
            if(x<480):
                x=x+5
            else:
                x=0
            

            # Exit if ESC key is pressed
            if cv2.waitKey(1) & 0xFF == 27:
                break

img.release()
cap.release()
cv2.destroyAllWindows()
