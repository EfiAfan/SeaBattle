
def recalculate_weight_map(self, available_ships):

    self.weight = [[1 for _ in range(self.size)] for _ in range(self.size)]


    for x in range(self.size):
        for y in range(self.size):
            if self.radar[x][y] == Cell.damaged_ship:

                self.weight[x][y] = 0

                if x - 1 >= 0:
                    if y - 1 >= 0:
                        self.weight[x - 1][y - 1] = 0
                    self.weight[x - 1][y] *= 50
                    if y + 1 < self.size:
                        self.weight[x - 1][y + 1] = 0

                if y - 1 >= 0:
                    self.weight[x][y - 1] *= 50
                if y + 1 < self.size:
                    self.weight[x][y + 1] *= 50

                if x + 1 < self.size:
                    if y - 1 >= 0:
                        self.weight[x + 1][y - 1] = 0
                    self.weight[x + 1][y] *= 50
                    if y + 1 < self.size:
                        self.weight[x + 1][y + 1] = 0


    for ship_size in available_ships:

        ship = Ship(ship_size, 1, 1, 0)

        for x in range(self.size):
            for y in range(self.size):
                if self.radar[x][y] in (Cell.destroyed_ship, Cell.damaged_ship, Cell.miss_cell) \
                        or self.weight[x][y] == 0:
                    self.weight[x][y] = 0
                    continue
                for rotation in range(0, 4):
                    ship.set_position(x, y, rotation)
                    if self.check_ship_fits(ship, FieldPart.radar):
                        self.weight[x][y] += 1