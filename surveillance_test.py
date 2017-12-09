import imutils
import cv2
import numpy as np
import bounding_boxes as bb
import VideoGUI as vg
from imutils.object_detection import non_max_suppression

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

bgSub = cv2.BackgroundSubtractorMOG2()

frame_counter = 0

while frame_counter < num_of_frames:
    # Read frames of the video
    ret, next_frame = cap.read()
    frame_counter += 1

    next_frame_short = imutils.resize(next_frame, width = 500)

    next_frame_blur = cv2.GaussianBlur(next_frame_short, (21,21), 0)

    fgmask = bgSub.apply(next_frame_blur)

    # Dilate to complete outline of shape.
    dilation = cv2.dilate(fgmask, (5,5), iterations = 7)

    # Find contours.
    contour, _ = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create new contour area array.
    cont_area_arr = []

    # Determine how many contours are in the frame.
    num_of_contours = len(contour)
    rects = []

    for cont in contour:
        # Determine bounding box of contour.
        cont_area = cv2.contourArea(cont)
        if cont_area > 1000:
            rects.append(cv2.boundingRect(cont))
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    #print rects
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.25)

    for (xA, yA, xB, yB) in pick:
        cv2.rectangle(next_frame_short, (xA, yA), (xB, yB), (0, 255, 0), 2)

    cv2.imshow("Practice", next_frame_short)
    cv2.imshow("Thresh", fgmask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


