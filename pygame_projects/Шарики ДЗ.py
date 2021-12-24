import pygame as pg


class Circles:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        self.x, self.y = pg.mouse.get_pos()
        self.r = 10
        self.direction = 1
        self.dx = -1
        self.dy = -1
        self.clock = pg.time.Clock()

    def move(self):

        dt = self.clock.tick() / 1000
        if self.x <= self.r:
            self.x = self.r
            self.dx *= -1
        elif self.x >= self.screen_width - self.r:
            self.x = self.screen_width - self.r
            self.dx *= -1
        elif self.y <= self.r:
            self.y = self.r
            self.dy *= -1
        elif self.y >= self.screen_height - self.r:
            self.y = self.screen_height - self.r
            self.dy *= -1
        self.show()
        self.x += 100 * dt * self.dx
        self.y += 100 * dt * self.dy

    def show(self):
        pg.draw.circle(self.screen, 'white', (int(self.x), int(self.y)), self.r)


if __name__ == '__main__':
    pg.init()
    size = width, height = 500, 400
    screen = pg.display.set_mode(size)
    pg.display.set_caption('Шарики')
    running = True
    balls = []

    while running:
        screen.fill('black')
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                circle = Circles(screen)
                balls.append(circle)

        for ball in balls:
            ball.move()

        pg.display.flip()
    pg.quit()
