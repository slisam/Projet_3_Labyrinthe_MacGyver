from random import randrange
import pygame
from pygame.locals import *

pygame.init()
class Game:

    def __init__(self, maze_file):
        self.maze_file = maze_file
        self.maze = self.read_file()
        self.mg_pos_x = 1
        self.mg_pos_y = 1
        self.bag = []
        self.item_pos = [("S", self.random_free_pos()), ("T", self.random_free_pos()), ("A", self.random_free_pos())]

    def move_to(self, dx, dy):
        if self.is_free(self.mg_pos_x + dx * 15, self.mg_pos_y + dy * 15):
            self.mg_pos_x += dx
            self.mg_pos_y += dy

    def read_file(self):
        maze = []
        with open(self.maze_file, "r") as file:
            for line in file:
                line_maze = []
                for sprite in line:
                    if sprite != '\n':
                        line_maze.append(sprite)
                maze.append(line_maze)
        return maze

    def random_free_pos(self):
        while True:
            x, y = randrange(16), randrange(16)
            if self.is_free(x, y):
                return x, y

    def is_free(self, pos_x, pos_y):
        if pos_x < 0 or pos_y < 0 or pos_x > 14 or pos_y > 14:
            return False
        return self.maze[pos_x][pos_y] != "w"

    def display_maze(self):
        print(self.bag)
        wall = pygame.image.load("images/wall.png").convert_alpha()
        guardian = pygame.image.load("images/wall.png").convert_alpha()
        for l, line in enumerate(self.maze):
            for c, sprite in enumerate(line):
                if (l, c) == (self.mg_pos_x, self.mg_pos_y):
                    print("M", end="")
                    continue
                displayed_object = False
                for o, pos in self.item_pos:
                    if (l, c) == (pos[0], pos[1]):
                        print(o, end="")
                        displayed_object = True
                if displayed_object:
                    continue
                if sprite == '0':
                    print('-', end="")
                if sprite == 'w':
                    print('#', end="")
                if sprite == 'G':
                    print('G', end="")
                if sprite == 'X':
                    print('X', end="")
            print('')

    def is_wall(self, pos_x, pos_y):
        return self.maze[pos_x][pos_y] == "w"

    def item_picked(self, pos_x, pos_y):
        for i in self.item_pos:
            if i[1] == (pos_x, pos_y):
                for j, k in enumerate(game.item_pos):
                    if k[1] == (game.mg_pos_x, game.mg_pos_y):
                        game.bag.append(k[0])
                        del game.item_pos[j]

    def is_exit(self, pos_x, pos_y):
        if self.maze[pos_x][pos_y] == "X" and len(self.bag) == 3:
            return True

    def is_guard(self, pos_x, pos_y):
        if self.maze[pos_x][pos_y] == "G" and len(self.bag) != 3:
            return True


game = Game("maze")


game_on = 1
while game_on == 1:

    WINDOWS = pygame.display.set_mode((450, 450))
    BACKGROUND = pygame.image.load("images/background.jpg").convert()
    WINDOWS.blit(BACKGROUND, (0, 0))
    MG = pygame.image.load("images/MacGyver.png").convert()
    WINDOWS.blit(MG, (30, 30))
    pygame.display.flip()


    for event in pygame.event.get():
        pygame.time.Clock().tick(30)

        game.display_maze()
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            game_on = 2
        if event.type == K_UP:
            print("haut")
            game.move_to(- 1, 0)
        if event.type == K_DOWN:
            game.move_to(+ 1, 0)
        if event.type == K_RIGHT:
            game.move_to(0, +1)
        if event.type == K_UP:
            game.move_to(0, -1)

    if game.is_exit(game.mg_pos_x, game.mg_pos_y):
        game_on = 2
    if game.is_guard(game.mg_pos_x, game.mg_pos_y):
        game_on = 3
    game.item_picked(game.mg_pos_x, game.mg_pos_y)

if game_on == 2:
    print("You win!")
if game_on == 3:
    print("You Died!")
