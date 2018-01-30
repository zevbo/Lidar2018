import math
import LidarLines as ll

view = 10 * ll.measurment
angleAccuracy = 40
lengthAccuracy = .1
angleBig = 141
angleSmall = 128.6
length = 2.54 * (10.25 ** 0.5)
 
def isCorner(points,angle):
    angle1 = ll.lineEndA(points,ll.tooRecA(points,angle),angle,1)
    angle2 = ll.lineEndA(points,ll.tooRecA(points,angle),angle,-1)
    
    if not(ll.isLine(points,angle1,angle2)):
        return (false,0)
    
    p1 = ll.tooRecA(points,angle1)
    p2 = ll.tooRecA(points,angle2)
    
    line = ll.findLine(p1,p2)

    if angle1 + view >= ll.maxAngle or angle2 - view < 0 - ll.maxAngle:
            return(false,0)

    lineLeft = ll.findLine(p1,tooRecA(points,angle1 + view))        
    lineRight = ll.findLine(p2,tooRecA(points,angle2 - view))
    
    interAngle1 = ll.intersectionAngle(lineLeft,line)
    interAngle2 = ll.intersectionAngle(lineRight,line)
    
    if (ll.isLine(points,angle1,angle1 + view) and
            ll.isLine(points,angle2,angle2 - view) and
            math.fabs(max(interAngle1,interAngle2) - angleBig) < angleAccuracy  and
            math.fabs(min(interAngle1,interAngle2) - angleSmall) < angleAccuracy and
            ll.distance(p1,p2)):
        return (true,(angle1 + angle2)/2)
        return (false,0)


def findCorner(points):
    angleOn = 0 - ll.measurment

    while(angleOn < ll.maxAngle):
        cornerFound = isCorner(points,angleOn)
        if cornerFound[0]:
            return cornerFound[1]
        angleOn += ll.measurment

    return 1000
