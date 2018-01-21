from Tkinter import *


blockSeen = "Nothing"
distance = "N/A"
turning = "N/A"

h = 1000
w = 1000

def setAll(found,d,t,o):
	if found:
		blockSeen = "Block Found"
		distance = d
		turning = t
	else:
		blockSeen = "Nothing"
		distance = "N/A"
		turning = "N/A"

def display():
	dis = Tk()
	canvas = Canvas(dis, bg = "white", height = h, width = w)
	
	text = Text(dis)
	text.config(font = ("helvetica",24))
	text.config(height = 10)
	text.insert(INSERT,blockSeen)
	text.insert(INSERT,"\n")
	text.insert(END,distance)
	text.pack()

	dis.mainloop()
