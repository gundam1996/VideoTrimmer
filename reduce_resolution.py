import cv2
import numpy as np

TARGET_SIZE = (1280, 720)
# TARGET_FPS = 60 # It might be complicated to use non-divisible number from target

# TARGET_SIZE = (640, 360)
TARGET_FPS = 60 # It might be complicated to use non-divisible number from target

# TARGET_SIZE = (7680, 4320)
# TARGET_FPS = 60 # It might be complicated to use non-divisible number from target

def reduce_quality(input_file, output_file):
	print(f"Parsing {input_file}")

	cap = cv2.VideoCapture(input_file)
	fourcc = cv2.VideoWriter_fourcc(*'avc1') # Apple's version of MPEG4 part 10 / H.264

	print(f"	Video FPS: {cap.get(cv2.CAP_PROP_FPS)}")

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
			if (TARGET_FPS != 60):
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
		if (file != ".DS_Store" or (len(file) > 1 and file[0] != '.')): # Do not take cache or hidden file into consideration
			reduce_quality(input_file=f"./{INPUT_FOLDER}/{file}", output_file=f"./{OUTPUT_FOLDER}/shortened_{file}")
else:
	print(f"Not sure what to do with: {sys.argv}")



