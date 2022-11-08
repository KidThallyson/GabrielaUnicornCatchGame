
import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, zoom, uni_list, group):
		super().__init__(group)

		self.jump_length = 13
		self.jump_gravity = 3
		self.jump_cooldown = 100

		self.uni_list = uni_list

		self.flip_x = False
		self.zoom = zoom
		
		self.collided = False

		self.frame = 0

		self.timer = self.jump_length
		self.timer2 = self.jump_cooldown 
		
		self.animate()
		self.image = self.animatione[self.frame]  
		self.rect = self.image.get_rect(center=(500, 500))


		self.jump = False

		self.position = pygame.math.Vector2(pos[0], pos[1])
		self.direction = pygame.math.Vector2(0, 0)
		self.speed = 400

		self.floor_rect = pygame.Rect(0, 710, 1308, 100)


		self.right_btn = pygame.transform.scale_by(pygame.image.load("buttons/right.png"), 5)
		self.right_rect = self.right_btn.get_rect()
		self.left_btn = pygame.transform.scale_by(pygame.image.load("buttons/left.png"), 5)
		self.left_btn = self.left_btn.get_rect()


		self.stats = {
		
		"health": 3,
		"unicorns": 0

		}
	def animate(self):
		self.animatione = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(f"anim/{frame}.png"), (20 * self.zoom, 27 * self.zoom)), self.flip_x, False).convert_alpha() for frame in range(6)]


	def animation(self):


		for unicorn in self.uni_list:

			if pygame.sprite.collide_mask(unicorn, self):
				self.collided = True

				self.uni_list.remove(unicorn)
				self.stats["unicorns"] += 1


			if unicorn.rect.y > 60 * self.zoom:

				self.uni_list.remove(unicorn)
				self.stats["health"] -= 1


	def movement(self, dt):
		self.position += self.direction * self.speed * dt
		self.rect.x = round(self.position.x)
		self.rect.y = round(self.position.y)

	def input(self, fingers):

		kb = pygame.key.get_pressed()

		self.direction.x = 0
		
		for finger, pos in fingers.items():
			if self.right_rect.collidepoint(pos):
				pass


		if kb[pygame.K_d]:
			self.flip_x = False
			if self.rect.colliderect(self.floor_rect):

				self.direction.x = 1
			else:
				self.direction.x = 3
		if kb[pygame.K_a]:
			self.flip_x = True
			if self.rect.colliderect(self.floor_rect):
				self.direction.x = -1
			else:
				self.direction.x = -3
		if kb[pygame.K_w]:
			if self.rect.colliderect(self.floor_rect):
				if self.timer2 == self.jump_cooldown:
					self.timer = 0
				

		if self.timer < self.jump_length:
			self.timer2 = 0
			self.jump = True
		else:
			self.jump = False

		if self.jump == True:
			if self.rect.colliderect(self.floor_rect):
				self.direction.y = -self.jump_gravity
		else:
			self.direction.y = 0

		if self.rect.colliderect(self.floor_rect):
			if self.jump == False:
				self.direction.y = 0
		else:
			if self.jump == False:
				self.direction.y = self.jump_gravity



	def update(self, dt, fingers):


		self.animation()
		self.movement(dt)
		self.input(fingers)
		self.animate()
		if self.collided == True:
			self.frame += 1 * dt * 10
		if self.frame > 5:
			self.frame = 0
			self.collided = False

		if self.timer < self.jump_length:
			self.timer += 1
		if self.timer2 < self.jump_cooldown:
			self.timer2 += 1
		self.image = self.animatione[int(self.frame)]  