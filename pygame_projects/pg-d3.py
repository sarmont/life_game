import pygame


def draw_romb(screen, n):
    width = screen.get_width()
    height = screen.get_height()

    screen.fill('yellow')
    for j in range(height // n):
        for i in range(width // n):
            pygame.draw.polygon(screen, 'orange',
                                [(0 + i * n, n // 2 + j * n), (n // 2 + i * n, 0 + j * n), (n + i * n, n // 2 + j * n),
                                 (n // 2 + i * n, n + j * n)],
                                width=0)


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:

    n = int(input())
    # screen — холст, на котором нужно рисовать:
    # размер холста
    size = (500, 300)
    try:
        screen = pygame.display.set_mode(size)
        # формирование кадра:
        # команды рисования на холсте
        pygame.display.set_caption('Кирпичи')
        draw_romb(screen, n)
        # ...
        # смена (отрисовка) кадра:
        pygame.display.flip()
        # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
        # завершение работы:
        pygame.quit()
    except ValueError:
        print("Неправильный формат ввода")
        pygame.quit()
