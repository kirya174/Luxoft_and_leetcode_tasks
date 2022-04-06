class Board:
    alphabet = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ"

    def __init__(self, size=10):
        self.size = size
        self.ships = []
        self.board = {x: [] for x in Board.alphabet[:size]}

    def add_ship(self, start_coordinates: str, end_coordinates=""):
        ''' Добавление нового корабля на доску '''
        ship = BaseShip(self.convert_coords_from_str_to_dict(start_coordinates + end_coordinates))
        can_add = True
        for x in ship.coords.keys():
            for y in ship.coords[x]:
                if y in self.board[x]:
                    print("Coordinates already occupied")
                    can_add = False
                    break
            if not can_add:  # выход из цикла x, если координаты заняты
                break

        if can_add:
            # добавление объекта ship в список кораблей
            self.ships.append(ship)
            # добавление координат корабля для отслеживания уже занятых координат на доске
            for x, y in ship.coords.items():
                self.board[x].extend(y)

    def hit_ship(self, coordinates: str):
        ''' атака по кораблю '''
        x_coord = coordinates[0]
        y_coord = int(coordinates[1])
        ship_damaged = False
        # проверка есть ли корабли по таким координатам, если да, то вызов hit_ship_elem для данного корабля
        for ship in self.ships:
            if x_coord in ship.coords.keys() and y_coord in ship.coords[x_coord]:
                ship.hit_ship_elem(x_coord, y_coord)
                ship_damaged = True
                break
        if not ship_damaged:
            print("No ship damaged")

    @staticmethod
    def convert_coords_from_str_to_dict(coordinates: str) -> dict:
        ''' Преобразование координат в формат словаря {буква: [цифра] } '''
        if len(coordinates) == 2:
            return {coordinates[0]: [int(coordinates[1])]}
        elif len(coordinates) == 4:
            start_pos_x = Board.alphabet.find(coordinates[0])
            end_pos_x = Board.alphabet.find(coordinates[2])
            start_pos_y = int(coordinates[1])
            end_pos_y = int(coordinates[3])
            converted_coordinates = {}
            for x in range(start_pos_x, end_pos_x + 1):
                for y in range(start_pos_y, end_pos_y + 1):
                    if Board.alphabet[x] in converted_coordinates.keys():
                        converted_coordinates[Board.alphabet[x]].append(y)
                    else:
                        converted_coordinates[Board.alphabet[x]] = [y]
            return converted_coordinates
        else:
            raise ValueError  # todo error type

    def print_board(self):
        # todo
        print("", end="\t")
        for key in self.board.keys():
            print(key, end="\t")
        print()
        for i in range(self.size):
            print(i + 1, end='\t')
            for j in range(1, self.size + 1):
                if j in self.board[Board.alphabet[i]]:
                    print('\u25A1', end='\t')
                else:
                    print(' ', end='\t')
            print()

        # print('\u25A1') # □
        # print('\u25A3') # ▣
        # print('\u25CF') # ●


class BaseShip:
    max_ship_elem_health = 1  # здоровье каждого элемента корабля

    def __init__(self, coordinates: dict):
        # Словарь с координатами корабля
        self.coords = coordinates
        self.ship_length = len(self.coords.values())
        # список, содержащий здоровье каждого элемента корабля
        self.ship_health = dict()
        for key in self.coords.keys():
            for i in range(len(self.coords[key])):
                self.ship_health[key + str(self.coords[key][i])] = BaseShip.max_ship_elem_health
        # флаг, что корабль жив
        self.alive = True

    def change_coord_on_hit(self):
        """Изменение координат при попадании"""
        pass

    def hit_ship_elem(self, x, y):
        """Попадание по элементу корабля"""
        print("Ship damaged")
        elem = x + str(y)
        self.ship_health[elem] -= 1
        if self.ship_health[elem] == 0:
            print("Ship element destroyed")
        if sum(self.ship_health.values()) == 0:
            self.alive = False
            print("Ship destroyed")


game_board = Board()
game_board.add_ship("А2", "А4")
game_board.add_ship("А1", "Г1")
game_board.add_ship("И1")
game_board.add_ship("Б2Г2")
while True:
    game_board.hit_ship(input())
