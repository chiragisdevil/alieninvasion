import pygame
class Ship:
	'''A class to manage the ship'''
	def __init__(self,game):
		'''Initialize the Ship and set the starting position'''
		self.screen = game.screen
		self.screen_rect = game.screen.get_rect()

		# Load the ship image and get the rect from the ship image
		self.image = pygame.image.load("images/ship.bmp")
		self.rect = self.image.get_rect()

		# Set the rect position to the centre of the screen
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		'''Draw the ship in the current location'''
		self.screen.blit(self.image,self.rect)



