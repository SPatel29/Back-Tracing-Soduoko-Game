import pygame
import time
from Soduko_Board_Algorithim import Algorithm

pygame.init()

font = pygame.font.Font(None, 54)
SCREEN_WIDTH = 660
SCREEN_HEIGHT = 700
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

ACTIVE_COLOR = (173, 216, 230)
UN_ACTIVE_COLOR = WHITE

def neturalize_row_col(row, col):
    if row % 3 != 0:
        if (row - 1) % 3 == 0:
            row -= 1
        elif (row - 2) % 3 == 0:
            row -= 2
    if col % 3 != 0:
        if (col - 1) % 3 == 0:
            col -= 1
        elif (col - 2) % 3 == 0:
            col -= 2
    return row, col

def reformat_time(seconds):
    if seconds < 60:
        return str(seconds) + ' seconds'
    elif 60 <= seconds < 3600:
        minute_num = seconds // 60
        seconds_num = seconds % 60
        if seconds_num < 10:
            return str(minute_num) + ":0" + str(seconds_num)
        else:
            return str(minute_num) + ":" + str(seconds_num)


class Tiles:
    def __init__(self, value, row, col, x, y, width, height, font_color, active=False):
        self.value = value
        self.active = active
        self.y = y
        self.x = x
        self.tile = pygame.Rect([x, y, width, height])
        self.row = row
        self.col = col
        self.font_color = font_color

    def draw_rectangle(self,
                       value2):  # ADDED THE IF STATEMENT CLAUSE, YOU CAN DELETE IT AND REMOVE THE ElSE AND KEEP THE REST TO MAKE IT WORK
        if self.value == value2:
            pygame.draw.rect(SCREEN, GREEN, self.tile)
        else:
            if not self.active:
                pygame.draw.rect(SCREEN, UN_ACTIVE_COLOR, self.get_tile())
            else:
                pygame.draw.rect(SCREEN, ACTIVE_COLOR, self.get_tile())

    def get_tile(self):
        return self.tile

    def get_value(self):
        return self.value

    def get_font_color(self):
        return self.font_color

    def set_font_color(self, new_color):
        self.font_color = new_color

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_value(self, new_value):
        self.value = new_value

    def get_active(self):
        return self.active

    def set_active(self, status):
        if status:
            self.active = True
        else:
            self.active = False

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col


def set_message(msg, color, surface, x_coord, y_coord):
    font = pygame.font.Font('freesansbold.ttf', 28)
    screen_txt = font.render(msg, True, color)
    surface.blit(screen_txt, [x_coord, y_coord])


def draw_vertical_lines():
    start_x_value = 81
    start_y_value = 65
    end_x_value = 81
    end_y_value = 658
    for i in range(9):
        for j in range(9):
            thickness = 4
            if j == 2:
                start_x_value = 212
                end_x_value = 212
                thickness = 10
            if j == 5:
                start_x_value = 410
                end_x_value = 410
                thickness = 10
            if j != 8:
                pygame.draw.line(SCREEN, BLACK, (start_x_value, start_y_value), (end_x_value, end_y_value), thickness)
            if j == 8:
                thickness = 10
                pygame.draw.line(SCREEN, BLACK, (start_x_value, start_y_value), (end_x_value, end_y_value), thickness)
            if j == 2 or j == 5:
                start_x_value += 3
                end_x_value += 3
            start_x_value += 65
            end_x_value += 65


