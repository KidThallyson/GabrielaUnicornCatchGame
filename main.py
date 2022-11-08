import pygame, sys
from settings import *
from Player import *
from Unicorn import *
import random

class SpriteGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()

	def draw(self, screen):
		for sprite in self.sprites():
			screen.blit(sprite.image, sprite.rect)



pygame.init()
screen = pygame.display.set_mode((109 * display["zoom"], 60 * display["zoom"]))
clock = pygame.time.Clock()
bg_img = pygame.transform.scale(pygame.image.load("map/0.png").convert_alpha(), (109 * display["zoom"], 60 * display["zoom"]))
bg_img_rect = bg_img.get_rect()
music = pygame.mixer.Sound("music.mp3")


def game():

	loss, victory = pygame.mixer.Sound("loss.mp3"), pygame.mixer.Sound("yay.mp3")  
	lost = False

	

	timer = 700


	index = 0

	music.play(-1)

	sprite_group = SpriteGroup()

	play_again = pygame.transform.scale(pygame.image.load(f"play_btn/{index}.png"), (400, 200))

	unicorns = []

	gabi = Player((200, 200), display["zoom"], unicorns, sprite_group)

	font = pygame.font.SysFont("Arial", 40, bold=True, italic=True)
	font2 = pygame.font.SysFont("Arial", 200, bold=True, italic=True)

	pygame.mixer.set_num_channels(2)
	fingers = {}
	while True:
		
		music.play(-1)
			
		mx, my = pygame.mouse.get_pos()

		screen.blit(bg_img, bg_img_rect)

		for event in pygame.event.get():
			if event.type == 256:
				pygame.quit()
				sys.exit()
			if event.type == pygame.FINGERDOWN:
				x = event.x * window.get_height()
				y = event.y * window.get_width()
				fingers[event.finger_id] = x, y
			if event.type == pygame.FINGERUP:
				fingers.pop(event.finger_id, None)

		dt = clock.tick(120) / 1000



		for unicorn in unicorns:
			screen.blit(unicorn.image, unicorn.rect)
			unicorn.update(dt)

		screen.blit(pygame.image.load("unicorn/0.png").convert_alpha(), (0, 0, 1, 1))
		screen.blit(pygame.transform.scale(pygame.image.load("heart.png"), (40, 40)).convert_alpha(), (1100, 0, 1, 1))

		screen.blit(font.render(f"UNICORNS: {gabi.stats['unicorns']}", True, (0, 0, 0)), (52, 4, 1, 1))
		screen.blit(font.render(f"UNICORNS: {gabi.stats['unicorns']}", True, (255, 255, 255)), (54, 2, 1, 1))

		screen.blit(font.render(f"LIVES: {gabi.stats['health']}", True, (0, 0, 0)), (1200 - 52, 4, 1, 1))
		screen.blit(font.render(f"LIVES: {gabi.stats['health']}", True, (255, 255, 255)), (1200 - 54, 2, 1, 1))





		timer2 = pygame.Surface((gabi.timer2, 10))

		timer2.fill((0, 50, 200))
		screen.blit(timer2, pygame.Rect(gabi.rect.x + 65, gabi.rect.y, 1, 1))

		sprite_group.draw(screen)
		sprite_group.update(dt, fingers)


		if gabi.stats['health'] == 0 or gabi.stats['health'] <= 0:
			screen.blit(font2.render("YOU LOST :(", True, (0, 0, 0)), (222, 202, 1, 1))
			screen.blit(font2.render("YOU LOST :(", True, (255, 0, 0)), (220, 200, 1, 1))

			timer = 0

			if timer < 700:
				loss.play()
			else:
				loss.stop()

			music.stop()

			unicorns = []
			mouse_rect = pygame.Rect(mx, my, 10, 10)
			kb = pygame.mouse.get_pressed()

			
			screen.blit(play_again, (420, 500, 1, 1))

			index = 0
			if play_again.get_rect(x=420, y=500).colliderect(mouse_rect):

				index = 1
				if kb == (1, 0, 0):
					index = 2
					loss.stop()
					game()

		if len(unicorns) < 10:
			if gabi.stats['unicorns'] <= 50:
				unicorns.append(Unicorn(random.randrange(0, 100 * display["zoom"]), random.randrange(0, 60), display["zoom"]))
			else:
				screen.blit(font2.render("YOU WON :D", True, (0, 0, 0)), (222, 202, 1, 1))
				screen.blit(font2.render("YOU WON :D", True, (0, 255, 0)), (220, 200, 1, 1))
				
				victory.play()
				music.stop()
				unicorns = []

				mouse_rect = pygame.Rect(mx, my, 10, 10)
				kb = pygame.mouse.get_pressed()

				
				screen.blit(play_again, (420, 500, 1, 1))

				index = 0
				if play_again.get_rect(x=420, y=500).colliderect(mouse_rect):

					index = 1
					if kb == (1, 0, 0):
						victory.stop()
						index = 2
						game()

		play_again = pygame.transform.scale(pygame.image.load(f"play_btn/{index}.png"), (400, 200))



		pygame.display.update()

		if timer < 700:
			timer += 1


		print(timer)



def menu():

	index = 0
	play_btn = pygame.transform.scale(pygame.image.load(f"play_btn/{index}.png"), (400, 200))


	image = pygame.transform.scale(pygame.transform.rotate(pygame.transform.flip(pygame.image.load(f"unicorn/0.png"), False, False), 0), ((42 / 3) * display["zoom"], (37 / 3) * display["zoom"])).convert_alpha()

	gabi2 = pygame.mixer.Sound("untitled.mp3")
	gabi2.play()
	while True:
		mx, my = pygame.mouse.get_pos()
		screen.fill((126, 182, 28))
		for event in pygame.event.get():
			if event.type == 256:
				pygame.quit()
				sys.exit()

		mouse_rect = pygame.Rect(mx, my, 10, 10)
		kb = pygame.mouse.get_pressed()
		index = 0



		if play_btn.get_rect(x=425, y=200).colliderect(mouse_rect):
			index = 1
			if kb == (1, 0, 0):

				index = 2
				break


		play_btn = pygame.transform.scale(pygame.image.load(f"play_btn/{index}.png"), (400, 200))



		screen.blit(image, (200, 200, 1, 1))
		screen.blit(pygame.transform.flip(image, True, False), (890, 200, 1, 1))
		screen.blit(play_btn, (425, 200, 1, 1))




		pygame.display.update()

	return game()



menu()