import math
linePrecision = 0.2
measurment = 1
maxAngle = 30
def spot(angle): #Takes an angle and returns the place in the LIDAR point array which it's in
        return int(1/measurment * (angle + maxAngle))
def tooRec(angle,l): #Converts a point of the form (theta,R) to (X,Y)
        x = math.sin(math.radians(angle)) * l
        y = math.cos(math.radians(angle)) * l
        return(x,y)
def tooRecA(points,angle): #Takes an array of points and an angle and finds the (X,Y) point that measurment corresponds to
        return tooRec(angle,points[spot(angle)])
def findLine(p1,p2): #Takes two points of the form (X,Y) and returns (M,B) from y = mx + b equation that connects the two points
        denom = p1[0] - p2[0]
	if denom == 0:
		denom = 0.0001
	m = (p1[1] - p2[1])/denom
        b = p1[1] - p1[0]*m
        return (m,b)
def distance(p1,p2): #Takes two points of the form (X,Y) and returns the distance between them
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
def intersection(line1,line2): #Takes two lines of the form (M,B) and returns the (X,Y) where they intersect
        denom = line2[0] - line1[0]
	if denom == 0:
		denom = 0.0001
	x = (line1[1] - line2[1])/denom
        y = line1[0]*x + line1[1]
        return (x,y)
def expectedLength(line,angle): #Takes a line of the form (M,B) and an angle and returns the length of the line extending from (0,0) to the line at the specified angle
        myLine = findLine((0,0),tooRec(angle,1))
        return distance((0,0),intersection(line,myLine))
def onLine(line,angle,length): #Takes a line  of form (M,B), an angle and a length and returns wether or not it's close enough to the expected length
        return math.fabs(expectedLength(line,angle) - length) < linePrecision
def allOnLine(points,startingAngle,endAngle,line): #Takes an array of LIDAR points, two angles to scan between, and a line on which they should all fall. It returns if all the lengths are close enough to the given line
        while(startingAngle != endAngle and onLine(line,startingAngle,points[spot(startingAngle)])):
                startingAngle += measurment
        return startingAngle == endAngle
def isLine(points,sA,eA): #Takes an array of LIDAR points and two angles to scan between and returns wether all of the angles in between fall on the same line
        return allOnLine(points,sA,eA,findLine(tooRecA(points,sA),tooRec(points,eA)))
def lineEnd(points,ogPoint,angle,direction): #Scans backwards until it's no longer on the line
        maxM = 100
	minM = -100
	while(angle >= 0 - maxAngle and angle < maxAngle and maxM > minM):
		point = tooRecA(points,angle)
		hyp = distance(ogPoint,point)
		if hyp > linePrecision:
			baseAngle = math.atan((point[1] - ogPoint[1])/(point[0] - ogPoint[0]))
			uncertinatyAngle = math.asin(linePrecision/hyp)
			uncertianHyp = math.sqrt((point[0] - ogPoint[0]) ** 2 + (point[1] - ogPoint[1]) ** 2 - linePrecision ** 2)
			uncertianPoints = ((uncertianHyp * math.cos(baseAngle + uncertinatyAngle), uncertianHyp * math.sin(baseAngle + uncertinatyAngle)),
						(uncertianHyp * math.cos(baseAngle - uncertinatyAngle), uncertianHyp * math.sin(baseAngle - uncertinatyAngle)))
			possibleMs = (uncertianPoints[1] - ogPoint[1])/(uncertianPoints[0] - ogPoint[0])
			maxM = min(maxM,max(possibleMs))
			minM = max(minM,min(possibleMs))
                angle += direction * measurment
        return tooRecA(points,angle - 2 * direction * measurment)
#def lineEndFor(points,ogPoint,angle): #Scans forwards until it's no longer on the line
	#while(angle < maxAngle and onLine(line,angle,points[spot(angle)])):
        #        angle += measurment
        #return tooRecA(points,angle - measurment)

def intersectionAngle(line1,line2): #Takes two lines of form (M,B) and returns the angle that their intersction makes
        return math.degrees(math.atan(math.fabs(line1[0] * line2[0]))) * 2 

