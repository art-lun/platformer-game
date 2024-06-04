import pygame

# scrolls the objects in game according to player movement.
class grass(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		super().__init__()
		img_path = 'assets/terrain/grass.png'
		self.image = pygame.image.load(img_path)
		self.image = pygame.transform.scale(self.image, (size, size))
		self.rect = self.image.get_rect(topleft = pos)

	def update(self, x_shift):
		self.rect.x += x_shift
class dirt(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		super().__init__()
		img_path = 'assets/terrain/dirt.png'
		self.image = pygame.image.load(img_path)
		self.image = pygame.transform.scale(self.image, (size, size))
		self.rect = self.image.get_rect(topleft=pos)

	# update object position due to world scroll
	def update(self, x_shift):
		self.rect.x += x_shift