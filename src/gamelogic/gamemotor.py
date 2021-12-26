import pygame
import gamelogic.game
import gameboard.board
import gameboard.event_queue
import gameboard.gameloop
import gameboard.renderer
import data.datahandling

class GameMotor:
    """Luokka, joka huolehtii uuden pelin pyörittämiseen ja piirtämiseen tarvittavien
    olioiden luomisesta ja kutsumisesta.

    Attributes:
        new_game: Pelilogiikasta vastaava olio
        new_board: Pelilaudan piirtämisestä vastaava olio
        new_event_queue: Tapahtumakäsittelystä vastaava olio
        data_handler: Datan käsittelystä vastaava olio
        new_renderer: Pelilaudan päivittämisestä vastaava olio
    """
    def __init__(self, name, size):
        """Luokan konstruktori, joka luo tarvittavat oliot

        Args:
            name: Pelaajan nimi, jonka pelaaja on antanut uutta peliä aloittaessaan
            size: Pelilaudan koko, jonka pelaaja on valinnut uutta peliä aloittaessaan
        """
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
        """Metodi, joka käynnistää varsinaisen pelin luomalla pelikierroksesta vastaavan
        olion new_gameloop.

        Pelin päättyessä tallennetaan pelin tulokset.
        """
        pygame.display.set_caption("2048")

        new_gameloop = gameboard.gameloop.GameLoop(self.new_game, self.new_renderer,
                                                   self.new_event_queue)
        new_gameloop.start()

        self.data_handler.add_row(self.new_game.get_results())
