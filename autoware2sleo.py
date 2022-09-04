#!/usr/bin/env python
import rospy
# from sensor_msgs.point_cloud2 import create_cloud
from geometry_msgs.msg import Twist,TwistStamped,PoseStamped
from geometry_msgs.msg import Vector3
from autoware_msgs.msg import VehicleCmd
import math
# ==============================================================================
# -- main() -------------------------edited by xhao-----------------------------
# ==============================================================================
class Transfer():
    def __init__(self):
        rospy.init_node('autoware_to_sleo', anonymous=True)
        self.twist_pub = rospy.Publisher('sleo_velocity_controller/cmd_vel',Twist,queue_size=100)
        rospy.Subscriber("/twist_raw",TwistStamped, self.TwistCallback)

    def TwistCallback(self,data):
        new_msg = Twist()
       # data.twist.angular.z = -data.twist.angular.z*int(data.twist.linear.x)/2
        new_msg = data.twist
        if abs(data.twist.angular.z) >100:
            new_msg=0.0
        self.twist_pub.publish(new_msg)
    
if __name__ == '__main__':
    Transfer()
    rospy.spin()


