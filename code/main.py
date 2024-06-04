import math

import pygame, sys
from settings import *
from world import World
from player import Player

pygame.init()

# game title and width + height, can be adjusted in settings.py
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

class Platformer:
	def __init__(self, screen, width, height):
		self.screen = screen
		self.clock = pygame.time.Clock()
		self.player_event = False

		# background terrain images

		self.bg_img = pygame.image.load('assets/terrain/bg.png').convert()
		self.bg_width = self.bg_img.get_width()

		self.bg_water = pygame.image.load('assets/trap/blade/spike.png').convert()

		# variables for bg
		self.scroll = 0
		self.bg_tiles = math.ceil(WIDTH / self.bg_width) + 1

	def main(self):
		world = World(world_map, self.screen)

		run = True
		while run:

			# draw scrolling background
			for i in range(0, self.bg_tiles):
				self.screen.blit(self.bg_img, (i * self.bg_width + self.scroll, 0))

			# scroll background
			self.scroll -= .5

			# reset scroll
			if abs(self.scroll) > self.bg_width:
				self.scroll = 0

			# background water
			# self.screen.blit(self.bg_water, (200,430))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					pygame.quit()
					sys.exit()

			# updating the world depending on key inputs.

				elif event.type == pygame.KEYDOWN:

					if event.key == pygame.K_LEFT:
						self.player_event = "left"

					if event.key == pygame.K_RIGHT:
						self.player_event = "right"
				
					if event.key == pygame.K_UP:
						self.player_event = "space"

				elif event.type == pygame.KEYUP:
					self.player_event = False

			# world updates and game fps
			world.update(self.player_event)
			pygame.display.update()
			self.clock.tick(60)


if __name__ == "__main__":
	play = Platformer(screen, WIDTH, HEIGHT)
	play.main()