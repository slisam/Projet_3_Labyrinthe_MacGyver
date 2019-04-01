from random import randrange
import pygame
from pygame.locals import *

class Game:

    def __init__(self, maze_file):
        """
        maze object
        """
        self.maze_file = maze_file
        self.maze = self.read_file()
        self.mg_pos_x = 1
        self.mg_pos_y = 1
        self.bag = []
        self.item_pos = [("syringe", self.random_free_pos()), ("ether", self.random_free_pos()), ("needle", self.random_free_pos())]
        pygame.init()
        self.window = pygame.display.set_mode((450, 450))
        icon = pygame.image.load('images/MacGyver.png')
        pygame.display.set_icon(icon)
        # Titre
        pygame.display.set_caption("MacGyver maze")
        self.pic = {}
        for item in ["background", "macgyver", "guardian", "wall", "needle", "ether", "syringe", "bag"]:
            self.pic[item] = pygame.image.load("images/{}.png".format(item)).convert()

    def move_to(self, dx, dy):
        """
        move MG if the destination square is free
        """
        if self.is_free(self.mg_pos_x + dx, self.mg_pos_y + dy):
            self.mg_pos_x += dx
            self.mg_pos_y += dy

    def read_file(self):
        """
        generate a list of a list with the file "maze"
        """
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
        """
        return a random free square
        """
        while True:
            x, y = randrange(16), randrange(16)
            if self.is_free(x, y):
                return x, y

    def is_free(self, pos_x, pos_y):
        """
        check if the square is free
        """
        if pos_x < 0 or pos_y < 0 or pos_x > 14 or pos_y > 14:
            return False
        return self.maze[pos_x][pos_y] != "w"

    def display_at(self, what, pos):
        """
        display a picture of images folder
        """
        self.window.blit(self.pic[what], pos)

    def display_maze(self):
        """
        display all maze elements
        """
        self.display_at('background',(0,0))
        for l, line in enumerate(self.maze):
            for c, sprite in enumerate(line):
                if (l, c) == (self.mg_pos_x, self.mg_pos_y):
                    self.display_at('macgyver',  (c*30, l*30))
                    continue
                displayed_object = False
                for o, pos in self.item_pos:
                    if (l, c) == (pos[0], pos[1]):
                        self.display_at('macgyver', (c * 30, l * 30))
                        self.window.blit(self.pic[o], (c * 30, l * 30))
                        displayed_object = True
                if displayed_object:
                    continue
                if sprite == 'w':
                    self.window.blit(self.pic["wall"], (c * 30, l * 30))
                if sprite == 'G':
                    self.window.blit(self.pic["guardian"], (c * 30, l * 30))
                if sprite == 'X':
                    pass
            print('')
        pygame.time.Clock().tick(30)
        pygame.display.flip()


    def item_picked(self):
        """

        :return:
        """
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
            dir = self.get_direction()
            if dir == 0:
                continue
            if dir == -1:
                game_on = 0
            else:
                self.game.user_move(dir)
                if self.game.is_mg_on_exit():
                    game_on = 2
                if self.game.is_mg_on_guard():
                    game_on = 3
                self.game.item_picked()
        return game_on

    @staticmethod
    def get_direction():
        for event in pygame.event.get():

            # Si l'utilisateur quitte, on met la variable qui continue le jeu
            # ET la variable générale à 0 pour fermer la fenêtre
            if event.type == QUIT:
                return -1
            elif event.type == KEYDOWN:
                # Si l'utilisateur presse Echap ici, on revient seulement au menu
                if event.key == K_ESCAPE:
                    return -1
                elif event.key == K_RIGHT:
                    return 3
                elif event.key == K_LEFT:
                    return 4
                elif event.key == K_UP:
                    return 1
                elif event.key == K_DOWN:
                    return 2
            return 0




gl = GameLogic()
game_on = gl.play_one_game()
if game_on == 2:
    print("You win!")
if game_on == 3:
    print("You Died!")
