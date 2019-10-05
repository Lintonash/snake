import pygame

WIDTH = 500
ROWS = 20


class Snake:
    def __init__(self):
        pass


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
            pygame.time.delay(50)
            self.clock.tick(10)
            self.redraw_window()

if __name__ == '__main__':
    my_game = Game()
    my_game.play()