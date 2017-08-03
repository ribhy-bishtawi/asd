import palgame
import pygame

while True:




	palgame.get_event()
	palgame.clear_screen()

	largeText = pygame.font.SysFont('monospace',200)	
	label = largeText.render("You lose",1 , red) 
	screen.blit(label, (200, 100))

















	palgame.get_event()
	palgame.draw_everything()