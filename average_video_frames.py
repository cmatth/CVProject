import cv2
import numpy as np
def average_frames(video):
	cap = cv2.VideoCapture(video)
	ret, frames = cap.read()
	Video_end = False
	frame_count = 0
	while not Video_end:
		ret, next_frame = cap.read()
		if ret == False:
			Video_end = True
			continue
		else:
			frames = np.add(frames,next_frame)
			frame_count += 1

	frames = frames / frame_count
	return frames

avg = average_frames('button.MP4')
cv2.imshow("Average", avg)
cv2.waitKey(0)
