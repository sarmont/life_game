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
                pygame.draw.rect(screen, 'white', (
                    self.left + self.cell_size * i, self.top + self.cell_size * j, self.cell_size, self.cell_size),
                                 width=1)


if __name__ == '__main__':
    pygame.init()

    board = Board(7, 10)
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Инициализация игры')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()
