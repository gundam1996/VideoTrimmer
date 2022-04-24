import cv2
import numpy as np

TARGET_SIZE = (640, 360)
TARGET_FPS = 20 # It might be complicated to use non-divisible number from target

def reduce_quality(input_file, output_file):
	cap = cv2.VideoCapture(input_file)
	fourcc = cv2.VideoWriter_fourcc(*'avc1') # Apple's version of MPEG4 part 10 / H.264

	out = cv2.VideoWriter(output_file, fourcc, TARGET_FPS, TARGET_SIZE)
	count = 100
	while True:
		ret, frame = cap.read()

		if ret == True:
			b = cv2.resize(frame, TARGET_SIZE, fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
			out.write(b)

			# print(type(frame), len(frame))
			# print(len(frame), len(frame[0]), len(frame[0][0]))
			# print(TARGET_SIZE[0], TARGET_SIZE[1], 3)
			# print(frame.flatten(), len(frame.flatten()), type(bytearray(frame.flatten())), TARGET_SIZE[0] * TARGET_SIZE[1] * 3)			

			print(cap.get(cv2.CAP))

			# print("")
			# print(type(b), len(b))
			# print(len(b), len(b[0]), len(b[0][0]))
			# print()

			break

			# print(cap.get(cv2.CAP_PROP_POS_MSEC))

			# count -= 1

			# if (count < 90):
			# 	break

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


reduce_quality(input_file='./target.MOV', output_file='./output.MOV')



