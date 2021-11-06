import random

class Game:
    def __init__(self, size):
        self.size = size
        self.map = []
        self.initialize_map()

    def initialize_map(self):
        new_map = []
        for row in range(self.size):
            new_map.append([])

            for column in range(self.size):
                new_map[row].append(0)

        self.map = new_map

        drawn_tiles = 0

        while drawn_tiles < 3:
            if self.new_tile() is True:
                drawn_tiles = drawn_tiles + 1

    def new_tile(self):
        empty_tiles = self.empty_tiles()

        if len(empty_tiles) == 0:
            return False

        drawn = random.randint(0, len(empty_tiles) - 1)

        y = empty_tiles[drawn][0]
        x = empty_tiles[drawn][1]

        self.map[y][x] = 2
        return True

    def empty_tiles(self):
        empty = []
        for column in range(self.size):
            for row in range(self.size):
                if self.map[row][column] == 0:
                    empty.append((row, column))

        return empty

    def swap_tiles(self, from_x, from_y, to_x, to_y):
        from_tile = self.map[from_y][from_x]
        to_tile = self.map[to_y][to_x]

        if from_tile == 0:
            return False

        if to_tile == 0:
            self.map[to_y][to_x] = from_tile
            self.map[from_y][from_x] = 0
            return True
        elif from_tile == to_tile:
            self.map[to_y][to_x] = from_tile + to_tile
            self.map[from_y][from_x] = 0
            return True

    def move_left(self):
        legal_move = False
        for row in range(self.size):
            for column in range(self.size - 1):
                for column in range(self.size - 1):
                    if self.swap_tiles(column+1, row, column, row) is True:
                        legal_move = True

    def move_right(self):
        legal_move = False
        for row in range(self.size):
            for column in range(self.size - 1):
                for column in range(self.size - 1):
                    if self.swap_tiles(column, row, column + 1, row) is True:
                        legal_move = True

    def move_up(self):
        legal_move = False
        for column in range(self.size):
            for row in range(self.size - 1):
                for row in range(self.size - 1):
                    if self.swap_tiles(column, row + 1, column, row) is True:
                        legal_move = True

    def move_down(self):
        legal_move = False
        for column in range(self.size):
            for row in range(self.size - 1):
                for row in range(self.size - 1):
                    if self.swap_tiles(column, row, column, row + 1) is True:
                        legal_move = True

    def __str__(self):
        printed = ""
        for row in self.map:
            printed = printed + str(row) + '\n'

        return printed