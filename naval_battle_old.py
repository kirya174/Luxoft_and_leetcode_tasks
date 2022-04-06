from itertools import product


class Board:
    coords_dict = {"А": 0, "Б": 1, "В": 2, "Г": 3, "Д": 4, "Е": 5, "Ж": 6, "З": 7, "И": 8, "К": 9}

    def __init__(self, size=10):
        self.size = size
        self.ships = []
        self.board = {y: [] for y in range(0, size)}

    def add_ship(self, start_coordinates: str, end_coordinates=""):
        new_ship = BaseShip(self.convert_coords_from_str_to_dict(start_coordinates + end_coordinates))
        can_add = True
        for x in new_ship.coords.keys():
            if x in self.board[y]:
                print("Coordinates already occupied")
                can_add = False
                break
        if can_add:
            self.ships.append(new_ship)
            for y in new_ship.coords["y"]:
                for x in new_ship.coords["x"]:
                    self.board[y].append(x)

    def hit_ship(self, coordinates: str):
        x_coord = Board.coords_dict[coordinates[0]]
        y_coord = int(coordinates[1]) - 1
        ship_damaged = False
        for ship in self.ships:
            if x_coord in ship.coords["x"] and y_coord in ship.coords["y"]:
                ship.hit_ship_elem(x_coord, y_coord)
                ship_damaged = True
                break
        if ship_damaged:
            print("Ship damaged")
        else:
            print("No ship at this coordinates")

    @staticmethod
    def convert_coords_from_str_to_dict(coordinates: str) -> dict:
        converted_coordinates = {
            "x": [i for i in range(Board.coords_dict[coordinates[0]], Board.coords_dict[coordinates[2]] + 1)],
            "y": [i for i in range(int(coordinates[1]) - 1, int(coordinates[3]))]}
        return converted_coordinates


class BaseShip:
    max_ship_elem_health = 1  # здоровье каждого элемента корабля

    def __init__(self, coordinates: dict):
        # Словарь с координатами корабля
        self.coords = coordinates
        # длина корабля, вычисляемая по координатам
        self.ship_length = (max(self.coords["x"]) - min(self.coords["x"])) + \
                           (max(self.coords["y"]) - min(self.coords["y"])) + 1
        # список с длиной корабля, содержащий здоровье каждого элемента
        self.ship_health = [BaseShip.max_ship_elem_health for _ in range(self.ship_length)]
        # добавление корабль на общую доску

    def change_coord_on_hit(self):
        """Изменение координат при попадании"""
        pass

    def hit_ship_elem(self, x, y):
        """Попадание по элементу корабля"""
        elem_num = x - min(self.coords["x"]) + y - min(self.coords["y"])
        self.ship_health[elem_num] -= 1
        if self.ship_health[elem_num] == 0:
            print("Ship element destroyed")
        if sum(self.ship_health) == 0:
            print("Ship destroyed")


game_board = Board()
game_board.add_ship("А1Г1")
game_board.add_ship("Б2Г2")
while True:
    game_board.hit_ship(input())
# ship2 = BaseShip()
# ship3 = BaseShip()
# ship4 = BaseShip()
