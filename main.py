import pygame, sys, random
from pygame.locals import *

#Initialize
pygame.init()
WIN_SIZE = (640,480)
main_clock = pygame.time.Clock()
window = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption('Tic Tac Toe')
cursor = pygame.Rect(100, 100, 100, 100)

#colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (77, 77, 77)

#Font
font = pygame.font.Font('Roboto-Light.ttf', 50)
top_render = font.render('Tic Tac Toe', True, white)

#Images
X = pygame.image.load('X.png').convert()
X.set_colorkey(black)

O= pygame.image.load('O.png').convert()
O.set_colorkey(black)

board_images = [] #Board images position List
particles = [] #particles effect

#Function to render the board
def draw_board():
    board = pygame.image.load('tic_tac_toe.png').convert()
    board.set_colorkey(black)
    window.blit(board,(0,0))

def draw_cursor():
    cursor_color = (200, 100, 150)
    pygame.draw.rect(window, cursor_color, cursor, 100, 4)

def move_cursor():
    pass

def particle_effect(x, y):
     particles.append([[x, y], [random.randint(-20,20)/10*-1, random.randint(-20,20)/10*-1],random.randint(50, 70)])

     for particle in particles:
         particle[0][0] += particle[1][0]
         particle[0][1] += particle[1][1]
         particle[2] -= 0.2
         pygame.draw.circle(window, gray, [int(particle[0][0]), int(particle[0][1])],int(particle[2]))
     if particle[2] <= 0:
         particles.remove(particle)


#Main game loop
while True:
    window.fill(black)
    particle_effect(0, 0)
    particle_effect(WIN_SIZE[0], WIN_SIZE[1])
    window.blit(top_render,(185,15)) 
    draw_board()
    draw_cursor()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
        
    pygame.display.update()
    main_clock.tick(60)
    




