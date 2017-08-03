import palgame
import pygame
mouse_x = 100
mouse_y = 100
def check_arrows(mouse_x, mouse_y):
	spacebar_ticker = 15
	#arrows 
	#ARROW UP Y = Y - NUMBER
	if pygame.key.get_pressed()[pygame.K_UP] == True:	
		mouse_y -= 15		
	#ARROW DOWN Y = Y + NUMBER
	if pygame.key.get_pressed()[pygame.K_DOWN] == True:			
		mouse_y += 15		
	#ARROW LEFT X = X - NUMBER
	if pygame.key.get_pressed()[pygame.K_LEFT] == True:			
		mouse_x -= 15		
	#ARROW RIGHT X = X + NUMBER
	if pygame.key.get_pressed()[pygame.K_RIGHT] == True:			
		mouse_x += 15		
	return [mouse_x, mouse_y]

def run_level1(no_move_wall_list, second_no_move_wall_list, move_wall_list):
	global mouse_x
	global mouse_y
	arrows = check_arrows(mouse_x, mouse_y) 
	mouse_x, mouse_y = arrows[0], arrows[1]

	#colors
	PINK = (218, 112, 214)
	salmon = (250, 128, 114)
	brown = (210, 105, 30)
	red = (102, 0, 0)
	blue = (0, 206, 209)
	purple = (139, 0, 139)

	# ball
	ball_radius = 15

	# wall dimensions
	rect_hight = 400
	rect_width = 20
	rect_hight2 = 20
	rect_width2 = 1000
	x = 150
	y = 29
	# mouse_x = palgame.get_mouse_location()[0]
	# mouse_y = palgame.get_mouse_location()[1]
	palgame.get_event()
	palgame.clear_screen()
	screen.blit(bg, (0,0))
	
	# draw the first and second wall list (stationary)
	for k in range (10) :
		block = no_move_wall_list[k] 
		palgame.draw_rect(block[0], block[1], rect_width, rect_hight, PINK)
	#draw the seconde no move wall list
	for j in range (6):
		block = second_no_move_wall_list[j]
		block_x = block[0]
		block_y = block[1]	
		palgame.draw_rect(block[0], block[1], rect_width2, rect_hight2, PINK)

	# draw and move the seconde wall list
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
			label = largeText.render("you lose",1 , red) 
			screen.blit(label, (200, 100))
			ball_radius = 0			
	
	# check collisions2
	for u in range (4):
		block = move_wall_list[u]
		block_x = block[0]
		block_y = block[1]
		if(mouse_x > block_x and mouse_x< block_x + rect_width)	and(mouse_y > block_y and mouse_y < block_y + rect_hight):
			print "game over"
			largeText = pygame.font.SysFont('monospace',200)	
			label = largeText.render("you lose",1 , red) 
			screen.blit(label, (200, 100))
			ball_radius = 0
		if mouse_x >=1250:
			return WIN

	# check collisions3
	for j in range (6):
		block = second_no_move_wall_list[j]
		block_x = block[0]
		block_y = block[1]	
		if (mouse_x > block_x and mouse_x < block_x + rect_width2) and (mouse_y > block_y and mouse_y < block_y + rect_hight2):
			print "game over"
			largeText = pygame.font.SysFont('monospace',200)	
			label = largeText.render("you lose",1 , red) 
			screen.blit(label, (200, 100))
			ball_radius = 0					
	
	# Game Over			
	if ball_radius == 0 :
		return LOSE

	# Draws the mouse circles
	palgame.draw_circle(arrows[0], arrows[1], ball_radius, brown)
	palgame.draw_everything()

	return KEEP_PLAYING

def run_level2 (no_move_wall_list, second_no_move_wall_list, move_wall_list, second_move_wall_list):
	global mouse_x
	global mouse_y
	arrows = check_arrows(mouse_x, mouse_y)
	mouse_x, mouse_y = arrows[0], arrows[1]
	#colors
	PINK = (218, 112,214)
	salmon = (250, 128, 114)
	brown = (210,105,30)
	red = (102,0,0)
	blue = (0, 206, 209)
	purple = (139,0,139)

	# ball radius
	ball_radius = 10

	# wall dimensions
	rect_hight=20
	rect_width=400
	rect_hight1=400
	rect_width1=20

	# mouse_x = palgame.get_mouse_location()[0]
	# mouse_y = palgame.get_mouse_location()[1]

	palgame.get_event()
	palgame.clear_screen()
	screen.blit(bg, (0,0))
	
	# draw the first walls that don't move
	for k in range(8) :
		block = no_move_wall_list[k]
		# block[1] = block [1] + 5 
		palgame.draw_rect(block[0]-300, block[1], rect_width+200, rect_hight, PINK)
	
	# move the move wall list
	for u in range(4):
		if u == 1:
			move_wall_list[u][1] = move_wall_list[u][1] + 10
		else:
			move_wall_list[u][1] = move_wall_list[u][1] - 10
		move_wall_list[u][1] = move_wall_list[u][1] % 100
		block = move_wall_list[u]
		palgame.draw_rect(block[0], block[1] , rect_width1, rect_hight1, salmon)
	
	# move the second_move_wall_list
	for b in range(1):
		if b==1: 
			second_move_wall_list[b][0]= second_move_wall_list[b][0] +10
		else:
			second_move_wall_list[b][0]= second_move_wall_list[b][0] +10
		second_move_wall_list[b][0] = second_move_wall_list[b][0] % 600
		block = second_move_wall_list[b]
		palgame.draw_rect(block[0], block[1]-200 , rect_width, rect_hight, salmon)
	for l in range (1) :
		block = second_no_move_wall_list[l]
		block_x = block[0]
		block_y = block[1]	
	palgame.draw_rect(block[0], block[1], rect_width1, rect_hight1+100, PINK)
		
	# check collisions1
	for k in range(8):
		block = no_move_wall_list[k]
		block_x = block[0]-300
		block_y = block[1]
		if (mouse_x > block_x and mouse_x < block_x + rect_width+200) and (mouse_y > block_y and mouse_y < block_y + rect_hight):
			print "game over"
			ball_radius = 0
	
	# check collisions2
	for u in range (4):
		block = move_wall_list[u]
		block_x = block[0]
		block_y = block[1]
		if(mouse_x > block_x and mouse_x< block_x + rect_width1)and(mouse_y > block_y and mouse_y < block_y + rect_hight1):
			print "game over"
			ball_radius = 0

	# check collisions3
	for b in range(1):
		block = second_move_wall_list[b]
		block_x = block[0]
		block_y = block[1]
		if (mouse_x > block_x and mouse_x < block_x + rect_width) and (mouse_y >(block_y-200) and mouse_y < 520):
			print "game over"
			ball_radius = 0
	# check collisions4		
	for l in range (1) :
		block = second_no_move_wall_list[l]
		block_x = block[0]
		block_y = block[1]	
		if(mouse_x > block_x and mouse_x< block_x + rect_width1)and(mouse_y > block_y and mouse_y < block_y + rect_hight1+100):
			print "you win"
			largeText = pygame.font.SysFont('monospace',150)	
			label = largeText.render("You win",1 , red) 
			screen.blit(label, (100,100 ))
			return WIN
	#break 
	if ball_radius == 0 :
		largeText = pygame.font.SysFont('monospace',150)	
		label = largeText.render("You lose",1 , red) 
		screen.blit(label, (100,100 ))
		return LOSE
	
	# draws the mouse circles
	palgame.draw_circle(arrows[0], arrows[1], ball_radius, brown)
	palgame.draw_everything() 

	return KEEP_PLAYING

