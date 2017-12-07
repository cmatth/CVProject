import imutils
import cv2
import Tkinter
import tkFileDialog
import numpy as np
import matplotlib.pyplot as plt

#def count_frames(vid):
#    # Determine the number of frames in a recorded video.
#    tot_frames = 0
#
#    while True:
#        ret, frame = vid.read()
#        if not ret:
#            break
#        tot_frames += 1
#
#    return tot_frames

# Have user select the video file.
root = Tkinter.Tk()
root.withdraw()
video_file_path = tkFileDialog.askopenfilename()

cap = cv2.VideoCapture(video_file_path)

# Get number of frames in recorded video.
num_of_frames = 200#count_frames(cap)

bgSub = cv2.BackgroundSubtractorMOG()

frame_counter = 0

while frame_counter < num_of_frames:
    # Read frames of the video
    ret, next_frame = cap.read()
    frame_counter += 1

    if np.mod(frame_counter,15) == 0:
        bgSub = cv2.BackgroundSubtractorMOG()

    next_frame_short = imutils.resize(next_frame,width=400)

    next_frame_blur = cv2.GaussianBlur(next_frame_short,(3,3),0)

    fgmask = bgSub.apply(next_frame_blur)

    # Find contours.
    contour, _ = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create new contour area array.
    cont_area_arr = []

    # Determine how many contours are in the frame.
    num_of_contours = len(contour)

    for cont in contour:
        #if cv2.contourArea(cont) < 70 and cv2.contourArea(cont) > 150:
        #   continue
        # Determine bounding box of contour.
        x, y, w, h, = cv2.boundingRect(cont)
        cv2.rectangle(next_frame_short, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("Practice", next_frame_short)
        cv2.imshow("Thresh", fgmask)
        print len(contour)
        #cv2.imshow("Change in Frame", frame_diff)
        cv2.waitKey(1)
        #cont_area_arr.append(cv2.contourArea(cont))
        #cont_area_arr = np.array(cont_area_arr)
