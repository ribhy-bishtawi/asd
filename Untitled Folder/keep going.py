import turtle 
from running_man import Running_man
screen = turtle.getscreen()
turtle.tracer(1)
running_man1 = Running_man(0, 0, 0, 0)
turtle.ht()


screen.listen()



def upKeyPressed():
	running_man1.dy = running_man1.dy +1 
screen.onkey(upKeyPressed, "Up")
screen.listen()	
def downKeyPressed():
	running_man1.dy =running_man1.dy - 1 
screen.onkey(downKeyPressed,"Down")	
screen.listen()
def rightKeyPressed():
	running_man1.dx = running_man1.dx + 1 
screen.onkey(rightKeyPressed,"Right")	
screen.listen()
def leftKeyPressed():
	running_man1.dx = running_man1.dx - 1 
screen.onkey(leftKeyPressed,"Left")	
screen.listen()