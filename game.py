import pygame
from random import randrange


class Game:
    """
    all maze actions called by "GameLogic"
    """
    def __init__(self, maze_file):
        # load the file which contains the maze structure
        self.maze_file = maze_file
        self.maze = self.read_file()
        # load MacGyver starting position
        self.mg_pos_x = 1
        self.mg_pos_y = 1
        # instantiate list of picked objects
        self.bag = []
        # list of tuples which contain the names of items and their positions
        self.item_pos = [("syringe", self.random_free_pos()),
                         ("ether", self.random_free_pos()), ("needle", self.random_free_pos())]
        self.window = pygame.display.set_mode((450, 450))
        icon = pygame.image.load('images/MacGyver.png').convert_alpha()
        pygame.display.set_icon(icon)
        pygame.display.set_caption("MacGyver maze")
        # sprite loading loop
        self.pic = {}
        for item in ["background", "macgyver", "guardian", "wall", "needle", "ether", "syringe", "bag", "bag_1",
                     "bag_2", "bag_3", "win", "over"]:
            self.pic[item] = pygame.image.load("images/{}.png".format(item)).convert_alpha()

    def move_to(self, dx, dy):
        """
        move MG if the destination square is free
        """
        if self.is_free(self.mg_pos_x + dx, self.mg_pos_y + dy):
            self.mg_pos_x += dx
            self.mg_pos_y += dy

    def read_file(self):
        """
        generate two dimensions list with the file "maze"
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
        if pos_x < 1 or pos_y < 1 or pos_x > 14 or pos_y > 14:
            return False
        if self.maze[pos_x][pos_y] != "w" and self.maze[pos_x][pos_y] != "X" and self.maze[pos_x][pos_y] != "G":
            return self.maze[pos_x][pos_y]

    def display_at(self, what, pos):
        """
        display a picture of images folder
        """
        self.window.blit(self.pic[what], pos)

    def display_maze(self):
        """
        display all maze elements
        """
        self.display_at('background', (0, 0))
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
                if len(self.bag) == 1:
                    self.display_at('bag_1', (420, 0))
                if len(self.bag) == 2:
                    self.display_at('bag_2', (420, 0))
                if len(self.bag) == 3:
                    self.display_at('bag_3', (420, 0))
                if sprite == 'w':
                    self.window.blit(self.pic["wall"], (c * 30, l * 30))
                if sprite == 'G':
                    self.window.blit(self.pic["guardian"], (c * 30, l * 30))
                if sprite == 'X':
                    pass

        # limit the refresh of pygame to optimize ressources
        pygame.time.Clock().tick(30)
        # refrech the display
        pygame.display.flip()

    def item_picked(self):
        """
        check if MG is on an object square, and delete it from the screen if he is
        """
        for i in self.item_pos:
            if i[1] == (self.mg_pos_x, self.mg_pos_y):
                for j, k in enumerate(self.item_pos):
                    if k[1] == (self.mg_pos_x, self.mg_pos_y):
                        del self.item_pos[j]
                        self.bag.append("object")

    def is_exit(self, pos_x, pos_y):
        """
        check if MG is on the exit tile and had picket 3 objects
        """
        return self.maze[pos_x][pos_y] == "X" and len(self.bag) == 3

    def is_mg_on_exit(self):
        """
        check if MG is on the exit tile, with or without picked 3 objects
        """
        return self.is_exit(self.mg_pos_x, self.mg_pos_y)

    def is_guard(self, pos_x, pos_y):
        """
        check if MG is on the guardian tile, and if he had picked 3 items
        """
        return self.maze[pos_x][pos_y] == "G" and len(self.bag) != 3

    def is_mg_on_guard(self):
        """
        check if MG is on the guardian tile, with or without picked 3 objects
        """
        return self.is_guard(self.mg_pos_x, self.mg_pos_y)

    def user_move(self, direction):
        """
        move MG on the maze according to the user input (key press)
        """
        if direction == 1:
            self.move_to(- 1, 0)
        if direction == 2:
            self.move_to(+ 1, 0)
        if direction == 3:
            self.move_to(0, +1)
        if direction == 4:
            self.move_to(0, -1)
