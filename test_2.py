#!/usr/bin/env python
import roslib
#roslib.load_manifest('my_package')
import sys
import rospy
import cv2

#include "std_msg/string.h"


#import geometry_msgs/Twist.h
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:

  def __init__(self):

    self.image_pub = rospy.Publisher("test",Image,queue_size=2)
    self.twist_pub = rospy.Publisher("/motor_controller/twist",Twist,queue_size=100)	
    cv2.namedWindow("Image window", 1)
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/depth/image",Image,self.callback)
    self.twist_msg = Twist()
    

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data)
    except CvBridgeError, e:
      print e

    (rows,cols) = cv_image.shape
   # if cols > 60 and rows > 60 :
    #  cv2.circle(cv_image, (rows/2,cols/2), 10, 255)
    #print cv_image[rows/2,cols/2]
    
    mindist = 10000000.0
    angle = 0.0
    found=0
    #find closest point(s)
    for i in range(rows/4,3*rows/4):
      for j in range(cols):
        if cv_image[i,j] < mindist:
          mindist = cv_image[i,j]
          angle = -50 + j*100/cols
    #Define velocities
    P = 0.05
    if mindist >= 0.8 or mindist<=0.4 or mindist == 'nan':
      forward_speed = 0
      angular_speed = 0
      found=0
    else:
        found=1
	if abs(angle)<40:
	  forward_speed = 0.5
	  angular_speed = 0.0
        else:
      	  forward_speed = 0.15
          angular_speed = -1*P*angle
    print found, angle, forward_speed,angular_speed

    self.twist_msg.linear.x=forward_speed
    self.twist_msg.angular.z=angular_speed   

    #cv2.imshow("Image window", cv_image)
    #cv2.waitKey(3)
    item_print =self.bridge.cv2_to_imgmsg(cv_image)

    self.twist_pub.publish(self.twist_msg)
    #try:
     # self.image_pub.publish(item_print)

      
      #self.image_pub.publish(cv_image)
    #except CvBridgeError, e:
     # print e

def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print "Shutting down"
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
