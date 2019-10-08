import pygame
import sys
import random
from pygame.locals import *

WIDTH = 500
ROWS = 20
KEY_DIR_MAP = {
            K_LEFT: (-1, 0),
            K_RIGHT: (1, 0),
            K_UP: (0, -1),
            K_DOWN: (0, 1)
        }


class Cube(object):
    rows = ROWS
    width = WIDTH

    def __init__(self, pos, col):
        self.pos = pos
        self.color = col

    def draw(self, window, eyes=False):
        dis = self.width // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(window, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))
        if eyes:
            centre = dis // 2
            radius = 3
            circle_middle = (i * dis + centre - radius, j * dis + 8)
            circle_middle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(window, (0, 0, 0), circle_middle, radius)
            pygame.draw.circle(window, (0, 0, 0), circle_middle2, radius)


class Candy(object):
    def __init__(self, pos, col=(255, 255, 0)):
        self.pos = pos
        self.color = col
        self.cube = Cube(self.pos, self.color)

    def draw(self, window):
        self.cube.draw(window)


class Snake(object):
    def __init__(self, pos, col=(255, 0, 0)):
        self.color = col
        self.body = []  # list of Cubes
        self.head_pos = pos
        self.body.append(Cube(self.head_pos, self.color))
        self.dirx = 0
        self.diry = 1

    def move(self, candy):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()

            for key in KEY_DIR_MAP:
                if keys[key] and KEY_DIR_MAP[key] != (-self.dirx, -self.diry):  # Can't go to opposite direction
                    self.dirx, self.diry = KEY_DIR_MAP[key]
                    break

        self.head_pos = (self.head_pos[0] + self.dirx, self.head_pos[1] + self.diry)
        if self.head_pos in [c.pos for c in self.body]:
            pygame.quit()
        self.body.insert(0, Cube(self.head_pos, self.color))
        if not self.eat(candy):
            self.body.pop()
            return False
        return True

    def eat(self, candy):
        if self.head_pos == candy.pos:
            return True
        return False

    def draw(self, window):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(window, True)
            else:
                c.draw(window)


class Game:
    def __init__(self):
        self.width = WIDTH
        self.rows = ROWS
        self.window = pygame.display.set_mode((self.width, self.width))  # square window
        self.snake = Snake((10, 10))
        self.candy = self.generate_candy()
        self.game_on = True

        self.clock = pygame.time.Clock()

    def generate_candy(self):
        snake_pos = [c.pos for c in self.snake.body]
        x, y = random.randint(0, 20), random.randint(0, 20)
        while (x, y) in snake_pos:
            x, y = random.randint(0, 20), random.randint(0, 20)
        return Candy((x, y))

    def draw_grid(self):
        size_btwn = self.width // self.rows
        x = y = 0
        for _ in range(self.rows):
            x += size_btwn
            y += size_btwn

            pygame.draw.line(self.window, (255, 255, 255), (x, 0), (x, self.width))
            pygame.draw.line(self.window, (255, 255, 255), (0, y), (self.width, y))

    def redraw_window(self):
        self.window.fill((0, 0, 0))
        self.snake.draw(self.window)
        self.candy.draw(self.window)
        self.draw_grid()
        pygame.display.update()

    def play(self):
        while self.game_on and -1 < self.snake.head_pos[0] < 20 and -1 < self.snake.head_pos[1] < 20:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                keys = pygame.key.get_pressed()
                for key in KEY_DIR_MAP:
                    if keys[key] and KEY_DIR_MAP[key] != (-self.snake.dirx, -self.snake.diry):  # Can't go to opposite direction
                        self.snake.dirx, self.snake.diry = KEY_DIR_MAP[key]
                        break
            pygame.time.delay(50)
            self.clock.tick(5)
            if self.snake.move(self.candy):
                self.candy = self.generate_candy()
            self.redraw_window()


if __name__ == '__main__':
    my_game = Game()
    my_game.play()
