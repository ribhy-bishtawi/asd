import palgame
import pygame

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
SCREEN_HEIGHT1 = 300
pygame.mouse.set_visible(0)
PINK = (218, 112,214)
salmon = (250, 128, 114)
brown = (210,105,30)
red = (102,0,0)
bg = pygame.image.load("4.jpg")
from pygame import mixer
screen=palgame.build_screen(SCREEN_WIDTH, SCREEN_HEIGHT)
clock = pygame.time.Clock()
counter, text = 10, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
ball_radius = 15
loop=2
direction_x=1
direction_y=1
movement_y=1
score = 0
spacebar_ticker=0
# wall dimensions
rect_hight=400
rect_width=20
rect_y = 100
rect_x = 100
#wall dimensions 2
rect_hight1=20
rect_width1=400
rect_y1= 100
rect_x1 = 100
no_move_wall_list = []
move_wall_list = []
mixer.init()
mixer.music.load ('1.ogg')
mixer.music.play(-1)
for column in range(4):
	rect_x = 300 + column*250
	rect_y = 100
	move_wall_list.append([rect_x, rect_y])	
while loop==2:
	palgame.get_event()
	palgame.clear_screen()
	largeText = pygame.font.SysFont('arialb',100)	
	label = largeText.render("Press space to play!",1 , red) 
	screen.blit(label, (70, 100))
# check if spacebar is pressed
	if pygame.key.get_pressed()[pygame.K_SPACE] == True:			
		if spacebar_ticker == 0:
			spacebar_ticker = 15
			loop=1
			# do action
			# d_paddle = x_paddle -2
			# dy *= 2
	if spacebar_ticker > 0:
		spacebar_ticker -= 1

	palgame.draw_everything()
while loop==1:
	mouse_x=palgame.get_mouse_location()[0]
	mouse_y=palgame.get_mouse_location()[1]
	palgame.get_event()
	palgame.clear_screen()
	screen.blit(bg, (0,0))
	# create and draw first walls that don't move
	for row in range (2):
		for column in range (5):
			rect_x = 200 + column*250
			rect_y = 0 + row*450
			no_move_wall_list.append([rect_x, rect_y])
	for k in range (10) :
		block = no_move_wall_list[k]
		# block[1] = block [1] + 5 
		palgame.draw_rect(block[0], block[1], rect_width, rect_hight, PINK)
	# move the second wall list
	for u in range(4):
		if u==1:
			move_wall_list[u][1] = move_wall_list[u][1] + 10
		else:
			move_wall_list[u][1] = move_wall_list[u][1] - 10
		move_wall_list[u][1] = move_wall_list[u][1] % 300
		block = move_wall_list[u]
		palgame.draw_rect(block[0], block[1] , rect_width, rect_hight, salmon)
	# check collisions1
	for k in range(10):
		block = no_move_wall_list[k]
		block_x = block[0]
		block_y = block[1]
		if (mouse_x > block_x and mouse_x < block_x + rect_width) and (mouse_y > block_y and mouse_y < block_y + rect_hight):
			print "game over"
			largeText = pygame.font.SysFont('monospace',200)	
			label = largeText.render("You lose",1 , red) 
			screen.blit(label, (200, 100))
			ball_radius = 0	
	# check collisions2
	for u in range (4):
		block = move_wall_list[u]
		block_x = block[0]
		block_y = block[1]
		if(mouse_x > block_x and mouse_x< block_x + rect_width)	and(mouse_y > block_y and mouse_y < block_y + rect_hight):
			print "game over"
			ball_radius = 0
		if mouse_x >= 1200:
			largeText = pygame.font.SysFont('monospace',200)	
			label = largeText.render("You win",1 , red) 
			screen.blit(label, (100, 100))
	if ball_radius == 0 :
		largeText = pygame.font.SysFont('monospace',200)	
		label = largeText.render("You lose",1 , red) 
		screen.blit(label, (200, 100))
		break
	if mouse_x >= 1200:
		break
	# draws the mouse circles
	palgame.draw_circle(mouse_x, mouse_y, ball_radius, brown)
	palgame.draw_everything()

counter = 0
while True:
	counter += 1
	if counter > 25:
		break
	palgame.get_event()
	palgame.draw_everything()