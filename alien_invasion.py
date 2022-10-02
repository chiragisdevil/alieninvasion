import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
	'''Overall class to manage the game assets and behaviour'''
	def __init__(self):
		'''Initialize the pygame and also call the set_mode for screensize and set_caption for setting the screen caption'''
		pygame.init()
		self.settings = Settings()
		# self.screen = pygame.display.set_mode((self.settings.screen_height,self.settings.screen_width))
		self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		self.settings.screen_height = self.screen.get_rect().height
		self.settings.screen_width = self.screen.get_rect().width
		pygame.display.set_caption("Alien Invasion!!!")
		self.bg_color = self.settings.screen_background
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()

	def _fire_bullet(self):
		'''Create a new Bullet and add it to the bullet group'''
		new_bullet = Bullet(self)
		self.bullets.add(new_bullet)

	def _check_keydown_events(self,event):
		'''Respond to Keydown Events'''
		if event.key == pygame.K_RIGHT:
			self.ship.movement_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.movement_left = True
		elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self,event):
		'''Respond to Keyup events'''
		if event.key == pygame.K_RIGHT:
			self.ship.movement_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.movement_left = False

	def _check_events(self):
		'''Checks for events from keyboard and mouse and exits if a quit event (x) is received'''
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					self._check_keydown_events(event)
				elif event.type == pygame.KEYUP:
					self._check_keyup_events(event)

	def _update_screen(self):
		'''Updates the screen to fill background color and then draw the ship image'''
		self.screen.fill(self.bg_color)
		self.ship.blitme()

		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		# Make the most recently drawn screen visible
		pygame.display.flip()

	def run_game(self):
		'''Start the main loop of the game'''
		while True:
			# Watch for keyboard and mouse events
			self._check_events()
			self.ship.update_position()
			self.bullets.update()
			self._update_screen()

if __name__ == "__main__":
	ai = AlienInvasion()
	ai.run_game()

