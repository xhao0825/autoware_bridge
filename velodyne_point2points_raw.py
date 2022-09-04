# -*-coding:utf-8-*-
import rospy
from sensor_msgs.msg import PointCloud2

class Transfer():
    def __init__(self):
        #初始化节点
        rospy.init_node('transfer_topic_from_ego_lid1ar_to_points_raw')
        self.points_raw_pub = rospy.Publisher('/points_raw', PointCloud2, queue_size=100)

        #订阅lidar节点
        rospy.Subscriber('/velodyne_points', PointCloud2, self.callback_lidar)

        # 设置循环的频率
        rate = rospy.Rate(10)


    def callback_lidar(self,data):
        #重设frame_id
        data.header.frame_id="velodyne"

        # 发布消息
        self.points_raw_pub.publish(data)
        # print(data)
        
if __name__ == '__main__':
    Transfer()
    rospy.spin()

