import pygame
import game_logic

# start pygame
pygame.init()

# instanciation of game_logic
gl = game_logic.GameLogic()

# launch the game
game_on = gl.play_one_game()

if game_on == 2:
    # display the winning screen
    gl.win()
if game_on == 3:
    # display the looser screen
    gl.over()
