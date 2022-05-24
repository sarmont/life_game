import copy

import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 10

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for j in range(self.height):
            for i in range(self.width):
                if self.board[j][i] == 0:
                    pygame.draw.rect(screen, 'white', (
                        self.left + self.cell_size * i, self.top + self.cell_size * j, self.cell_size, self.cell_size),
                                     width=1)
                elif self.board[j][i] == 1:
                    pygame.draw.rect(screen, 'green', (
                        self.left + self.cell_size * i, self.top + self.cell_size * j, self.cell_size, self.cell_size),
                                     width=0)

    def get_cell(self, xy):
        x = xy[0]
        y = xy[1]
        if self.left < x < self.cell_size * self.width + self.left and self.top < y < self.cell_size * self.height + self.top:
            x_coords = (x - self.left) // self.cell_size + 1
            y_coords = (y - self.top) // self.cell_size + 1
            return (x_coords, y_coords)
        else:
            return None

    def on_click(self, xy):
        if self.get_cell(xy) is not None:
            x = self.get_cell(xy)[0] - 1
            y = self.get_cell(xy)[1] - 1
            if self.board[y][x] == 0:
                self.board[y][x] = 1
            elif self.board[y][x] == 1:
                self.board[y][x] = 0

    def get_click(self, xy):
        print(board.get_cell(xy))
        board.on_click(xy)


class Life(Board):
    def __init__(self, width, height):
        super().__init__(width, height)

    def count_life_cell(self, x, y):
        """
        подсчет количества живых клеток вокруг текущей
        """
        count = 0
        print('Считаем жизни')
        for i in (0, 1, -1):
            for j in (0, 1, -1):
                if 0 < (x - i) < 40 and 0 < (y - j) < 40 and (i != 0 or j != 0) and self.board[x][y]==1:
                    count += 1
        print((x, y), count)
        return count

    def next_move(self):
        print('Start')
        temp = copy.deepcopy(self.board)
        for j in range(self.height):
            for i in range(self.width):
                if self.board[j][i] == 0:
                    if self.count_life_cell(j, i) == 3:
                        self.board[j][i] = 1
                    elif 2>self.count_life_cell(j, i) > 3:
                        self.board[j][i] = 0
        self.board = copy.deepcopy(temp)


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((410, 410))
    board = Life(39, 39)
    pygame.display.set_caption('Инициализация игры')
    running = True
    start_stop = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print('mouse')
                # xy = pygame.mouse.get_pos()
                board.get_click(event.pos)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                print('space')
                start_stop = not start_stop
        screen.fill((0, 0, 0))
        board.render(screen)
        if start_stop:
            board.next_move()
        pygame.display.flip()
    pygame.quit()
