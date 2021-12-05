import pygame
import gamelogic.game
import gameboard.board
import gameboard.event_queue
import gameboard.gameloop
import gameboard.renderer
import data.datahandling

class GameMotor:
    def __init__(self, name, size):
        self.new_game = gamelogic.game.Game(size, name)
        self.new_board = gameboard.board.Board(self.new_game)
        self.new_event_queue = gameboard.event_queue.EventQueue()
        self.data_handler = data.datahandling.DataHandling()

        cell_size = 100
        display_height = size * cell_size
        display_width = size * cell_size
        display = pygame.display.set_mode((display_width, display_height))

        self.new_renderer = gameboard.renderer.Renderer(display, self.new_board)

    def start(self):
        pygame.display.set_caption("2048")

        new_gameloop = gameboard.gameloop.GameLoop(self.new_game, self.new_renderer, 
                                                   self.new_event_queue)
        new_gameloop.start()

        self.data_handler.add_row(self.new_game.get_results())
