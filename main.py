import pygame, sys, random
from pygame.locals import *

#Initialize
pygame.init()
WIN_SIZE = (640,480)
main_clock = pygame.time.Clock()
window = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption('Tic Tac Toe')
cursor_pos = [100, 85, 100, 100] #Cursor position
cursor = pygame.Rect(cursor_pos)
cube_pos = [0, 0, 100, 100] #Cube in the background
cube = pygame.Rect(cube_pos)

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
cubes = [] #flying cube background

#Function to render the board
def draw_board():
    board = pygame.image.load('tic_tac_toe.png').convert()
    board.set_colorkey(black)
    window.blit(board,(0,0))

def draw_cursor():
    cursor_color = (200, 100, 150)
    pygame.draw.rect(window, cursor_color, cursor, 100, 4)

def move_cursor(key):
    if key == K_w and cursor_pos[1] >= 100:
        cursor_pos[1] -= 140
        cursor.update(cursor_pos)

    if key == K_a and cursor_pos[0] > 100:
        cursor_pos[0] -= 160
        cursor.update(cursor_pos)

    if key == K_s and cursor_pos[1] <= 300:
        cursor_pos[1] += 140
        cursor.update(cursor_pos)

    if key == K_d and cursor_pos[0] <= 300:
        cursor_pos[0] += 160
        cursor.update(cursor_pos)

def particle_effect(x, y):
     particles.append([[x, y], [random.randint(-20,20)/10*-1, random.randint(-20,20)/10*-1],random.randint(50, 60)])

     for particle in particles:
         particle[0][0] += particle[1][0]
         particle[0][1] += particle[1][1]
         particle[2] -= 0.2
         pygame.draw.circle(window, gray, [int(particle[0][0]), int(particle[0][1])],int(particle[2]))
     if particle[2] <= 0:
         particles.remove(particle)

def background_animation(x, y):
    #[x,y,w,h] [x_vel, y_vel] [width]
    width = 50
    height = 50

    cubes.append([[x, y, width, height], [random.randint(-20,20)/10*-1, random.randint(-20,20)/10*-1],random.randint(50, 70)])
    
    for cube in cubes:
        cube[0][0] += cube[1][0]
        cube[0][1] += cube[1][1]
        cube[2] -= 0.2
        pygame.draw.rect(window, gray, [int(cube[0][0]),int(cube[0][1]),int(cube[0][2]),int(cube[0][3])], int(cube[2]))
        if cube[2] <=0:
            cubes.remove(cube)
 
#Main game loop
while True:
    window.fill(black)
    background_animation(0, WIN_SIZE[1] * 1.5)
    background_animation(WIN_SIZE[0], WIN_SIZE[1] * -0.5)
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
            move_cursor(event.key)        
    pygame.display.update()
    main_clock.tick(60)
    




