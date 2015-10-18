
import numpy as np
import cv2
import argparse 



ap = argparse.ArgumentParser();

ap.add_argument('-i', '--image')
args = vars(ap.parse_args());




def writeToFile(filename, data):
	with file(filename, 'w') as outfile:
		# outfile.write('# Array shape: {0}\n'.format(data.shape))
		for data_slice in data:
			np.savetxt(outfile, data_slice, fmt='%-7.2f')
			# outfile.write('\n')



image = cv2.imread(args["image"])
# image_small = cv2.resize(image, (0,0), fx = 0.25, fy= 0.25)
image_standard = cv2.resize(image, (1024, 768))
print image_standard.shape

# cv2.imshow("originalimage", image_small)
# cv2.imshow("originalimage", image_standard)
# cv2.waitKey(0)

image_vec = np.reshape(image_standard[:,:,1], image_standard.shape[0] * image_standard.shape[1])
image_vec1 = np.ravel(image_standard[:,:,0])

# cv2.imshow("originalimage", img_green)
# cv2.waitKey(0)
# exit()

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


# img_green = image_standard[165:210, 260:300, :];
img_red = image_standard[350:390, 265:300, :]
img_vio = image_standard[510:550, 190:235, :]
img_yellow = image_standard[580:630, 370:410, :]
img_gl = image_standard[205:255, 585:615]
img_gd = image_standard[165:205, 260:290, :]
img_bd = image_standard[380:425, 705:740]
img_bl = image_standard[440:475, 400:440]
img_orange = image_standard[610:650, 565:595]

img_re_hsv = hsv_image[350:390, 265:305]
img_vi_hsv = hsv_image[510:550, 190:235]
img_ye_hsv = hsv_image[580:630, 370:410]
img_gl_hsv = hsv_image[205:255, 585:615]
img_gd_hsv = hsv_image[165:205, 260:290]
img_bd_hsv = hsv_image[380:425, 705:740]
img_bl_hsv = hsv_image[440:475, 400:440]
img_or_hsv = hsv_image[610:650, 565:595]

print img_bl_hsv[1:5,1:5,:]

# cv2.imshow("green",img_bl);
# cv2.waitKey(0);

# np.savetxt('red_hsv.txt', img_red_hsv)

# data = img_red_hsv

writeToFile('red_hsv.txt', img_re_hsv)
writeToFile('gd_hsv.txt', img_gd_hsv)
writeToFile('gl_hsv.txt', img_gl_hsv)
writeToFile('bl_hsv.txt', img_bl_hsv)
writeToFile('bd_hsv.txt', img_bd_hsv)
writeToFile('ye_hsv.txt', img_ye_hsv)
writeToFile('or_hsv.txt', img_or_hsv)
writeToFile('vi_hsv.txt', img_vi_hsv)


# with file('red_hsv.txt', 'w') as outfile:
#     outfile.write('# Array shape: {0}\n'.format(data.shape))
#     for data_slice in data:
#         np.savetxt(outfile, data_slice, fmt='%-7.2f')

#         # Writing out a break to indicate different slices...
#         outfile.write('# New slice\n')



