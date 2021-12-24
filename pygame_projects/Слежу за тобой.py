import pygame


def draw(screen):
    screen.fill('black')
    print('ok')
    global n
    n = n + 1
    font = pygame.font.Font(None, 100)
    text = font.render(str(n), True, 'red')
    text_x = screen.get_width() // 2 - text.get_width() // 2
    text_y = screen.get_height() // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()

    screen = pygame.display.set_mode((200, 200))
    # формирование кадра:
    # команды рисования на холсте
    pygame.display.set_caption('Слежу за тобой')

    # ожидание закрытия окна:
    running = True
    n = -1
    draw(screen)
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEOEXPOSE:
                draw(screen)

        pygame.display.flip()
    pygame.quit()