def draw_horizontal_lines():
    start_y_value = 62
    end_y_value = 62
    for i in range(9):
        thickness = 4
        start_x_value = 20
        end_x_value = 606
        if i == 2:
            start_y_value = 260
            end_y_value = 260
            thickness = 10
            pygame.draw.line(SCREEN, BLACK, (start_x_value, start_y_value), (end_x_value, end_y_value), thickness)
            start_y_value += 4
            end_y_value += 4
        elif i == 5:
            start_y_value = 462
            end_y_value = 462
            thickness = 10
            pygame.draw.line(SCREEN, BLACK, (start_x_value, start_y_value), (end_x_value, end_y_value), thickness)
            start_y_value += 4
            end_y_value += 4
        else:
            start_y_value += 65
            end_y_value += 65
            if i != 8:
                pygame.draw.line(SCREEN, BLACK, (start_x_value, start_y_value), (end_x_value, end_y_value), thickness)
            else:
                thickness = 10
                end_x_value += 7
                pygame.draw.line(SCREEN, BLACK, (start_x_value, start_y_value), (end_x_value, end_y_value), thickness)
    pygame.draw.line(SCREEN, BLACK, (20, 65), (613, 65), 10)
    pygame.draw.line(SCREEN, BLACK, (20, 65), (613, 65), 10)
    pygame.draw.line(SCREEN, BLACK, (20, 61), (20, 666), 10)


def defeat_screen():
    SCREEN.fill(WHITE)
    set_message("YOU LOSE!", RED, SCREEN, 300, 300)
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    quit()

def draw_lives(hearts):
    x, y = 580, 668
    for i in hearts:
        SCREEN.blit(i, [x, y])
        x -= 50
