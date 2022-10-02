import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	'''This is the bullet class for all the bullets fired from the ship. 
	This is inherited fom Sprite class allowing us to create a group'''
	def __init__(self,game):
		super().__init__()
		self.screen = game.screen
		self.screen_rect = game.screen.get_rect()
		self.settings = game.settings
		self.color = self.settings.bullet_color

		# Create a Bullet 
		self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height) 
		self.rect.midtop = game.ship.rect.midtop

		# Store the vertical position of the bullet so we can adjust it
		self.y = float(self.rect.y)

	def move_bullets(self):
		'''Move the bullets up the screen'''
		# Update the decimal point of the bullet'''
		self.y -= self.settings.bullet_speed

		# Update the rect position
		self.rect.y = self.y

	def draw_bullet(self):
		'''Draw the bullet in the correct position'''
		pygame.draw.rect(self.screen,self.color,self.rect)



