import pygame
import game
import time


class GameLogic:
    """
    run the global logic of the maze
    """

    def __init__(self):
        """
        take the 'maze' file to generate the maze
        """
        self.game = game.Game("maze")

    def play_one_game(self):
        """
        loop which run the maze
        """
        game_exit = 1
        while game_exit == 1:
            self.game.display_maze()
            direction = self.get_direction()
            if direction == 0:
                continue
            if direction == -1:
                game_exit = 0
            else:
                self.game.user_move(direction)
                if self.game.is_mg_on_exit():
                    game_exit = 2
                if self.game.is_mg_on_guard():
                    game_exit = 3
                self.game.item_picked()
        return game_exit

    @staticmethod
    def get_direction():
        """
        take the input according to the key pressed by the user and use the 'user_move' function to move MG
        """
        for event in pygame.event.get():
            # loop in all events of pygame
            if event.type == pygame.KEYDOWN:
                # detect the key pressed by the user
                if event.key == pygame.K_ESCAPE:
                    return -1
                elif event.key == pygame.K_RIGHT:
                    return 3
                elif event.key == pygame.K_LEFT:
                    return 4
                elif event.key == pygame.K_UP:
                    return 1
                elif event.key == pygame.K_DOWN:
                    return 2
            return 0

    def win(self):
        """
        display the winning screen
        """
        self.game.display_at("win", (0, 0))
        pygame.display.flip()
        time.sleep(5)

    def over(self):
        """
        display the looser screen
        """
        self.game.display_at("over", (0, 0))
        pygame.display.flip()
        time.sleep(5)
