from random import randrange
# generate list of list with the maze file

def read_file():
    with open("maze", "r") as file:
        maze = []
        for line in file:
            line_maze = []
            for sprite in line:
                if sprite != '\n':
                    line_maze.append(sprite)
            maze.append(line_maze)
    return maze


# retourner si la sprite est un sol ou pas pour y placer un objet
def is_free(maze, pos_x, pos_y):
    if pos_x < 0 or pos_y <0 or pos_x > 14 or pos_y > 14:
        return False
    return maze[pos_x][pos_y] != "w"

def random_free_pos(maze):
    while True:
        x, y = randrange(16), randrange(16)
        if is_free(maze,x,y):
            return x,y


# retourner si la sprite est un mur pour eviter d'y placer quelque chose
def is_wall(maze, pos_x, pos_y):
    return maze[pos_x][pos_y] == "w"


def display_maze(maze, mg_pos_x, mg_pos_y, item_pos):

    for l, line in enumerate(maze):
        for c, sprite in enumerate(line):
            if (l, c) == (mg_pos_x, mg_pos_y):
                print("M", end="")
                continue
            displayed_object = False
            for o, pos in item_pos:
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


maze = read_file()
# à modifier par 1 seul tuple
mg_pos_x = 1
mg_pos_y = 1
# mg_pos_x = mg_pos[0]
# mg_pos_y = mg_pos[1]


item_pos = [("S", random_free_pos(maze)), ("T", random_free_pos(maze)), ("A", random_free_pos(maze))]
def display_item(items):
    items_pos2 = []
    for item in items:
        displayed_item = False
        while not displayed_item:
            x, y = randrange(16), randrange(16)
            if is_free(maze, x, y) & (x, y) not in items_pos2:
                items_pos2[item] = (x, y)
                displayed_item = True
    return items_pos2


bag = []

def item_picked(item_pos, pos_x, pos_y):
    for i in item_pos:
        if i[1] == (pos_x,pos_y):
            return True


game_on = 1
while game_on == 1:
    print(bag)
    display_maze(maze, mg_pos_x, mg_pos_y, item_pos)
    user_move = input("Choose MacGyver move : Up(z), Down(s), Right(d), Left (q) ")
    if user_move == "z":
        if is_free(maze, mg_pos_x -1, mg_pos_y):
            mg_pos_x = mg_pos_x - 1
    if user_move == "s":
        if is_free(maze, mg_pos_x + 1, mg_pos_y):
            mg_pos_x = mg_pos_x + 1
    if user_move == "d":
        if is_free(maze, mg_pos_x, mg_pos_y + 1):
            mg_pos_y = mg_pos_y + 1
    if user_move == "q":
        if is_free(maze, mg_pos_x, mg_pos_y - 1):
            mg_pos_y = mg_pos_y - 1
    if user_move == "quit":
        game_on = 2
    if item_picked(item_pos,mg_pos_x, mg_pos_y):
        for j, i in enumerate(item_pos):
            if i[1] == (mg_pos_x, mg_pos_y):
                bag.append(i[0])
                del item_pos[j]
    if maze[mg_pos_x][mg_pos_y] == "X" and len(bag) == 3 :
            game_on = 2
    if maze[mg_pos_x][mg_pos_y] == "G" and len(bag) != 3 :
            game_on = 3

if game_on == 2:
    print("You win!")
if game_on == 3:
    print("You Died!")

