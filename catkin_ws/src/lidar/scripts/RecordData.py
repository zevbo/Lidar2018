import rospy
import numpy as np
from sensor_msgs.msg import LaserScan
import LidarLines as ll

#pattern matcher
#0 - power block

angle = 0
pattern = 0
measurments = 50

def isInt(s):
	try: 
		int(s)
		return True
	except ValueError:
		return False

def strToArray(string):
	expand = tuple(string)
	arrayLen = 1
	expandLen = len(expand)
	on = 0
	inOuter = 0
	while(on < expandLen):
		if expand[on] == '[':
			inOuter += 1
		if expand[on] == ']':
			inOuter -= 1
		if inOuter == 1 and expand[on] == ',':
			arrayLen += 1
		on += 1
			
	array = range(arrayLen)
	
	onA = 0
	on = 1
	arrayLen = len(array)
	while(on < expandLen - 1 and onA < arrayLen):
		if isInt(expand[on]) or type(expand[on]) is int:
			numberLen = 1
			while(on + numberLen + 1 < expandLen and isInt(expand[on + numberLen])):
				numberLen += 1
			array[onA] = int(''.join(expand[on:on + numberLen]))
			on += numberLen
			while(on < expandLen and not(expand[on - 1] == ' ')):
				on += 1
		else:
			miniArrayLen = 1
			layer = 1
			on += 1
			while(layer >= 1):	
				if expand[on] == '[':
					layer += 1
				if expand[on] == ']':
					layer -= 1
				on += 1
				miniArrayLen += 1
			joined = ''.join(expand[on - miniArrayLen:on])
			inner = strToArray(joined)
			array[onA] = inner
			on += 2
		onA += 1
	
	return array


def getData():
	f = open('data.txt','r')
	allData = f.readlines()
	f.close()
	f = open('data.txt','w')
	f.writelines(''.join(allData))
	f.close()
	return allData

def addArray(arr):
	f = open('data.txt','r')
	allData = f.readlines()
	allData[len(allData)] = ''.join(str(arr),'\n')
	f.close()
	f = open('data.txt','w')
	f.writelines(''.join(allData))
	f.close()

def callback(data):
	record = (data,angle,pattern)
	on = 0
	l = len(data.ranges)
	while(i <= l - measurments):
		if angle > on and angle < on + measurments:
			addArray([data.ranges[i:i + measurments],angle - on,pattern,1])
		else:
			addArray([data.ranges[i:i + measurments],-1,pattern,-1])

def RecordData():
	msg = "/scan"
	rospy.Subscriber(msg,LaserScan,callback)
	rospy.spin()

if __name__ == '__main__':
	rospy.init_node('RecordData')
	RecordData()
