from random import randrange
# import pygame
# from pygame.locals import *


class Game:

    def __init__(self, maze_file):
        self.maze_file = maze_file
        self.maze = self.read_file()
        self.mg_pos_x = 1
        self.mg_pos_y = 1
        self.bag = []
        self.item_pos = [("S", self.random_free_pos()), ("T", self.random_free_pos()), ("A", self.random_free_pos())]

    def move_to(self, dx, dy):
        if self.is_free(self.mg_pos_x + dx, self.mg_pos_y + dy):
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

    def item_picked(self):
        for i in self.item_pos:
            if i[1] == (self.mg_pos_x, self.mg_pos_y):
                for j, k in enumerate(self.item_pos):
                    if k[1] == (self.mg_pos_x, self.mg_pos_y):
                        self.bag.append(k[0])
                        del self.item_pos[j]

    def is_exit(self, pos_x, pos_y):
        return self.maze[pos_x][pos_y] == "X" and len(self.bag) == 3

    def is_mg_on_exit(self):
        return self.is_exit(self.mg_pos_x, self.mg_pos_y)

    def is_guard(self, pos_x, pos_y):
        return self.maze[pos_x][pos_y] == "G" and len(self.bag) != 3

    def is_mg_on_guard(self):
        return self.is_guard(self.mg_pos_x, self.mg_pos_y)

    def user_move(self, direction):
        if direction == 1:
            self.move_to(- 1, 0)
        if direction == 2:
            self.move_to(+ 1, 0)
        if direction == 3:
            self.move_to(0, +1)
        if direction == 4:
            self.move_to(0, -1)





class GameLogic:

    def __init__(self):
        self.game = Game("maze")

    def play_one_game(self):
        game_on = 1
        while game_on == 1:
            self.game.display_maze()
            self.game.user_move(self.get_direction())
            if self.game.is_mg_on_exit():
                game_on = 2
            if self.game.is_mg_on_guard():
                game_on = 3
            self.game.item_picked()
        return game_on

    @staticmethod
    def get_direction():
        while True:
            direction = input("Choose MacGyver move : Up(z), Down(s), Right(d), Left (q) ")
            if direction and direction.lower() in "zqsd":
                return {"z": 1, "s": 2, "d": 3, "q": 4}[direction.lower()]

GameLogic.play_one_game()
gl = GameLogic()
game_on = gl.play_one_game()
if game_on == 2:
    print("You win!")
if game_on == 3:
    print("You Died!")
