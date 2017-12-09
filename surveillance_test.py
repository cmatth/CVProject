import imutils
import cv2
import numpy as np
import bounding_boxes as bb
import VideoGUI as vg

# Look into filming a scene for a "long time" to get an initial average frame of reference.

def count_frames(vid):
    # Determine the number of frames in a recorded video.
    tot_frames = int(vid.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
    return tot_frames

video_choice = vg.video_type()

if video_choice == 1:
    # Condition that continues while loop
    num_of_frames = np.inf
    # Index of webcam.
    cap = cv2.VideoCapture(0)
else:
    # Video that user selects.
    cap = cv2.VideoCapture(video_choice)
    # Get number of frames in recorded video.
    num_of_frames = count_frames(cap)
    condition = num_of_frames

bgSub = cv2.BackgroundSubtractorMOG()

frame_counter = 0

while frame_counter < num_of_frames:
    # Read frames of the video
    ret, next_frame = cap.read()
    frame_counter += 1

    next_frame_short = imutils.resize(next_frame, width = 400)

    next_frame_blur = cv2.GaussianBlur(next_frame_short, (21,21), 0)

    fgmask = bgSub.apply(next_frame_blur)

    # Dilate to complete outline of shape.
    dilation = cv2.dilate(fgmask, (5,5), iterations = 7)

    # Find contours.
    contour, _ = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create new contour area array.
    cont_area_arr = []

    x_arr = []
    y_arr = []
    w_arr = []
    h_arr = []

    # Determine how many contours are in the frame.
    num_of_contours = len(contour)

    for cont in contour:
        # Determine bounding box of contour.
        cont_area = cv2.contourArea(cont)
        x, y, w, h, = cv2.boundingRect(cont)
            #x_arr.append(x)
            #y_arr.append(y)
            #w_arr.append(w)
            #h_arr.append(h)

#    if len(x_arr) > 0:
#        x, y, w, h = bb.combine_boxes(x_arr, y_arr, w_arr, h_arr)
        cv2.rectangle(next_frame_short, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Practice", next_frame_short)
    cv2.imshow("Thresh", fgmask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


