import pygame


def draw_sphere(screen, n):
    width = screen.get_width()
    height = screen.get_height()
    step_x = width // 2 // n
    screen.fill((0, 0, 0))
    for i in range(n):
        pygame.draw.ellipse(screen, 'white', (0 + i * step_x, 0, width - 2 * step_x * i, height), width=1)
        pygame.draw.ellipse(screen, 'white', (0, 0 + i * step_x, width, height - 2 * step_x * i), width=1)


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:

    n = int(input())
    # screen — холст, на котором нужно рисовать:
    try:
        screen = pygame.display.set_mode((300, 300))
        # формирование кадра:
        # команды рисования на холсте
        pygame.display.set_caption('Сфера')
        draw_sphere(screen, n)
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
