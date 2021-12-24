import pygame as pg


class Rectangle:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.x = 0
        self.y = 0
        self.r_width = 100
        self.r_height = 100

    def show(self):
        pg.draw.rect(self.screen, 'green', (self.x, self.y, self.r_width, self.r_height))

    def move(self):
        pass


if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode((300, 300))

    pg.display.set_caption('Перетаскивание')
    running = True
    green_rect = Rectangle(screen)
    x = 0
    y = 0
    dx = 0
    dy = 0

    f = False
    while running:
        screen.fill('black')
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                dx = pg.mouse.get_pos()[0] - green_rect.x
                dy = pg.mouse.get_pos()[1] - green_rect.y
                f = True

            if event.type == pg.MOUSEMOTION and f is True:
                x_cursor = pg.mouse.get_pos()[0]
                y_cursor = pg.mouse.get_pos()[1]
                x = x_cursor - dx
                y = y_cursor - dy
                green_rect.x = x
                green_rect.y = y
            if event.type == pg.MOUSEBUTTONUP:
                f = False

        green_rect.show()
        pg.display.flip()
    pg.quit()
