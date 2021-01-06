import pygame
import time
import random

import Soduko_Board_Algorithim
from Soduko_Board_Algorithim import Algorithm

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 830
GRID_SIZE = SCREEN_WIDTH // 20
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



class GUI:
    def __init__(self):
        self.lives = 3
        self.hints = 3
        self.score = 0



    def draw_board(self):
        SCREEN.fill((255, 255, 255))
        count = 1
        for i in range(1, 9):
            if i % 3 == 0:
                pygame.draw.line(SCREEN, BLACK, (count * 200, 0), (count * 200, 630), 15)
                pygame.draw.line(SCREEN, BLACK, (0, count * 200), (630, count * 200), 15)
                count += 1
            else:
                pygame.draw.line(SCREEN, BLACK, (i * 200 / 3, 0), (i * 200 / 3, 630), 5)
                pygame.draw.line(SCREEN, BLACK, (0, i * 200 / 3), (630, i * 200 / 3), 5)

        pygame.draw.line(SCREEN, BLACK, (0, 630), (SCREEN_WIDTH, 630), 15)  # CHANGE THE STARTING Y AND ENDING Y -
        pygame.draw.line(SCREEN, BLACK, (0, 0), (SCREEN_WIDTH, 0), 15)  # CHANGE THE STARTING Y AND ENDING Y -
        pygame.draw.line(SCREEN, BLACK, (0, 0), (0, SCREEN_HEIGHT - 200), 15)  # CHANGE THE STARTING Y AND ENDING Y -
        pygame.draw.line(SCREEN, BLACK, (SCREEN_WIDTH, 0), (SCREEN_WIDTH, SCREEN_HEIGHT - 200), 15)  # CHANGE THE STARTING Y AND ENDING Y -

    def set_message(self, msg, color, surface, x_coord, y_coord, board):
        if board.current_board[x_coord][y_coord]:
            font = pygame.font.Font('freesansbold.ttf', 18)
            screen_txt = font.render(msg, True, color)
            surface.blit(screen_txt, [x_coord, y_coord])
    def draw_entire_grid(self, board):

        font = pygame.font.Font('freesansbold.ttf', 65)
        for i in range(9):
            count = 20
            for j in range(9):
                if board.current_board[i][j]!=-1:
                    screen_txt = font.render(str(board.current_board[i][j]), True, BLACK)
                    if i == 0:
                        SCREEN.blit(screen_txt, [(count), 8])
                    elif i == 1:
                        SCREEN.blit(screen_txt, [(count), 71])
                    elif i == 2:
                        SCREEN.blit(screen_txt, [(count), 134])
                    elif i == 3:
                        SCREEN.blit(screen_txt, [(count), 205])
                    elif i == 4:
                        SCREEN.blit(screen_txt, [(count), 270])
                    elif i == 5:
                        SCREEN.blit(screen_txt, [(count), 335])
                    elif i == 6:
                        SCREEN.blit(screen_txt, [(count), 405])
                    elif i == 7:
                        SCREEN.blit(screen_txt, [(count), 470])
                    elif i == 8:
                        SCREEN.blit(screen_txt, [(count), 540])
                count+=66

def main():
    my_board = [

        [7, 8, -1, 4, -1, -1, 1, 2, -1],
        [6, -1, -1, -1, 7, 5, -1, -1, 9],
        [-1, -1, -1, 6, -1, 1, -1, 7, 8],
        [-1, -1, 7, -1, 4, -1, 2, 6, -1],
        [-1, -1, 1, -1, 5, -1, 9, 3, -1],
        [9, -1, 4, -1, 6, -1, -1, -1, 5],
        [-1, 7, -1, 3, -1, -1, -1, 1, 2],
        [1, 2, -1, -1, -1, 7, 4, -1, -1],
        [-1, 4, 9, 2, -1, 6, -1, -1, 7]

    ]
    pygame.init()
    clock = pygame.time.Clock()
    user_interface = GUI()
    running = True
    user_interface.draw_board()
    board = Algorithm(my_board)
    while running:
        clock.tick(8)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        user_interface.draw_entire_grid(board)
        pygame.display.update()


main()
