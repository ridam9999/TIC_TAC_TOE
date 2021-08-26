import pygame, sys, random
from pygame.locals import *

#Initialize
pygame.init()
WIN_SIZE = (640,480)
white = (255, 255, 255)
black = (0, 0, 0)
main_clock = pygame.time.Clock()
window = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption('Tic Tac Toe')

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
    cursor_color = (155, 25, 20)
    cursor_width = 50
    pygame.draw.rect(window, cursor_color, (x, y, 5, 5), cursor_width)
  
def particle_effect(x, y):
     particles.append([[x, y], [random.randint(-20,20)/10*-1, random.randint(-20,20)/10*-1],random.randint(4,6)])

     for particle in particles:
         particle[0][0] += particle[1][0]
         particle[0][1] += particle[1][1]
         particle[2] -= 0.2
         pygame.draw.circle(window, white, [int(particle[0][0]), int(particle[0][1])],int(particle[2]))
     if particle[2] <= 0:
         particles.remove(particle)


#Main game loop
while True:
    for event in pygame.event.get():
        x, y = pygame.mouse.get_pos() #Mouse position
        window.fill(black)
        window.blit(top_render,(185,15)) 
        draw_board()
        draw_cursor()
        particle_effect(x, y)
        if event.type == QUIT:
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
        
        if event.type == pygame.MOUSEBUTTONUP :
                board_images.append([x, y])
                print(board_images)
        pygame.display.update()
        main_clock.tick(60)
    




