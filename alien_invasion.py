import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
	'''Overall class to manage the game assets and behaviour'''
	def __init__(self):
		'''Initialize the pygame and also call the set_mode for screensize and set_caption for setting the screen caption'''
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_height,self.settings.screen_width))
		pygame.display.set_caption("Alien Invasion!!!")
		self.bg_color = self.settings.screen_background
		self.ship = Ship(self)

	def _check_events(self):
		'''Checks for events from keyboard and mouse and exits if a quit event (x) is received'''
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

	def _update_screen(self):
		'''Updates the screen to fill background color and then draw the ship image'''
		self.screen.fill(self.bg_color)
		self.ship.blitme()

		# Make the most recently drawn screen visible
		pygame.display.flip()

	def run_game(self):
		'''Start the main loop of the game'''
		while True:
			# Watch for keyboard and mouse events
			self._check_events()
			self._update_screen()

if __name__ == "__main__":
	ai = AlienInvasion()
	ai.run_game()