def main():
    board = [

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
    hearts, my_lst, y_axis, x_axis = [], [], 65, 20
    for i in range(9):
        if i == 3:
            y_axis += 7
        if i == 6:
            y_axis += 7
        for j in range(9):
            my_lst.append(Tiles(board[i][j], i, j, x_axis, y_axis, 60, 60, GREY))
            if j == 2:
                x_axis += 3
            if j == 5:
                x_axis += 3
            x_axis += 65
        y_axis += 65
        x_axis = 20
    algorithm = Algorithm(board)
    algorithm.set_finished_board()
    running = True
    pygame.init()
    clock = pygame.time.Clock()
    for i in range(3):
        hearts.append(pygame.image.load('heart pixel art 32x32.png'))
    pygame.time.get_ticks()
    initial_time = time.time()
    current_time = 0
    check_one = None
    check_work = None
    solve_one = None
    solve_grid = None
    play_again = None
    while running:
        clock.tick(60)
        if hearts and algorithm.find_next_tile(algorithm.get_initial_board()):
            current_time = round(time.time() - initial_time)
        SCREEN.fill(WHITE)
        if hearts and algorithm.find_next_tile(algorithm.get_initial_board()):
            check_one = pygame.draw.rect(SCREEN, BLACK, [10, 12, 100, 30])
            check_work = pygame.draw.rect(SCREEN, BLACK, [445, 12, 151, 30])
            solve_one = pygame.draw.rect(SCREEN, BLACK, [120, 12, 150, 30])
            solve_grid = pygame.draw.rect(SCREEN, BLACK, [280, 12, 156, 30])
            set_message("Check ", WHITE, SCREEN, 15, 15)
            set_message("Check ALL", WHITE, SCREEN, 445, 15)
            set_message("Solve TILE", WHITE, SCREEN, 120, 15)
            set_message("Solve GRID", WHITE, SCREEN, 280, 15)
        elif hearts and not algorithm.find_next_tile(algorithm.get_initial_board()):
            play_again = pygame.draw.rect(SCREEN, BLACK, [10, 12, 165, 30])
            set_message("Play again?", WHITE, SCREEN, 10, 12)
            set_message("You win!", RED, SCREEN, 270, 12)
        else:
            play_again = pygame.draw.rect(SCREEN, BLACK, [10, 12, 165, 30])
            set_message("Play again?", WHITE, SCREEN, 10,12)
            set_message("You lose!", RED, SCREEN, 270,12)

        pygame.draw.rect(SCREEN, WHITE, [17, 675, 250, 30])
        for i in range(len(my_lst)):
            my_lst[i].draw_rectangle(algorithm.get_initial_board())
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again and pygame.Rect.collidepoint(play_again, pygame.mouse.get_pos()):
                    main()
                #print(pygame.mouse.get_pos())
                if pygame.Rect.collidepoint(check_one, pygame.mouse.get_pos()):
                    count = 0
                    for i in range(9):
                        for j in range(9):
                            if my_lst[count].get_active():
                                if my_lst[count].get_value() == algorithm.get_finished_board()[i][j]:
                                    algorithm.get_initial_board()[i][j] = algorithm.get_finished_board()[i][j]
                                else:
                                    if hearts:
                                        hearts.pop()
                            count += 1
                elif pygame.Rect.collidepoint(check_work, pygame.mouse.get_pos()):
                    count = 0
                    if algorithm.get_current_board() == algorithm.get_finished_board():
                        for i in range(9):
                            for j in range(9):
                                my_lst[count].set_font_color(BLACK)
                                algorithm.get_initial_board()[i][j] = algorithm.get_finished_board()[i][j]
                                count += 1
                    else:
                        for i in range(9):
                            for j in range(9):
                                if my_lst[count].get_value() == algorithm.get_finished_board()[i][j]:
                                    my_lst[count].set_font_color(BLACK)
                                    algorithm.get_initial_board()[i][j] = algorithm.get_finished_board()[i][j]
                                else:
                                    if hearts:
                                        hearts.pop()
                                    my_lst[count].set_font_color(GREY)
                                count += 1
                elif pygame.Rect.collidepoint(solve_one, pygame.mouse.get_pos()):
                    count = 0
                    for i in range(9):
                        for j in range(9):
                            if my_lst[count].get_active():
                                my_lst[count].set_value(algorithm.get_finished_board()[i][j])
                                algorithm.get_initial_board()[i][j] = algorithm.get_finished_board()[i][j]
                            count += 1
                elif pygame.Rect.collidepoint(solve_grid, pygame.mouse.get_pos()):
                    count = 0
                    row = 0
                    col = 0
                    for i in range(81):
                        if my_lst[i].get_active():
                            count = my_lst[i].get_row()
                            row, col = neturalize_row_col(my_lst[i].get_row(), my_lst[i].get_col())
                    for i in range(row, row + 3):
                        for j in range(col, col + 3):
                            algorithm.get_initial_board()[i][j] = algorithm.get_finished_board()[i][j]
                            count += 1
                        count += 9
                else:
                    for i in range(len(my_lst)):
                        if pygame.Rect.collidepoint(my_lst[i].get_tile(), pygame.mouse.get_pos()):
                            my_lst[i].set_active(True)
                        else:
                            my_lst[i].set_active(False)
            if event.type == pygame.KEYDOWN:
                for i in range(len(my_lst)):
                    if my_lst[i].get_active():
                        if event.key == pygame.K_1:
                            my_lst[i].set_value(1)
                        if event.key == pygame.K_2:
                            my_lst[i].set_value(2)
                        if event.key == pygame.K_3:
                            my_lst[i].set_value(3)
                        if event.key == pygame.K_4:
                            my_lst[i].set_value(4)
                        if event.key == pygame.K_5:
                            my_lst[i].set_value(5)
                        if event.key == pygame.K_6:
                            my_lst[i].set_value(6)
                        if event.key == pygame.K_7:
                            my_lst[i].set_value(7)
                        if event.key == pygame.K_8:
                            my_lst[i].set_value(8)
                        if event.key == pygame.K_9:
                            my_lst[i].set_value(9)
        count = 0
        for i in range(len(algorithm.get_current_board())):
            for j in range(len(algorithm.get_current_board())):
                if my_lst[count].get_row() == i and my_lst[count].get_col() == j:
                    if algorithm.get_initial_board()[i][j] == -1:
                        if my_lst[count].get_value() != -1:
                            set_message(str(my_lst[count].get_value()), GREY, SCREEN, my_lst[count].get_x() + 20,
                                        my_lst[count].get_y() + 15)
                    else:
                        set_message(str(algorithm.get_finished_board()[i][j]), BLACK, SCREEN,
                                    my_lst[count].get_x() + 20,
                                    my_lst[count].get_y() + 15)
                count += 1
        draw_lives(hearts)

        draw_vertical_lines(), draw_horizontal_lines()
        set_message(reformat_time(current_time), RED, SCREEN, 17, 675)
        pygame.display.update()


main()
