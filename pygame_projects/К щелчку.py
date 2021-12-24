import pygame as pg


class Circle:
    def __init__(self, screen):
        self.screen = screen
        self.r = 20
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.x = self.screen_width // 2
        self.y = self.screen_height // 2

    def show(self):
        pg.draw.circle(screen, 'red', (self.x, self.y), self.r)

    def go_to(self, m_x, m_y):

        dx = 0
        dy = 0
        if m_x < self.x:
            dx = -1
        if m_x > self.x:
            dx = 1
        if m_y < self.y:
            dy = -1
        if m_y > self.y:
            dy = 1

        self.x += 1 * dx
        self.y += 1 * dy


if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode((501, 501))
    pg.display.set_caption('К щелчку')
    running = True
    red_circle = Circle(screen)
    red_circle.show()
    f = False
    m_x, m_y = 0, 0
    clock = pg.time.Clock()
    while running:
        screen.fill('black')
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                m_x, m_y = pg.mouse.get_pos()
                f = True
        if (f is True) and ((m_x != int(red_circle.x)) or (m_y != int(red_circle.y))):
            red_circle.go_to(m_x, m_y)
        else:
            f = False
        clock.tick(50)
        red_circle.show()
        pg.display.flip()
    pg.quit()