# pause the game for some time
def pause_game():
	counter = 0
	while True:
		counter += 1
		if counter > 30:
			break
	palgame.get_event()
	palgame.draw_everything()


############################ GAME ACTION ###############################

#screen dimensions
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 600

#colors
PINK = (218, 112,214)
salmon = (250, 128, 114)
brown = (210,105,30)
red = (102,0,0)
blue = (0, 206, 209)
purple = (139,0,139)

# game states
WIN = 0
LOSE = 1
KEEP_PLAYING = 2

# background image
pygame.mouse.set_visible(0)
bg = pygame.image.load("4.jpg")

from pygame import mixer
screen=palgame.build_screen(SCREEN_WIDTH, SCREEN_HEIGHT)
clock = pygame.time.Clock()
text = '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)

# sound
mixer.init()
mixer.music.load ('1.ogg')
mixer.music.play(-1)

spacebar_ticker = 0

# starting screen loop	
loop = 2 
while loop == 2:
	palgame.get_event()
	palgame.clear_screen()
	screen.blit(bg, (0,0))
	largeText = pygame.font.SysFont('arialb',100)	
	label = largeText.render("Press space to play!",1 , red) 
	screen.blit(label, (300, 200))
	
	# check if spacebar is pressed
	if pygame.key.get_pressed()[pygame.K_SPACE] == True:			
		if spacebar_ticker == 0:
			spacebar_ticker = 15
			loop = 1
	if spacebar_ticker > 0:
		spacebar_ticker -= 1

	palgame.draw_everything()

# lists
no_move_wall_list = []
second_no_move_wall_list = []
move_wall_list = []
second_move_wall_list=[]


# main game loop
lists_intialized = False
game_level = 1
while loop == 1:
	if game_level == 1:
		if lists_intialized == False:
			# create the first wall list that don't move
			for row in range (2):
				for column in range (5):
					rect_x = 200 + column*250
					rect_y = 0 + row*450
					no_move_wall_list.append([rect_x, rect_y])
			# create the second wall list that don't move
			for row in range (2):
				for column in range (3):
					rect_x = 200 + column*250
					rect_y = 0 + row*580	
					second_no_move_wall_list.append([rect_x, rect_y])
			# creates the move wall list
			for column in range(4):
				rect_x = 300 + column*250
				rect_y = 100
				move_wall_list.append([rect_x, rect_y])
			lists_intialized = True
		
		# run the game for one round, and check result
		game_state = run_level1(no_move_wall_list, second_no_move_wall_list, move_wall_list)
		if game_state == WIN:
			pause_game()
			game_level = 2
			lists_intialized = False
		elif game_state == LOSE:
			pause_game()
			break

	elif game_level == 2:
		if lists_intialized == False:
			# set each list to be empty
			no_move_wall_list[:] = []
			second_no_move_wall_list[:] = []
			move_wall_list[:] = []
			second_move_wall_list[:] = []
			# create the first walls that don't move
			for row in range (2):
				for column in range (4):
					rect_x = 150 + column*200
					rect_y = 0 + row*500
					no_move_wall_list.append([rect_x, rect_y])
			# create the second walls that don't move
			for column in range (1):
				rect_x = 130+ column*200
				rect_y = 18 
				second_no_move_wall_list.append([rect_x, rect_y])
			# create the first wall list that moves
			for column in range(4):
				rect_x = 200 + column*250
				rect_y = 100
				move_wall_list.append([rect_x, rect_y])
			# create the second wall list that moves	
			for column in range(1):
				rect_x = 500 + column*700
				rect_y = 670
				second_move_wall_list.append([rect_x, rect_y])	
			lists_intialized = True
		
		# run the game for one round, and check result
		game_state = run_level2(no_move_wall_list, second_no_move_wall_list, move_wall_list, second_move_wall_list)
		if game_state == WIN or game_state == LOSE:
			pause_game()
			break 