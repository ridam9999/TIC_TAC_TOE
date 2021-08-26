import pygame
from pygame.locals import *

# initialize
pygame.init()
WIN_SIZE = (640,480)
white = (255, 255, 255)
black = (0, 0, 0)
main_clock = pygame.time.Clock()

window = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption('Tic Tac Toe')

font = pygame.font.Font('Roboto-Light.ttf', 50)
top_render = font.render('Tic Tac Toe', True, white)

board = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
#function to render the board
def draw_board():
    board = pygame.image.load('tic_tac_toe.png').convert()
    board.set_colorkey(black)
    window.blit(board,(0,0))




#main game loop
run = True
while run:
    for event in pygame.event.get():
        window.fill(black)
        window.blit(top_render,(180,15)) 
        if event.type == QUIT:
            sys.exit()
        
        draw_board()
        pygame.display.update()
        main_clock.tick(60)
    




