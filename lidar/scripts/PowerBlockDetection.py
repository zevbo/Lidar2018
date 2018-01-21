import LidarLines as ll
import math
anglePresicion = 20
boxLength = .255
boxPresicion = .075
minimumView = 2 * ll.measurment

def isBoxCorner(points,angle): #Sees if their is a power block with a corner at the given angle
	#line1 = ll.findLine(ll.tooRecA(points,angle + ll.measurment),ll.tooRecA(points,angle + minimumView))
        #line2 = ll.findLine(ll.tooRecA(points,angle - ll.measurment),ll.tooRecA(points,angle - minimumView))
        cornerPoint = ll.tooRecA(points,angle)
	cornerD = ll.distance(cornerPoint,(0,0))
	side1End = ll.lineEnd(points,ll.tooRecA(points,angle + 2 * ll.measurment),angle + minimumView,1)
        side2End = ll.lineEnd(points,ll.tooRecA(points,angle - 2 * ll.measurment),angle - minimumView,-1)
	line1 = ll.findLine(cornerPoint,side1End)
	line2 = ll.findLine(cornerPoint,side2End)
        #cornerPoint = ll.intersection(line1,line2)
        if math.fabs(math.degrees(math.atan(line1[0] * line2[0])) * 2 + 90) < anglePresicion:
		#print(line1)
		#print(line2) 
		#print(math.fabs(math.degrees(math.atan(line1[0] * line2[0]))) * 2)
		#print(anglePresicion)
		#print("-------")
		#math.fabs(ll.intersectionAngle(line1,line2) - 90) < anglePresicion
		if angle < 100 and angle > 75 and ll.distance(side1End,cornerPoint) < 2 and cornerD < 1:
			#print(ll.distance(side1End,cornerPoint))
			#print(ll.distance(side2End,cornerPoint))
			#print(angle)
			#print("------------")
			0
		return ((math.fabs(ll.distance(side1End,cornerPoint) - boxLength) < boxPresicion
                and math.fabs(ll.distance(side2End,cornerPoint) - boxLength) < boxPresicion
		and cornerD < ll.distance(side1End,(0,0))
		and cornerD < ll.distance(side2End,(0,0))), ll.findLine(side1End,side2End)[0])
def findBox(points): #Returns the angle pointing at the corner of a box
	angleOn = 0 - ll.maxAngle + minimumView
	def thisBox():
		temp = isBoxCorner(points,angleOn)
		return temp and temp[0]
        while(angleOn < ll.maxAngle - minimumView and not(thisBox())):
                angleOn += ll.measurment
        if angleOn >= ll.maxAngle - minimumView:
                return (ll.measurment/2,ll.measurment/2)
        else:	
		orientation = isBoxCorner(points,angleOn)[1]
                return (angleOn,orientation)

