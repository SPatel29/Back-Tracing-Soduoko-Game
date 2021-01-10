from Soduko_Board_Algorithim import Algorithm
import pygame
from Soduko_Board_Algorithim import Algorithm

pygame.init()

SCREEN_WIDTH = 660
SCREEN_HEIGHT = 700
# GRID_SIZE = SCREEN_WIDTH // 20
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)

ACTIVE_COLOR = (173, 216, 230)
UN_ACTIVE_COLOR = WHITE


class Tiles:
    def __init__(self, value, row, col, x, y, width, height, active=False):
        self.value = value
        self.active = active
        self.y = y
        self.x = x
        self.tile = pygame.Rect([x, y, width, height])
        self.width = width
        self.height = height
        self.row = row
        self.col = col

    def draw_rectangle(self):
        if not self.active:
            pygame.draw.rect(SCREEN, UN_ACTIVE_COLOR, self.get_tile())
        else:
            pygame.draw.rect(SCREEN, ACTIVE_COLOR, self.get_tile())

    def get_tile(self):
        return self.tile

    def get_value(self):
        return self.value

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

    def get_width(self):
        return self.width

    def set_width(self, new_width):
        self.width = new_width

    def write_to_tile(self):
        pass


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
    my_lst = []
    y_axis = 65  # maybe make thin line 65 and thick line 68?
    x_axis = 20
    for i in range(9):
        if i == 3:
            y_axis += 7
        if i == 6:
            y_axis += 7
        for j in range(9):
            my_lst.append(Tiles(board[i][j], i, j, x_axis, y_axis, 60, 60))
            if j == 2:
                x_axis += 3
            if j == 5:
                x_axis += 3
            x_axis += 65
        y_axis += 65
        x_axis = 20

    algorithm = Algorithm(board)
    algorithm.set_finished_board()
    print(algorithm.get_finished_board())
    running = True
    pygame.init()
    clock = pygame.time.Clock()
    color = GREY
    while running:
        clock.tick(60)
        SCREEN.fill(WHITE)
        check_one = pygame.draw.rect(SCREEN, BLACK, [10,12,100,30])
        check_work = pygame.draw.rect(SCREEN, BLACK, [400,12,230,30])
        for i in range(len(my_lst)):
            my_lst[i].draw_rectangle()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect.collidepoint(check_one, pygame.mouse.get_pos()):
                    count = 0
                    for i in range(9):
                        for j in range(9):
                            if my_lst[count].get_active():
                                if algorithm.get_current_board()[i][j] == algorithm.get_finished_board()[i][j]:
                                    algorithm.get_initial_board()[i][j] = algorithm.get_finished_board()[i][j]
                            count+=1
                elif pygame.Rect.collidepoint(check_work, pygame.mouse.get_pos()):
                    if algorithm.find_next_tile(
                            algorithm.get_current_board()) and algorithm.get_finished_board() != algorithm.get_current_board():
                        print("NOT DONE")
                    else:
                        color = BLACK
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
                            # I CAN JUST SET THE TILE VALUE HERE REGARDLESS IF WRONG OR RIGHT
                            # IF IT IS RIGHT THEN MOVE ONTO THE IF STATEMENT WHERE I DO SET_TILE (NEXT LINE CODE)
                            if not algorithm.check_wrong(algorithm.get_current_board(), my_lst[i].get_row(),
                                                         my_lst[i].get_col(), 1):
                                algorithm.set_tile(algorithm.get_current_board(), my_lst[i].get_row(),
                                                   my_lst[i].get_col(), 1)
                        if event.key == pygame.K_2:
                            # I CAN JUST SET THE TILE VALUE HERE REGARDLESS IF WRONG OR RIGHT
                            # IF IT IS RIGHT THEN MOVE ONTO THE IF STATEMENT WHERE I DO SET_TILE (NEXT LINE CODE)
                            if not algorithm.check_wrong(algorithm.get_current_board(), my_lst[i].get_row(),
                                                         my_lst[i].get_col(), 2):
                                algorithm.set_tile(algorithm.get_current_board(), my_lst[i].get_row(),
                                                   my_lst[i].get_col(), 2)
                        if event.key == pygame.K_3:
                            # I CAN JUST SET THE TILE VALUE HERE REGARDLESS IF WRONG OR RIGHT
                            # IF IT IS RIGHT THEN MOVE ONTO THE IF STATEMENT WHERE I DO SET_TILE (NEXT LINE CODE)
                            if not algorithm.check_wrong(algorithm.get_current_board(), my_lst[i].get_row(),
                                                         my_lst[i].get_col(), 3):
                                algorithm.set_tile(algorithm.get_current_board(), my_lst[i].get_row(),
                                                   my_lst[i].get_col(), 3)
                        if event.key == pygame.K_4:
                            # I CAN JUST SET THE TILE VALUE HERE REGARDLESS IF WRONG OR RIGHT
                            # IF IT IS RIGHT THEN MOVE ONTO THE IF STATEMENT WHERE I DO SET_TILE (NEXT LINE CODE)
                            if not algorithm.check_wrong(algorithm.get_current_board(), my_lst[i].get_row(),
                                                         my_lst[i].get_col(), 4):
                                algorithm.set_tile(algorithm.get_current_board(), my_lst[i].get_row(),
                                                   my_lst[i].get_col(), 4)
                        if event.key == pygame.K_5:
                            # I CAN JUST SET THE TILE VALUE HERE REGARDLESS IF WRONG OR RIGHT
                            # IF IT IS RIGHT THEN MOVE ONTO THE IF STATEMENT WHERE I DO SET_TILE (NEXT LINE CODE)
                            if not algorithm.check_wrong(algorithm.get_current_board(), my_lst[i].get_row(),
                                                         my_lst[i].get_col(), 5):
                                algorithm.set_tile(algorithm.get_current_board(), my_lst[i].get_row(),
                                                   my_lst[i].get_col(), 5)
                        if event.key == pygame.K_6:
                            # I CAN JUST SET THE TILE VALUE HERE REGARDLESS IF WRONG OR RIGHT
                            # IF IT IS RIGHT THEN MOVE ONTO THE IF STATEMENT WHERE I DO SET_TILE (NEXT LINE CODE)
                            if not algorithm.check_wrong(algorithm.get_current_board(), my_lst[i].get_row(),
                                                         my_lst[i].get_col(), 6):
                                algorithm.set_tile(algorithm.get_current_board(), my_lst[i].get_row(),
                                                   my_lst[i].get_col(), 6)
                        if event.key == pygame.K_7:
                            # I CAN JUST SET THE TILE VALUE HERE REGARDLESS IF WRONG OR RIGHT
                            # IF IT IS RIGHT THEN MOVE ONTO THE IF STATEMENT WHERE I DO SET_TILE (NEXT LINE CODE)
                            if not algorithm.check_wrong(algorithm.get_current_board(), my_lst[i].get_row(),
                                                         my_lst[i].get_col(), 7):
                                algorithm.set_tile(algorithm.get_current_board(), my_lst[i].get_row(),
                                                   my_lst[i].get_col(), 7)
                        if event.key == pygame.K_8:
                            # I CAN JUST SET THE TILE VALUE HERE REGARDLESS IF WRONG OR RIGHT
                            # IF IT IS RIGHT THEN MOVE ONTO THE IF STATEMENT WHERE I DO SET_TILE (NEXT LINE CODE)
                            if not algorithm.check_wrong(algorithm.get_current_board(), my_lst[i].get_row(),
                                                         my_lst[i].get_col(), 8):
                                algorithm.set_tile(algorithm.get_current_board(), my_lst[i].get_row(),
                                                   my_lst[i].get_col(), 8)
                        if event.key == pygame.K_9:
                            #I CAN JUST SET THE TILE VALUE HERE REGARDLESS IF WRONG OR RIGHT
                            #IF IT IS RIGHT THEN MOVE ONTO THE IF STATEMENT WHERE I DO SET_TILE (NEXT LINE CODE)

                            if not algorithm.check_wrong(algorithm.get_current_board(), my_lst[i].get_row(),
                                                         my_lst[i].get_col(), 9):
                                algorithm.set_tile(algorithm.get_current_board(), my_lst[i].get_row(),
                                                   my_lst[i].get_col(), 9)
        count = 0

        for i in range(len(algorithm.get_current_board())):
            for j in range(len(algorithm.get_current_board())):
                if my_lst[count].get_row() == i and my_lst[count].get_col() == j and algorithm.get_current_board()[i][
                    j] != -1:
                    if algorithm.get_initial_board()[i][j] == -1:
                        set_message(str(algorithm.get_current_board()[i][j]), color, SCREEN, my_lst[count].get_x() + 20,
                                    my_lst[count].get_y() + 15)
                    else:
                        set_message(str(algorithm.get_current_board()[i][j]), BLACK, SCREEN, my_lst[count].get_x() + 20,
                                    my_lst[count].get_y() + 15)
                count += 1
        set_message("Check ONE", WHITE, SCREEN, 15, 12)
        set_message("Check ALL work", WHITE, SCREEN, 400, 12)

        draw_vertical_lines()
        draw_horizontal_lines()
        pygame.display.update()


main()
