
import numpy as np
import cv2
import argparse 



ap = argparse.ArgumentParser();

ap.add_argument('-i', '--image')
args = vars(ap.parse_args());


image = cv2.imread(args["image"])
# image_small = cv2.resize(image, (0,0), fx = 0.25, fy= 0.25)
image_standard = cv2.resize(image, (640, 480))
# print image.shape

# cv2.imshow("originalimage", image_small)
# cv2.imshow("originalimage", image_standard)
cv2.waitKey(0)

image_vec = np.reshape(image_standard[:,:,1], image_standard.shape[0] * image_standard.shape[1])
image_vec1 = np.ravel(image_standard[:,:,0])
print np.min(image_vec1)
print np.max(image_vec1)
# print np.reshape(image_standard[:,:,1], image_standard.shape[0] * image_standard.shape[1])[:,np.newaxis]
# exit()
# set color boundaries for red, green, blue, yellow, orange, light green, fluroscent green and violet.
boundaries = [
	([0, 0, 100], [60, 70, 255]),
	([0, 40, 0], [70, 220, 100]),
	([40, 0, 0], [220, 90, 110]),
	([0, 20, 70], [40, 220, 250]),
	([0, 60, 70], [30, 200, 210]),

]


# boundaries_hsv = [()]

# set color boundaries for red, green, blue, yellow, orange, light green, fluroscent green and violet.
hsv_image = cv2.cvtColor(image_standard, cv2.COLOR_BGR2HSV)
# r, g, b, y, v, o, fg

boundaries_hsv = [
	([135, 90, 90], [180, 255, 255]),
	([30, 90, 90], [75, 220, 220]),
	([90, 120, 120], [130, 255, 255]),
	([0, 100, 100], [25, 255, 255]),
	([130, 100, 100], [165, 255, 255]),
	([23, 110,110], [42, 255, 255]),
	([35, 200, 140], [75, 255, 255])
]
# cv2.imshow("hsvimage", hsv_image)
# cv2.waitKey(0)
# exit()

for (lower, upper) in boundaries:

	lower = np.array(lower, dtype="uint8")
	upper = np.array(upper, dtype="uint8")


	mask = cv2.inRange(image_standard, lower, upper)
	output = cv2.bitwise_and(image_standard, image_standard, mask=mask)

	cv2.imshow("images", np.hstack([image_standard, output]))
	cv2.waitKey(0)



for(lower_hsv, upper_hsv) in boundaries_hsv:

	lower_hsv = np.array(lower_hsv, dtype="uint8")
	upper_hsv = np.array(upper_hsv, dtype="uint8")

	mask_hsv = cv2.inRange(hsv_image, lower_hsv, upper_hsv)
	output_hsv = cv2.bitwise_and(hsv_image, hsv_image, mask = mask_hsv)

	cv2.imshow("images_hsv", np.hstack([hsv_image, output_hsv]))
	cv2.waitKey(0)


