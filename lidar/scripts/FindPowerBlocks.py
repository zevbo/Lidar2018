import rospy
import math
import numpy as np
from sensor_msgs.msg import LaserScan
import PowerBlockDetection as PBD
import LidarDisplay as LD
import LidarLines as ll
import random

lastAngles = np.array([-1000.0,-1000.0,-1000.0])
lastLengths = np.array([-1000.0,-1000.0,-1000.0])

def lastBox():
	pairOne = math.fabs(lastAngles[0] - lastAngles[1])
	pairTwo = math.fabs(lastAngles[0] - lastAngles[2])
	pairThree = math.fabs(lastAngles[1] - lastAngles[2])
	closestAngles = max(pairOne,pairTwo,pairThree)
	if closestAngles == pairThree or closestAngles == pairTwo:
		return (lastAngles[0],lastLengths[0])
	else:
		return (lastAngles[1],lastLengths[1])


def callback(data):
    powerBlock = True
    time = 60
    displayRange = 5
    length = len(data.ranges)
    maxDistance = 2
    if powerBlock: 
	newRanges = np.ndarray(shape = (length))
	for i in range(length):
		if data.ranges[i] == float('inf'):
			newRanges[i] = 100
		else:
			newRanges[i] = data.ranges[i]
	powerBlock = PBD.findBox(newRanges)
	orientation = powerBlock[1]
	powerBlockAngle = powerBlock[0]
        if powerBlockAngle != ll.measurment/2 and data.ranges[ll.spot(powerBlockAngle)] < maxDistance:
	    coloredPoints = np.ndarray(shape = (length,2))
	    dis = data.ranges[ll.spot(powerBlockAngle)]
	    lastAngles[2] = lastAngles[1]
	    lastAngles[1] = lastAngles[0]
	    lastAngles[0] = powerBlockAngle
	    lastLengths[2] = lastLengths[1]
	    lastLengths[1] = lastLengths[0]
            lastLengths[0] = dis
	    print(powerBlockAngle)
	    print(dis)
	    print(int(orientation * 1000)/1000.0)
	    print("----------")
            pos = ll.spot(powerBlockAngle)
            cornerLen = data.ranges[pos]
            for i in range(len(coloredPoints)):
                if i - pos < displayRange and i - pos > 0 - displayRange:
                    coloredPoints[i][1] = 1
		else:
                    coloredPoints[i][1] = 0
                coloredPoints[i][0] = data.ranges[i]
            LD.displayPointsC(coloredPoints,time)
        else:
	    0
            #LD.displayPoints(data.ranges,time)
    else:
        0
        #LD.displayPoints(data.ranges,time)
def FindPowerBlocks():
    msg = "/scan"
    rospy.Subscriber(msg,LaserScan,callback)
    rospy.spin()
if __name__ == '__main__':
    rospy.init_node('FindPowerBlocks')
    FindPowerBlocks()

