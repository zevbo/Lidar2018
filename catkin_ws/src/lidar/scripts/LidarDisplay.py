from Tkinter import *
import LidarLines as ll
from threading import Timer
w = 600
h = 600
scale = 50
dis = 0
def clear():
        global dis
        if dis != 0:
                dis.destroy()
def displayPoints(points,time):
        dis = Tk()
        canvas = Canvas(dis, bg = "white", height = h, width = w)
        i = 0 - ll.maxAngle
        while(i < ll.maxAngle - ll.measurment):
                pH = ll.tooRec(i,points[ll.spot(i)])
                nextPH = ll.tooRec(i+ll.measurment,points[ll.spot(i + ll.measurment)])
                p = (pH[0] * scale + w/2, pH[1] * scale + h/2)
                nextP = (nextPH[0] * scale + w/2, nextPH[1] * scale + h/2)
                point = canvas.create_line(p,nextP,fill = "red")
                i += ll.measurment
        canvas.pack()
        t = Timer(time,dis.destroy)
	t.start()
        dis.mainloop()
        t.cancel()
def displayPointsC(points,time):
        i = 0 - ll.maxAngle
        dis = Tk()
        canvas = Canvas(dis, bg = "white", height = h, width = w)
	def numToColor(num):
		if num == 0:
			return "red"
		if num == 1:
			return "blue"
		if num == 2:
			return "green"
        while(i < ll.maxAngle - ll.measurment):
                pH = ll.tooRec(i,points[ll.spot(i)][0])
                nextPH = ll.tooRec(i+ll.measurment,points[ll.spot(i + ll.measurment)][0])
                p = (pH[0] * scale + w/2, pH[1] * scale + h/2)
                nextP = (nextPH[0] * scale + w/2, nextPH[1] * scale + h/2)
                point = canvas.create_line(p,(w/2,h/2),fill = numToColor(points[ll.spot(i + ll.measurment)][1]),width = 1)
                i += ll.measurment
        canvas.pack()
        t = Timer(time,dis.destroy)
	t.start()
        dis.mainloop()
        t.cancel()

