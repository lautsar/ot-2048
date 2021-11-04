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
    
    def __str__(self):
        printed = ""
        for row in self.map:
            printed = printed + str(row) + '\n'

        return printed