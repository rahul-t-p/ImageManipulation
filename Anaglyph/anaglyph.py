import cv2
import numpy as np
import sys

def anaglyph(image):
    height, width = image.shape[:2]
    # Spliting components
    B, G, R = cv2.split(image)

    # Creating a zero matrix for filtering
    zeros = np.zeros(image.shape[:2], dtype = 'uint8')
    # Red filtering(sub image1)
    limage = cv2.merge([zeros, zeros, R])
    # Cyan filtering(sub image2)
    rimage = cv2.merge([B, G, zeros])

    # translation on image2
    y_shift = 5
    x_shift = 5
    # translational matrix T
    T = np.float32([[1, 0, x_shift], [0, 1, y_shift]])
    img_translation = cv2.warpAffine(rimage, T, (width, height))

    # Merging image1 and modified image2
    merged = cv2.add(limage, img_translation)
    # Removing non merged regions
    global cropped
    cropped = merged[y_shift:height, x_shift:width]
    return cropped

def main():
    for i in range(1,len(sys.argv)):
        # Read image
        image = cv2.imread(sys.argv[i])
        
        anaglyph(image)
        
        # Name of output image
        k = sys.argv[i].index('.')
        name = sys.argv[i][:k] + '_anaglyph' + sys.argv[i][k:]
        # Write image
        cv2.imwrite(name, cropped)

if (__name__ == "__main__"):
	main()
	print('Done!..')




