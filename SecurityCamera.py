# import the necessary packages
from __future__ import print_function

from imutils.video import VideoStream
from imutils.io import TempFile
from datetime import datetime
from datetime import date
import numpy as np
import argparse
import imutils
import signal
import time
import cv2
import sys



print("Starting the camera camera...")
vs = VideoStream(src=0).start()
time.sleep(3.0)


ChangeInCurrentSnapShot = False
vid_writer = None
Width = None
Height = None



while True:

	frame = vs.read()
	ChangeInPrevSnapShot = ChangeInCurrentSnapShot

	if frame is None:
		break
	frame = imutils.resize(frame, width=200)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	

	if vid_writer is None or Height is None:
		(Height, Width) = frame.shape[:2]

	mean = np.mean(gray)
	
	ChangeInCurrentSnapShot = mean > 115


	if ChangeInCurrentSnapShot and not ChangeInPrevSnapShot:
		startTime = datetime.now()
		tempVideo = TempFile(ext=".mp4")
		vid_writer = cv2.VideoWriter(tempVideo.path, 0x21, 30, (W, H),
			True)
	elif ChangeInPrevSnapShot:
		timeDiff = (datetime.now() - startTime).seconds
        if ChangeInCurrentSnapShot and timeDiff > 5:
            vid_writer.release()
            vid_writer = None			
	if vid_writer is not None:
		writer.write(frame)

if vid_writer is not None:
	writer.release()

cv2.destroyAllWindows()
vs.stop()

