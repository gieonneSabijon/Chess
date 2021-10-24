
import pygame
from piece import Pawn, King

WINDOW = pygame.display.set_mode((900,500))
pygame.display.set_caption("Chess")

def setup():
    
    global pawns
    global kings
    kings = [King(4,0,1), King(4,7,0)]
    pawns = []
    for pawn in range(16):
        if pawn < 8:
            pawns.append(Pawn(pawn, 1, 1))
        else:
            pawns.append(Pawn(pawn - 8, 6, 0))

    

def main():
    run = True  
    clock = pygame.time.Clock()
    setup()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        update()
        draw()

    pygame.quit()

def update():
    
    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)

def draw():
    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
    cursor_image = pygame.image.load('cursor.png')
    black_pawn_image = pygame.image.load('blackpawn.png')
    white_pawn_image = pygame.image.load('whitepawn.png')
    black_king_image = pygame.image.load('blackking.png')
    white_king_image = pygame.image.load('whiteking.png')
    board_image = pygame.image.load('board.png')

    WINDOW.fill((255,255,255))
    WINDOW.blit(board_image, (0,0))

    for pawn in pawns:
        if pawn.alignment == 1:
            WINDOW.blit(black_pawn_image, (pawn.x * 60, pawn.y * 60))
        else:
            WINDOW.blit(white_pawn_image, (pawn.x * 60, pawn.y * 60))

    for king in kings:
        if king.alignment == 1:
            WINDOW.blit(black_king_image, (king.x * 60, king.y * 60))
        else:
            WINDOW.blit(white_king_image, (king.x * 60, king.y * 60))

    WINDOW.blit(cursor_image, pygame.mouse.get_pos())
    pygame.display.update()

if __name__ == "__main__":
    main()