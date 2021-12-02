import pygame, sys, random
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
TEXTCOLOR = (0,0,0)
BACKGROUNDCOLOR = (255, 255, 255)
FPS = 20
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 20
BADDIEMINSPEED = 1
BADDIEMAXSPEED = 6
ADDNEWBADDIERATE = 4
PLAYERMOVERATE = 5 

def terminate():
	pygame.quit()
	sys.exit()


def wait_for_player_to_press_key():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			return

def player_has_hit_baddie(playerRect, baddies):
	for b in baddies:
		if playerRect.colliderect(b['rect']):
			return True
	return False

def draw_text(text, font, surface, x, y):
	textobj = font.render(text, 1, TEXTCOLOR)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y)
	surface.blit(textobj, textrect)


pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Dogger')
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 48)

gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background.mid')

playerImage = pygame.image.load('player.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('baddie.png')

windowSurface.fill(BACKGROUNDCOLOR)
draw_text('Dogger', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
draw_text('Press any key to start', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)

pygame.display.update()
wait_for_player_to_press_key()

topScore = 0

while True:
	baddies = []
	score = 0
	playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
	moveLeft = moveRight = moveUp = moveDown = False
	reverseCheat = slowCheat = False
	baddieAddCounter = 0
	pygame.mixer.music.play(-1, 0.0)

	while True:
		score += 1

		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()

			if event.type == KEYDOWN:
				if event.key == K_LEFT or event.key == K_a:
					moveRight = False
					moveLeft = True
				if event.key == K_RIGHT or event.key == K_d:
					moveLeft = False
					moveRight = True
				if event.key == K_UP or event.key == K_w:
					moveUp =True
					moveDown =False
				if event.key == K_DOWN or event.key == K_s:
					moveUp = False
					moveDown = True
				if event.key == K_z:
					reverseCheat = True
				if event.key == K_x:
					slowCheat = True

			if event.type == KEYUP:
				if event.key == K_z:
					reverseCheat = False
				if event.key == K_x:
					slowCheat = False
				if event.key == K_ESCAPE:
					terminate()
				if event.key == K_LEFT or event.key == K_a:
					moveLeft = False
				if event.key == K_RIGHT or event.key == K_d:
					moveRight = False
				if event.key == K_UP or event.key == K_w:
					moveUp =False
				if event.key == K_DOWN or event.key == K_s:
					moveDown = False
				if event.key == K_m:
					if musicPlaying:
						pygame.mixer.music.stop()
					else:
						pygame.mixer.music.paly(-1, 0.0)
					musicPlaying = not musicPlaying

			if event.type == MOUSEMOTION:
				playerRect.centerx = event.pos[0]
				playerRect.centery = event.pos[1]

		if not reverseCheat and not slowCheat:
			baddieAddCounter += 1
		if baddieAddCounter == ADDNEWBADDIERATE:
			baddieAddCounter = 0
			baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)
			newBaddie = {
							'rect':pygame.Rect(random.randint(0, WINDOWWIDTH - baddieSize),
								0 - baddieSize, baddieSize, baddieSize),
							'speed':random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
							'surface': pygame.transform.scale(baddieImage, (baddieSize, baddieSize))
							}

			baddies.append(newBaddie)

		if moveLeft and playerRect.left > 0:
			playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
		if moveRight and playerRect.right < WINDOWWIDTH:
			playerRect.move_ip(PLAYERMOVERATE, 0)
		if moveUp and playerRect.top > 0:
			playerRect.move_ip(0, -1 * PLAYERMOVERATE)
		if moveDown and playerRect.bottom > WINDOWHEIGHT:
			playerRect.move_ip(0, PLAYERMOVERATE)

		for b in baddies:
			if not reverseCheat and not slowCheat:
				b['rect'].move_ip(0, b['speed'])
			elif reverseCheat:
				b['rect'].move_ip(0, -5)
			elif slowCheat:
				b['rect'].move_ip(0, 1)

		for b in baddies[:]:
			if b['rect'].top > WINDOWHEIGHT:
				baddies.remove(b)

			windowSurface.fill(BACKGROUNDCOLOR)

			draw_text('Score: %s' %(score), font, windowSurface, 10, 0)
			draw_text('Top Score: %s' %(topScore), font, windowSurface, 10, 40)

			windowSurface.blit(playerImage, playerRect)

		for b in baddies:
			windowSurface.blit(b['surface'], b['rect'])

		pygame.display.update()

		if player_has_hit_baddie(playerRect, baddies):
			if score > topScore:
				topScore = score
			break

		mainClock.tick(FPS)

	pygame.mixer.music.stop()
	gameOverSound.play()

	draw_text('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
	draw_text('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3)+ 50)
	pygame.display.update()
	wait_for_player_to_press_key()

	gameOverSound.stop()















