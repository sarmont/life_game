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
        self.cell_size = 30

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
                    pygame.draw.rect(screen, 'red', (
                        self.left + self.cell_size * i, self.top + self.cell_size * j, self.cell_size, self.cell_size),
                                     width=0)
                elif self.board[j][i] == 2:
                    pygame.draw.rect(screen, 'blue', (
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
                self.board[y][x] = 2
            elif self.board[y][x] == 2:
                self.board[y][x] = 0

    def get_click(self, xy):
        print(board.get_cell(xy))
        board.on_click(xy)


if __name__ == '__main__':
    pygame.init()

    board = Board(7, 10)
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('События от мыши')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                xy = pygame.mouse.get_pos()
                board.get_click(xy)

        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()
