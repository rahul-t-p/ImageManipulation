# Import opencv2 and sys
import cv2
import sys

for i in range(2,len(sys.argv)):
	# Read image
	image = cv2.imread(sys.argv[i])
	# Name of output image
	k = sys.argv[i].index('.')
	name = sys.argv[i][:k] + '_modified' + sys.argv[1]
	# Write image
	cv2.imwrite(name, image)

print 'Done...'
