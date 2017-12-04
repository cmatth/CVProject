import imutils
import cv2
import Tkinter
import tkFileDialog
import matplotlib.pyplot as plt

# Have user select the video file.
root = Tkinter.Tk()
root.withdraw()
video_file_path = tkFileDialog.askopenfilename()

cap = cv2.VideoCapture(video_file_path)

# Get first frame of video.
ret, init_frame = cap.read()

# Convert initial frame to gray scale.
init_frame_grayscale = cv2.cvtColor(init_frame, cv2.COLOR_BGR2GRAY)
init_frame_grayscale = cv2.GaussianBlur(init_frame_grayscale, (21, 21), 0)

num_frames = 0

while num_frames < 100:
    # Read frames of the video
    ret, next_frame = cap.read()
    num_frames += num_frames

    # Convert initial frame to gray scale.
    frame_gray_scale = cv2.cvtColor(next_frame, cv2.COLOR_BGR2GRAY)
    frame_gray_scale = cv2.GaussianBlur(frame_gray_scale, (21,21), 0)

    # Compute the difference between each frame throughout the video.
    frame_diff = abs(init_frame_grayscale - frame_gray_scale)

    # Threshold the difference between frames. Index at 1 to make thre_hold a numerical tuple.
    #thresh_hold = cv2.threshold(frame_diff,25,255,cv2.THRESH_BINARY)[1]
    thresh_hold = cv2.adaptiveThreshold(frame_diff, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Dilate threshold to determine object contours.
    new_thresh = cv2.dilate(thresh_hold,None,iterations = 2)

    # Find contours.
    contour, _ = cv2.findContours(new_thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cont in contour:
        cont_area = cv2.contourArea(cont)
        if cont_area < 100:
            continue
        # Determine bounding box of contour.
        x, y, w, h, = cv2.boundingRect(cont)
        cv2.rectangle(next_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("Practice", next_frame)
        cv2.imshow("Thresh", thresh_hold)
        #cv2.imshow("Change in Frame", frame_diff)
        cv2.waitKey(1)