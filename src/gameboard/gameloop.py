import pygame

class GameLoop:
    """Luokka huolehtii yhden pelikierroksen toteutuksesta.

    Attributes:
        _board: Kuluvan pelin pelilauta
        _renderer: Pygamen piirtämisestä huolehtiva olio
        _event_queue: Pygamen tapahtumajonosta huolehtiva olio
    """
    def __init__(self, board, renderer, event_queue):
        """Luokan konstruktori, joka saa parametreina kaikki tarvittavat komponentit

        Args:
            board: Pelilauta
            renderer: Pelilaudan päivittäjä
            event_queue: Tapahtumajono
        """
        self._board = board
        self._renderer = renderer
        self._event_queue = event_queue

    def start(self):
        """Metodi käynnistää pelikierroksen, kutsuu tapahtumankäsittelijää ja
        päivittää pelilautaa tapahtumankäsittelijän antamien tietojen mukaisesti.
        """
        while True:
            if self.handle_events() is False:
                self._board.set_biggest()
                self.close()
                break

            self.render()

    def handle_events(self):
        """Metodi, joka tulkitsee käyttäjän nuolinäppäimillä antamia komentoja
        ja kutsuu pelilogiikasta huolehtivaa oliota niiden mukaan.
        """
        for event in self._event_queue.get():
            if self._board.game_continues() is False:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self._board.move_left() is True:
                        self._board.new_tile()
                    return True
                if event.key == pygame.K_RIGHT:
                    if self._board.move_right() is True:
                        self._board.new_tile()
                    return True
                if event.key == pygame.K_UP:
                    if self._board.move_up() is True:
                        self._board.new_tile()
                    return True
                if event.key == pygame.K_DOWN:
                    if self._board.move_down() is True:
                        self._board.new_tile()
                    return True
            elif event.type == pygame.QUIT:
                return False

    def render(self):
        """Metodi kutsuu renderöijää, joka päivittää pelilaudan.
        """
        self._renderer.render()

    def close(self):
        """Metodi kutsuu renderöijää, joka sulkee peli-ikkunan.
        """
        self._renderer.close_window()
