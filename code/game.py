import pygame
import sys
from settings import HEIGHT, WIDTH

pygame.font.init()

class Game:
	def __init__(self, screen):
		self.screen = screen
		self.font = pygame.font.SysFont('VCRosdNEUE', 70)
		self.message_color_win = pygame.Color("green")
		self.message_color_lose = pygame.Color("red")

	# if player ran out of life or fell below the platform
	def _game_lose(self, player):
		player.game_over = True

		textOutline = self.font.render("YOU LOSE!", False, (0,0,0))
		text = self.font.render("YOU LOSE!", False, (255, 0, 0))

		for i in range(-3, 4):
			for j in range(-3, 4):
				self.screen.blit(textOutline, (370 + i, 100 + j))

		self.screen.blit(text, (370,100))


	# if player reach the goal
	def _game_win(self, player):
		player.game_over = True
		player.win = True

		textOutline = self.font.render("YOU WIN!", False, (0, 0, 0))
		text = self.font.render("YOU WIN!", False, (0, 255, 0))

		for i in range(-3, 4):
			for j in range(-3, 4):
				self.screen.blit(textOutline, (370 + i, 100 + j))


		self.screen.blit(text, (370, 100))

	# checks if the game is over or not, and if win or lose
	def game_state(self, player, goal):
		if player.life <= 0 or player.rect.y >= HEIGHT:
			self._game_lose(player)
		elif player.rect.colliderect(goal.rect):
			self._game_win(player)
		else:
			None

	def show_life(self, player):
		life_size = 32
		img_path = "assets/life/health.png"
		life_image = pygame.image.load(img_path)
		life_image = pygame.transform.scale(life_image, (life_size, life_size))
		# life_rect = life_image.get_rect(topleft = pos)
		indent = 0
		for life in range(player.life):
			indent += life_size
			self.screen.blit(life_image, (indent, life_size))