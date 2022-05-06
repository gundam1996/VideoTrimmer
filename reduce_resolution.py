import cv2
import numpy as np

TARGET_SIZE = (640, 360)
TARGET_FPS = 20 # It might be complicated to use non-divisible number from target

# TARGET_SIZE = (7680, 4320)
# TARGET_FPS = 60 # It might be complicated to use non-divisible number from target

def reduce_quality(input_file, output_file):
	cap = cv2.VideoCapture(input_file)
	fourcc = cv2.VideoWriter_fourcc(*'avc1') # Apple's version of MPEG4 part 10 / H.264

	out = cv2.VideoWriter(output_file, fourcc, TARGET_FPS, TARGET_SIZE)

	while True:
		ret, frame = cap.read()

		if ret == True:
			b = cv2.resize(frame, TARGET_SIZE, fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
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


import sys, os

if (len(sys.argv) > 2):
	INPUT_FOLDER = sys.argv[1]
	OUTPUT_FOLDER = sys.argv[2]

	for file in os.listdir(INPUT_FOLDER):
		# reduce_quality(input_file=f"./{file}", output_file=f"{OUTPUT_FOLDER/shortened_{file}}")
		print(f"./{file}", f"{OUTPUT_FOLDER}/shortened_{file}")

		# reduce_quality(input_file='./target_short.MOV', output_file='./output.MOV')
else:
	print(f"Not sure what to do with: {sys.argv}")



