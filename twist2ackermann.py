import rospy
# from autoware_msgs.msg import VehicleCmd
from yhs_can_msgs.msg import ctrl_cmd
from geometry_msgs.msg import TwistStamped

class twist2ackermann():
    def __init__(self):
        rospy.init_node('twist_to_ackermann',anonymous=True)
        self.mov_cmd_vel = ctrl_cmd()
        self.cmd_vel = TwistStamped()

        self.cmd_vel_sub = rospy.Subscriber('twist_cmd', TwistStamped, self.callback)
        rospy.sleep(2)
        self.cmd_vel_pub = rospy.Publisher('ctrl_cmd', ctrl_cmd, queue_size=10)
        self.rate = rospy.Rate(10)

        while not rospy.is_shutdown():
            self.transform()


    def callback(self,data):
        self.cmd_vel = data

    def transform(self):
        self.mov_cmd_vel.ctrl_cmd_gear = 4
        self.mov_cmd_vel.ctrl_cmd_velocity = self.cmd_vel.twist.linear.x
        self.mov_cmd_vel.ctrl_cmd_steering = self.cmd_vel.twist.angular.z
        self.cmd_vel_pub.publish(self.mov_cmd_vel)
        self.rate.sleep()


if __name__ == '__main__':
    twist2ackermann()