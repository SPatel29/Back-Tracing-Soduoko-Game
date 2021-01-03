import pygame
import time
import random

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

    def set_message(self, msg, color, surface, x_coord, y_coord, current_board, initial_board):
        if not initial_board[x_coord][y_coord]:
            font = pygame.font.Font('freesansbold.ttf', 18)
            screen_txt = font.render(msg, True, color)
            surface.blit(screen_txt, [x_coord, y_coord])

def main():
    pygame.init()
    clock = pygame.time.Clock()
    user_interface = GUI()
    running = True
    user_interface.draw_board()
    while running:
        clock.tick(8)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

        pygame.display.update()


main()
