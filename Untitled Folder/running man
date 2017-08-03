from turtle import Turtle
class Running_man(Turtle):
	dx = 0
	dy = 0
	width = 0
	height = 0
	def __init__(self, x, y, dx, dy):
		Turtle.__init__(self)
		self.pu()
		self.goto(x, y)
		self.dx = dx
		self.dy = dy
		self.shape("turtle")

	def move(self):
		oldy = self.ycor()
		newy = oldy + self.dy
		self.goto(10,newy)
		self.dy -=1
		if self.ycor() <= self.window_height() :
			self.dy == 0