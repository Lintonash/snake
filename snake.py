import pygame
import sys
import random
from pygame.locals import *

WIDTH = 500
ROWS = 20


class Cube(object):
    rows = ROWS
    width = WIDTH

    def __init__(self, pos, col=(255, 0, 0)):
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
        self.cube = Cube(pos, col)

    def draw(self, window):
        self.cube.draw(window)


class Snake(object):
    def __init__(self, pos, col):
        self.color = col
        self.body = []  # list of Cubes
        self.head_pos = pos
        self.body.append(Cube(self.head_pos))
        self.dirx = 0
        self.diry = 1
        self.key_dir_map = {
            K_LEFT: (-1, 0),
            K_RIGHT: (1, 0),
            K_UP: (0, -1),
            K_DOWN: (0, 1)
        }

    def move(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()

            for key in self.key_dir_map:
                if keys[key] and self.key_dir_map[key] != (-self.dirx, -self.diry):  # Can't go to opposite direction
                    self.dirx, self.diry = self.key_dir_map[key]
                    break

        self.head_pos = (self.head_pos[0] + self.dirx, self.head_pos[1] + self.diry)
        self.body.insert(0, Cube(self.head_pos))
        self.body.pop()

    def eat(self):
        if self.head_pos

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
        self.draw_grid()
        pygame.display.update()

    def play(self):
        while self.game_on:
            # Necessary sentence
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            pygame.time.delay(100)
            self.clock.tick(10)
            self.snake.move()
            self.redraw_window()


if __name__ == '__main__':
    my_game = Game()
    my_game.play()
