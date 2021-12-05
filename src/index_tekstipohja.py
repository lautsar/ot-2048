import pygame

import gameboard.board
import gamelogic.game
import gameboard.gameloop
import gameboard.event_queue
import gameboard.renderer

import data.datahandling

def main():
    error = False
    name = input("Player name (optional): ")
    new_size = input("Select grid size (3, 4, 5): ")

    if len(name) == 0:
        name = "Unknown"

    try:
        size = int(new_size)
    except ValueError:
        error = True

    if error is True or size < 3 or size > 5:
        size = 4

    new_game = gamelogic.game.Game(size, name)
    new_board = gameboard.board.Board(new_game)
    new_event_queue = gameboard.event_queue.EventQueue()
    new_data = data.datahandling.DataHandling()

    cell_size = 100
    display_height = size * cell_size
    display_width = size * cell_size
    display = pygame.display.set_mode((display_width, display_height))

    new_renderer = gameboard.renderer.Renderer(display, new_board)

    pygame.display.set_caption("2048")

    new_gameloop = gameboard.gameloop.GameLoop(new_game, new_renderer, new_event_queue)
    new_gameloop.start()

    new_data.add_row(new_game.get_results())
    new_data.sort_data()

if __name__ == "__main__":
    main()
