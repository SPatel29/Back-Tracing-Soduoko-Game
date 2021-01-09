from Soduko_Board_Algorithim import Algorithm
import pygame

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

ACTIVE_COLOR = (173, 216, 230)
UN_ACTIVE_COLOR = RED


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
    count = 0
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

    for x in range(len(my_lst)):
        print(my_lst[x].get_value(), my_lst[x].get_row(), my_lst[x].get_col(), "VALue, X, Y")

    running = True
    pygame.init()
    clock = pygame.time.Clock()
    while running:
        clock.tick(60)
        SCREEN.fill(WHITE)
        for i in range(len(my_lst)):
            my_lst[i].draw_rectangle()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(my_lst)):
                    print(my_lst[i].get_active())
                    if pygame.Rect.collidepoint(my_lst[i].get_tile(),pygame.mouse.get_pos()):
                        my_lst[i].set_active(True)
                    else:
                        my_lst[i].set_active(False)

        #SCREEN.fill(WHITE)  # UNCOMMENT THIS TO GET UN-DISPLAY THE RED RECTANGLES, BUT STILL HAVE THEM ON THE BACKGROUND
        draw_vertical_lines()
        draw_horizontal_lines()
        pygame.display.update()


main()
