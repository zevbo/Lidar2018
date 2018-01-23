import rospy
from sensor_msgs.msg import LaserScan
import LidarDisplay as LD
import math

def callback(data):
	l = len(data)
	displayData = np.ndarray(size = (l,2))
	on = 0
	time = 120
	while(on < l):
		displayData[on][0] = data.ranges[on]
		if math.fabs(on) < 4:
			displayData[on][1] = 1
		elif math.fabs(on - l/3) < 4:
			displayData[on][1] = 2
		else:
			displayData[on][1] = 0 
	LD.displayPointsC(displayData,time)

def ShowData():
	msg = "/scan"
	rospy.Subscriber(msg,LaserScan,callback)

if __name__ == '__main__':
	rospy.init_node('ShowData')
	ShowData()
