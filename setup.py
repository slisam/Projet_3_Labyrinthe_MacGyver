#generate list of list with the maze file
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

#retourner si la sprite est un sol ou pas pour y placer un objet
def is_free(maze,pos_y, pos_x) :
    return maze[pos_y][pos_x] == "0"


def is_wall(maze,pos_y,pos_x) :
    return maze[pos_y][pos_x] == "w"


def display_maze(maze, pos_y, pos_x):
    for l, line in enumerate(maze):
        for c, sprite in enumerate(line):
            if (l, c) == (pos_y, pos_x) :
                print("M", end="")
                continue
            if sprite == '0':
                print('-', end="")
            if sprite == 'w':
                print('#', end="")
            if sprite == 'G':
                print('G', end="")
            if sprite == 'S':
                print('S', end="")
            if sprite == 'T':
                print('T', end="")
            if sprite == 'A':
                print('A', end="")

        print('')

def move_pos(pos_y, pos_x, user_move) :
    if user_move == "z":
        mg_pos(pos_y - 1,pos_x -1)
    if user_move == "s":
        print("Down")
    if user_move == "d":
        print("Right")
    if user_move == "q":
        print("Left")

maze = read_file()
mg_pos_y = 1
mg_pos_x = 1


game_on = 1
while game_on == 1:
    display_maze(maze, mg_pos_y, mg_pos_x)
    user_move = input("Choose MacGyver move : Up(z), Down(s), Right(d), Left (q) ")
    if user_move == "z":
        mg_move_y = mg_pos_y - 1
        mg_move_x = mg_pos_x
    if user_move == "s":
        mg_move_y = mg_pos_y + 1
        mg_move_x = mg_pos_x
    if user_move == "d":
        mg_move_y = mg_pos_y
        mg_move_x = mg_pos_x + 1
    if user_move == "q":
        mg_move_y = mg_pos_y
        mg_move_x = mg_pos_x - 1
    if user_move == "quit":
        game_on = 2
    if is_free(maze,mg_move_y, mg_move_x) :
        mg_pos_y , mg_pos_x = mg_move_y, mg_move_x


# def mg_pos(pos_x, pos_y):
#     mg_maze_pos = maze[pos_x][pos_y]
#     return maze[pos_x- 1][pos_y]


# print(mg_pos(2,2))

'''
def mg_pos(pos_y, pos_x):
    maze[pos_y][pos_x] = "M"



maze =[
[8,8,8,7,7,7,7,7,8,7,7,7,7,7,7],
[8,7,8,8,8,8,8,7,8,7,7,8,7,8,8],
[8,8,7,7,8,7,8,8,8,7,8,8,8,8,7],
[7,8,8,7,7,7,7,7,8,8,8,7,7,7,7],
[7,8,8,7,8,8,8,8,8,7,7,7,8,8,7],
[7,7,8,7,8,7,7,8,7,7,8,8,8,7,7],
[8,8,8,7,7,7,8,8,8,8,8,7,7,7,7],
[8,7,8,8,7,7,7,8,7,8,7,7,8,8,7],
[8,7,7,8,7,8,8,8,7,8,8,8,8,7,7],
[7,7,7,8,8,7,7,7,7,8,7,7,7,7,7],
[7,7,7,8,7,7,8,7,8,8,7,7,8,8,7],
[7,8,8,8,7,8,8,7,8,7,7,8,8,7,7],
[8,8,7,7,7,8,7,8,8,8,8,8,7,7,7],
[7,8,7,7,8,8,7,7,8,7,7,8,7,7,7],
[7,8,8,8,8,7,7,7,8,8,7,8,8,8,9],
]
mg_pos = maze[0][0]
display_maze = ''
for sprite in maze :
    # if sprite == mg_pos:
    #     display_maze+='M'
    if sprite == 8:
        display_maze+='-'
    if sprite == 7:
        display_maze+='#'
    # if sprite == 'G':
    #     display_maze+='G'
    print(display_maze)
















#####################################
# import pygame



    load maze
with open("maze", "r") as file:
    maze_level = []
    display_maze = ''
    for line in file:
        line_maze = []
        for sprite in line:
            if sprite == 'M':
                display_maze+='M'
            if sprite == '0':
                display_maze+='-'
            if sprite == 'w':
                display_maze+='#'
            if sprite == 'G':
                display_maze+='G'
            if sprite == '\n':
                display_maze +='\n'
                line_maze.append(sprite)
        maze_level.append(line_maze)
    #Main loop
# def display_maze(maze_level) :
#
#     for i in maze_level:
#         if i != "\n":
#             print(i)
# print(display_maze(maze_level))
# print(maze_level)
#
# test = maze_level[0][0]
# print(test)
# move = input("Deplacement : Haut(z) Gauche(q) Bas(s) Droite(d)")
# if move == "z":
#     print("bas")

# game_on = 1
#
# while game_on :
#     for event in pygame.event.get():
#         if event.type == KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 #MG.move('right')
#                 print("right")
#             elif event.key == pygame.K_LEFT:
#                 #MG.move('left')
#                 print("right")
#             elif event.key == pygame.K_UP:
#                 #MG.move('up')
#                 print("right")
#             elif event.key == pygame.K_DOWN:
#                 #MG.move('down')
#                 print("right")
#
# def loot:
#
'''