import pygame
from settings import Settings
class Ship:
	'''A class to manage the ship'''
	def __init__(self,game):
		'''Initialize the Ship and set the starting position'''
		self.screen = game.screen
		self.screen_rect = game.screen.get_rect()

		self.movement_right = False
		self.movement_left = False
		self.settings = Settings()

		# Load the ship image and get the rect from the ship image
		self.image = pygame.image.load("images/ship.bmp")
		self.rect = self.image.get_rect()

		# Set the rect position to the centre of the screen
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		'''Draw the ship in the current location'''
		self.screen.blit(self.image,self.rect)

	def update_position(self):
		''' Move the ship to the right by speed defined'''
		if self.movement_right == True and self.rect.right <= self.screen_rect.right:
			self.rect.x += self.settings.speed
		elif self.movement_left == True and self.rect.left >= self.screen_rect.left:
			self.rect.x -= self.settings.speed


