maze =[
[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
[7,8,8,8,8,8,8,7,8,7,7,8,7,8,7],
[7,8,7,7,8,7,8,8,8,7,8,8,8,8,7],
[7,8,8,7,7,7,7,7,8,8,8,7,7,7,7],
[7,8,8,7,8,8,8,8,8,7,7,7,8,8,7],
[7,7,8,7,8,7,7,8,7,7,8,8,8,7,7],
[7,8,8,7,7,7,8,8,8,8,8,7,7,7,7],
[7,7,8,8,7,7,7,8,7,8,7,7,8,8,7],
[7,7,7,8,7,8,8,8,7,8,8,8,8,7,7],
[7,7,7,8,8,7,7,7,7,8,7,7,7,7,7],
[7,7,7,8,7,7,8,7,8,8,7,7,8,8,7],
[7,8,8,8,7,8,8,7,8,7,7,8,8,7,7],
[7,8,7,7,7,8,7,8,8,8,8,8,7,7,7],
[7,8,7,7,8,8,7,7,8,7,7,8,8,8,9],
[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
]
mg_pos = maze[0][0]

for sprite in maze :
    if sprite == mg_pos:
        display_maze+='M'
    if sprite == '8':
        display_maze+='-'
    if sprite == '7':
        display_maze+='#'
    # if sprite == 'G':
    #     display_maze+='G'
    print sprite