from manim import *
import pygame

pygame.init()

width = 800
height = 600
running = True

# define classes here

pygame.display.set_caption("Window Title")
scrn = pygame.display.set_mode((width, height))
pp = pygame.image.load(r"path/to/file")
pygame.display.set_icon(pp)
font_size = 24
font = pygame.font.Font("freesansbold.ttf", font_size)
text = font.render("This is text.", True, GREEN_D)

# define functions here

while running:
	scrn.fill(BLACK)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	scrn.blit(text, (10, 1))

	pygame.display.update()

pygame.quit()