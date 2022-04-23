import cv2
import numpy as np

# expected_size = (1280, 720)
expected_size = (640, 360)
expected_fps = 5

cap = cv2.VideoCapture('./target.MOV')
fourcc = cv2.VideoWriter_fourcc(*'avc1') # Apple's version of MPEG4 part 10 / H.264

out = cv2.VideoWriter('output.MOV', fourcc, 20, expected_size)
count = 100
while True:
	ret, frame = cap.read()
	if ret == True:
		b = cv2.resize(frame, expected_size, fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
		out.write(b)

		###################
		# Extra 2 read-without-write to reduce frame rate slowdown
		# If we want to allow created video to contain slow motion, we need to 
		#   comment out this extra rate while maintaining reduced frame rate
		#   comparing to source
		ret, frame = cap.read()
		ret, frame = cap.read()

		###################
		# Debug only
		# cv2.imshow('resized_frame', b)
		# cv2.waitKey(10)
		# break
		# if (count > 100):
		# 	break
		# else:
		# 	count += 1
	else:
		break

cap.release()
out.release()
cv2.destroyAllWindows()