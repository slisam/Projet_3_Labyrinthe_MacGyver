import pygame
import game_logic

# start pygame
pygame.init()

gl = game_logic.GameLogic()
# gl
# launch the game
game_on = gl.play_one_game()

if game_on == 2:
    print("You win!")
if game_on == 3:
    print("You Died!")
