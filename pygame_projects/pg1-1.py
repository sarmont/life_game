import pygame


def draw_board(screen, w, n):
    width = screen.get_width()
    height = screen.get_height()
    screen.fill((0, 0, 0))
    colors = ('red', 'green', 'blue')
    for i in range(n):
        pygame.draw.circle(screen, colors[i % 3], (width // 2, height // 2), (n - i) * w)


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:

    size = input()
    # screen — холст, на котором нужно рисовать:
    try:
        size = [int(el) for el in size.split()]
        screen = pygame.display.set_mode((size[0] * size[1] * 2, size[0] * size[1] * 2))
        # формирование кадра:
        # команды рисования на холсте
        pygame.display.set_caption('Мишень')
        draw_board(screen, size[0], size[1])
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
