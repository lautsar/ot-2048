import random

class Game:
    """Luokka, joka huolehtii pelin sääntöjen toiminnasta.

    Attributes:
        size: Pelilaudan koko
        player: Pelaajan nimi
        map: Pelilaudan kartta
        moves: Peliin käytettyjen siirtojen määrä
        biggest: Pelilaudalla olevan suurimman laatan arvo pelin lopussa
    """

    def __init__(self, size, player):
        """Luokan konstruktori, joka luo uuden pelin.

        Args:
            size: Halutun pelilaudan koko
            player: Pelaajan nimi, jos se on annettu.
        """
        self.size = size
        if len(player) > 0:
            self.player = player
        else:
            self.player = "Unknown"
        self.map = []
        self.moves = 0
        self.biggest = 0
        self.initialize_map()

    def initialize_map(self):
        """Alustaa pelilaudan, kun uusi peli aloitetaan.

        Kaikki ruudut alustetaan ensin nollaksi. Sen jälkeen kutsutaan metodia,
        joka arpoo pelilaudalle uusia laattoja.
        """
        new_map = []
        for row in range(self.size):
            new_map.append([])

            for column in range(self.size):
                new_map[row].append(0)

        self.map = new_map

        drawn_tiles = 0

        while drawn_tiles < self.size:
            if self.new_tile() is True:
                drawn_tiles = drawn_tiles + 1

    def new_tile(self):
        """Arpoo laudalle tyhjään kohtaan laatan, jonka arvo on kaksi.

        Returns:
            True, jos laudalla on tyhjiä laattoja ja uuden laatan lisääminen onnistuu.
            False, jos tyhjiä laattoja ei ole.
        """
        empty_tiles = self.empty_tiles()

        if len(empty_tiles) == 0:
            return False

        drawn = random.randint(0, len(empty_tiles) - 1)

        y = empty_tiles[drawn][0]
        x = empty_tiles[drawn][1]

        self.map[y][x] = 2
        return True

    def empty_tiles(self):
        """Etsii ruudukossa olevat tyhjät laatat ja tallentaa ne listaan.

        Returns:
            Listan tyhjistä laatoista. Lista on tyhjä, jos tyhjiä laattoja ei ole.
        """
        empty = []
        for column in range(self.size):
            for row in range(self.size):
                if self.map[row][column] == 0:
                    empty.append((row, column))

        return empty

    def swap_tiles(self, from_x, from_y, to_x, to_y):
        """Päivittää laattojen arvot siirtojen yhteydessä.

        Jos lähtöruudun arvo on 0 tai lähtö- ja kohderuudun arvot eroavat,
        ei tehdä mitään. Jos kohderuudun arvo on 0, vaihdetaan ruutujen arvot.
        Jos lähtö- ja kohderuutujen arvot ovat samat, asetetaan kohderuudun
        arvoksi näiden summa ja lähtöruudun arvoksi 0.

        Args:
            from_x: Lähtöruudun sarake
            from_y: Lähtöruudun rivi
            to_x: Kohderuudun sarake
            to_y: Kohderuudun rivi

        Returns:
            True, jos vaihto muutti laudan tilannetta.
            False, jos mitään ei tapahdu.
        """
        from_tile = self.map[from_y][from_x]
        to_tile = self.map[to_y][to_x]

        if from_tile == 0:
            return False
        elif to_tile == 0:
            self.map[to_y][to_x] = from_tile
            self.map[from_y][from_x] = 0
            return True
        elif from_tile == to_tile:
            self.map[to_y][to_x] = from_tile + to_tile
            self.map[from_y][from_x] = 0
            return True
        else:
            return False

    def move_left(self):
        """Yrittää siirtää kaikkia laudan ruutuja vasemmalle kutsumalla swap_tiles-metodia.

        Returns:
            True, jos siirto aiheuttaa jonkin muutoksen laudalla.
            False, jos mitään ei tapahdu siirron seurauksena.
        """
        legal_move = False
        for row in range(self.size):
            for column in range(self.size - 1):
                for column in range(self.size - 1):
                    if self.swap_tiles(column+1, row, column, row) is True:
                        legal_move = True

        if legal_move is True:
            self.moves += 1

        return legal_move

    def move_right(self):
        """Yrittää siirtää kaikkia laudan ruutuja oikealle kutsumalla swap_tiles-metodia.

        Returns:
            True, jos siirto aiheuttaa jonkin muutoksen laudalla.
            False, jos mitään ei tapahdu siirron seurauksena.
        """
        legal_move = False
        for row in range(self.size):
            for column in range(self.size - 1):
                for column in range(self.size - 1):
                    if self.swap_tiles(column, row, column + 1, row) is True:
                        legal_move = True

        if legal_move is True:
            self.moves += 1

        return legal_move

    def move_up(self):
        """Yrittää siirtää kaikkia laudan ruutuja ylös kutsumalla swap_tiles-metodia.

        Returns:
            True, jos siirto aiheuttaa jonkin muutoksen laudalla.
            False, jos mitään ei tapahdu siirron seurauksena.
        """
        legal_move = False
        for column in range(self.size):
            for row in range(self.size - 1):
                for row in range(self.size - 1):
                    if self.swap_tiles(column, row + 1, column, row) is True:
                        legal_move = True

        if legal_move is True:
            self.moves += 1

        return legal_move

    def move_down(self):
        """Yrittää siirtää kaikkia laudan ruutuja alas kutsumalla swap_tiles-metodia.

        Returns:
            True, jos siirto aiheuttaa jonkin muutoksen laudalla.
            False, jos mitään ei tapahdu siirron seurauksena.
        """
        legal_move = False
        for column in range(self.size):
            for row in range(self.size - 1):
                for row in range(self.size - 1):
                    if self.swap_tiles(column, row, column, row + 1) is True:
                        legal_move = True

        if legal_move is True:
            self.moves += 1

        return legal_move

    def game_continues(self):
        """Tarkistaa, jatkuuko peli vielä.

        Returns:
            True, jos peli voi vielä jatkua, eli jos laudalla on tyhjiä laattoja tai jos
            samalla rivillä tai sarakkeella on kaksi saman arvoista laattaa vierekkäin.
            False, jos peli päättyy, eli pelaaja on voittanut saamalla 2048-laatan tai
            hävinnyt, koska mahdollisia siirtoja ei ole enää jäljellä.
        """
        for row in range(self.size):
            for column in range(self.size):
                if self.map[row][column] == 2048:
                    return False

        for row in range(self.size):
            for column in range(self.size):
                if self.map[row][column] == 0:
                    return True

        for row in range(self.size):
            for column in range(self.size - 1):
                if self.map[row][column] == self.map[row][column + 1]:
                    return True

        for row in range(self.size - 1):
            for column in range(self.size):
                if self.map[row + 1][column] == self.map[row][column]:
                    return True

        return False

    def set_biggest(self):
        """Asettaa pelin suurimman laatan arvoksi sen arvon, joka on suurin pelilaudalla oleva arvo.
        """
        biggest = 0
        for row in range(self.size):
            for column in range(self.size):
                if self.map[row][column] > biggest:
                    biggest = self.map[row][column]

        self.biggest = biggest

    def get_results(self):
        """Luo listan peliin liittyvistä tiedoista tuloslistaa varten: pelaajan nimi,
        pelilaudan koko, siirtojen määrä ja suurimman laatan arvo.

        Returns:
            Lista peliin liittyvistä tiedoista
        """
        return [self.player, str(self.size)+"x"+str(self.size), self.moves, self.biggest]

    def __str__(self):
        """Muodostaa pelilaudasta merkkijonomuotoisen esityksen.

        Returns:
            Merkkijono, joka kuvaa pelilaudan tilaa.
        """
        printed = ""
        for row in self.map:
            printed = printed + str(row) + '\n'

        return printed
