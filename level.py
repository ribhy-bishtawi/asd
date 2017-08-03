import palgame
import pygame

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_HEIGHT1 = 300
pygame.mouse.set_visible(0)

# colors
PINK = (235, 8,114)
salmon = (250, 128, 114)
brown = (210,105,30)
red = (102,0,0)
blue = (0, 206, 209)
purple = (139,0,139)

bg = pygame.image.load("4.jpg")
from pygame import mixer
clock = pygame.time.Clock()
counter, text = 10, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
screen=palgame.build_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

#ball
global ball_radius
ball_radius = 10

# wall dimensions
rect_hight=20
rect_width=400
rect_hight1=400
rect_width1=20
rect_y = 100
rect_x = 100

#lists
no_move_wall_list = []
move_wall_list = []
seconde_move_wall_list=[]
seconde_no_move_wall_list = []

#music
mixer.music.load ('1.ogg')
mixer.music.play(-1)

#move wall 
for column in range(3):
	rect_x = 300 + column*250
	rect_y = 100
	move_wall_list.append([rect_x, rect_y])

#seconde move wall 	
for column in range(1):
	rect_x = 500 + column*700
	rect_y = 700
	seconde_move_wall_list.append([rect_x, rect_y])	

#image
bg= pygame.image.load("4.jpg")

# main screen
def begin_level2(counter, ball_radius):
	while True:
		mouse_x=palgame.get_mouse_location()[0]
		mouse_y=palgame.get_mouse_location()[1]

		palgame.get_event()
		palgame.clear_screen()
		screen.blit(bg, (0,0))
		
		# create and draw first walls that don't move
		for row in range (2):
			for column in range (4):
				rect_x = 150 + column*200
				rect_y = 0 + row*520
				no_move_wall_list.append([rect_x, rect_y])
		for k in range (8) :
			block = no_move_wall_list[k]
			# block[1] = block [1] + 5 
			palgame.draw_rect(block[0], block[1], rect_width, rect_hight, PINK)
		
		# move the move wall list
		for u in range(3):
			if u==1:
				move_wall_list[u][1] = move_wall_list[u][1] + 10
			else:
				move_wall_list[u][1] = move_wall_list[u][1] - 10
			move_wall_list[u][1] = move_wall_list[u][1] % 100
			block = move_wall_list[u]
			palgame.draw_rect(block[0], block[1] , rect_width1, rect_hight1, salmon)
		
		#move the seconde_move_wall_list
		for b in range(1):
			if b==1: 
				seconde_move_wall_list[b][0]= seconde_move_wall_list[b][0] +10
			else:
				seconde_move_wall_list[b][0]= seconde_move_wall_list[b][0] +10
			seconde_move_wall_list[b][0] = seconde_move_wall_list[b][0] % 600
			block = seconde_move_wall_list[b]
			palgame.draw_rect(block[0], block[1]-200 , rect_width, rect_hight, blue)
		for column in range (1):
			rect_x = 130+ column*200
			rect_y = 18 
			seconde_no_move_wall_list.append([rect_x, rect_y])
		for l in range (1) :
			block = seconde_no_move_wall_list[l]
			block_x = block[0]
			block_y = block[1]	
		palgame.draw_rect(block[0], block[1], rect_width1, rect_hight1+100, PINK)
			
		# check collisions1
		for k in range(8):
			block = no_move_wall_list[k]
			block_x = block[0]
			block_y = block[1]
			if (mouse_x > block_x and mouse_x < block_x + rect_width) and (mouse_y > block_y and mouse_y < block_y + rect_hight):
				print "game over"
				ball_radius = 0
		
		# check collisions2
		for u in range (3):
			block = move_wall_list[u]
			block_x = block[0]
			block_y = block[1]
			if(mouse_x > block_x and mouse_x< block_x + rect_width1)and(mouse_y > block_y and mouse_y < block_y + rect_hight1):
				print "game over"
				ball_radius = 0

		# check collisions3
		for b in range(1):
			block = seconde_move_wall_list[b]
			block_x = block[0]
			block_y = block[1]
			if (mouse_x > block_x and mouse_x < block_x + rect_width) and (mouse_y > 500 and mouse_y < 520):
				print "game over"
				ball_radius = 0
		# check collisions4		
		for l in range (1) :
			block = seconde_no_move_wall_list[l]
			block_x = block[0]
			block_y = block[1]	
			if(mouse_x > block_x and mouse_x< block_x + rect_width1)and(mouse_y > block_y and mouse_y < block_y + rect_hight1):
				print "game over"
			
		# win 
		if mouse_x <= 30:
			largeText = pygame.font.SysFont('monospace',200)	
			label = largeText.render("You win",1 , red) 
			screen.blit(label, (200, 100))
			break
		#break 
		if ball_radius == 0 :
			largeText = pygame.font.SysFont('monospace',150)	
			label = largeText.render("You lose",1 , red) 
			screen.blit(label, (100,100 ))
			break
		
		# draws the mouse circles
		palgame.draw_circle(mouse_x, mouse_y, ball_radius, brown)
		palgame.draw_everything() 
	
	#counter
	counter = 0
	while True:
		counter += 1
		if counter > 25:
			break
		
	palgame.get_event()
	palgame.draw_everything()
