import pygame
import sys
from pygame.locals import *


WIDTH = 500
ROWS = 20


class Cube(object):
    pass


class Snake(object):

    def __init__(self, color, pos):
        self.color = color
        self.body = []  # list of Cubes
        self.head_pos = pos
        self.body.append(Cube(self.head_pos))
        self.dirx = 0
        self.diry = 1
        self.key_dir_map = {
            pygame.K_LEFT: (-1, 0),
            pygame.K_RIGHT: (1, 0),
            pygame.K_UP: (0, -1),
            pygame.K_DOWN: (0, 1)
        }

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()

            for key in self.key_dir_map:
                if keys[key] and self.key_dir_map[key] != (-self.dirx, -self.diry):  # Can't go to opposite direction
                    self.dirx, self.diry = self.key_dir_map[key]
                    break

        self.body.pop()
        self.head_pos = (self.head_pos[0] + self.dirx, self.head_pos[1] + self.diry)
        self.body.insert(0, Cube(self.head_pos))


class Game:
    def __init__(self):
        self.width = WIDTH
        self.rows = ROWS
        self.window = pygame.display.set_mode((self.width, self.width))  # square window
        # self.snake = Snake((255, 0, 0), (10, 10))
        self.game_on = True

        self.clock = pygame.time.Clock()

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
        self.draw_grid()
        pygame.display.update()

    def play(self):
        while self.game_on:
            for event in pygame.event.get():
                if event.type in (QUIT, KEYDOWN):
                    sys.exit()
            pygame.time.delay(100)
            self.clock.tick(10)
            self.redraw_window()


if __name__ == '__main__':
    my_game = Game()
    my_game.play()
