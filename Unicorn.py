import pygame

class Unicorn:
	def __init__(self, posx, posy, zoom):

		self.flip_x = False
		self.rotate = 0
		self.zoom = zoom

		self.image = pygame.transform.scale(pygame.transform.rotate(pygame.transform.flip(pygame.image.load("unicorn/0.png"), self.flip_x, False), self.rotate), ((42 / 3) * self.zoom, (37 / 3) * self.zoom)).convert_alpha()
		self.rect = self.image.get_rect(x=posx, y=posy)




	def update(self, dt):

		self.rotate += 1
		self.rect.y += 1



		self.image = pygame.transform.scale(pygame.transform.rotate(pygame.transform.flip(pygame.image.load("unicorn/0.png"), self.flip_x, False), self.rotate), ((42 / 3) * self.zoom, (37 / 3) * self.zoom)).convert_alpha()
