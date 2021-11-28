import pygame
import board
import game
import gameloop
import event_queue
import renderer
import data.datahandling

def main():
    size = 3
    new_game = game.Game(size)
    new_board = board.Board(new_game)
    new_event_queue = event_queue.EventQueue()
    new_data = data.datahandling.DataHandling()

    cell_size = 100
    display_height = size * cell_size
    display_width = size * cell_size
    display = pygame.display.set_mode((display_width, display_height))

    new_renderer = renderer.Renderer(display, new_board)

    pygame.display.set_caption("2048")

    new_gameloop = gameloop.GameLoop(new_game, new_renderer, new_event_queue)
    new_gameloop.start()

    new_data.add_row(new_game.get_results())

if __name__ == "__main__":
    main()
