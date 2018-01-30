import rospy
import math
import numpy as np
from sensor_msgs.msg import LaserScan
import LidarLines as ll
import CornerDetection as CD
import LidarDisplay as LD

def callback(data):
    time = 120
    displayRange = 5
    maxDistance = 4
    l = len(data.ranges)

    for i in data.ranges:
        if i == float('inf') or i > maxDistance:
            i = 100

    corner = CD.findCorner(data.ranges)
    if corner < 1000:
        
        coloredPoints = np.ndarray(shape = (l,2))

        for i in range(l):

            coloredPoints[i][0] = data.ranges[i]

            if math.fabs(i - ll.spot(corner[1])) < maxDistance:
                coloredPoints[i][1] = 1
            else:
                coloredPoints[i][1] = 0

        print("Corner found at ", corner[1], " degrees and ", data.ranges[ll.spot(corner[1])], " meters away")
        print("")
        LD.displayPointsC(coloredPoints)


def FindCorners():
    msg = "/scan"
    rospy.Subscriber(msg,LaserScan,callback)
    rospy.spin()

if __name__=='__main__':
    rospy.init_node('FindCorners')
    FindCorners()
