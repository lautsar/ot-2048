import random

class Game:
    def __init__(self, size, player="Unknown"):
        self.size = size
        self.player = player
        self.map = []
        self.moves = 0
        self.biggest = 0
        self.initialize_map()

    def initialize_map(self):
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
        biggest = 0
        for row in range(self.size):
            for column in range(self.size):
                if self.map[row][column] > biggest:
                    biggest = self.map[row][column]

        self.biggest = biggest

    def get_results(self):
        print(f"Player {self.player} made {self.moves} moves in {self.size}x{self.size} grid, biggest {self.biggest}")
        return [self.player, str(self.size)+"x"+str(self.size), self.moves, self.biggest]

    def __str__(self):
        printed = ""
        for row in self.map:
            printed = printed + str(row) + '\n'

        return printed
