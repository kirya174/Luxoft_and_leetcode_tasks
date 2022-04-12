def get_figure(name, source):
    match name:
        case "rook":
            return Rook(source)
        case "knight":
            return Knight(source)
        case "bishop":
            return Bishop(source)
        case "pawn":
            return Pawn(source)
        case "king":
            return King(source)
        case "queen":
            return Queen(source)
        case _:
            raise WrongArgument


class WrongArgument(Exception):
    """Raised when wrong arguments provided"""
    pass


class BadStep(Exception):
    """Raised when piece can't move to provided destination"""
    pass


class Piece:
    """Super class for Pieces on Board"""
    __slots__ = ["x", "y"]
    coordinates = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}

    def __init__(self, source_coordinate):
        """Initial position of an element on the board"""
        self.x, self.y = self.convert_coords_to_nums(source_coordinate)
        self.can_move(self.x, self.y)

    def next_step(self, destination):
        """Defines how an element can be moved on a board"""
        new_x, new_y = self.convert_coords_to_nums(destination)
        self.can_move(new_x, new_y)

    def get_coord(self):
        """Returns current coordinates of piece in format (A-H)(1-8)"""
        x_coord = ""
        for char, num in Piece.coordinates.items():
            if num == self.x:
                x_coord = char
                break
        y_coord = self.y

        current_coordinate = x_coord + str(y_coord)

        return current_coordinate

    @staticmethod
    def can_move(x, y):
        """Check if selected coordinates are inside the board"""
        if not (1 <= x <= 8 and 1 <= y <= 8):
            raise BadStep

    @staticmethod
    def convert_coords_to_nums(coords):
        x = Piece.coordinates[coords[0]]
        y = int(coords[1])
        return x, y


class Rook(Piece):
    __slots__ = super().__slots__

    def __init__(self, source_coordinate):
        super().__init__(source_coordinate)

    def next_step(self, destination):
        """Can move up, down, left or right by any number of cells"""
        x_new, y_new = super().convert_coords_to_nums(destination)
        super().can_move(x_new, y_new)
        if x_new == self.x or y_new == self.y:
            self.x = x_new
            self.y = y_new
        else:
            raise BadStep


class Knight(Piece):
    __slots__ = super().__slots__

    def __init__(self, source_coordinate):
        super().__init__(source_coordinate)

    def next_step(self, destination):
        """The move forms an "L"-shape: two squares vertically and one square horizontally,
        or two squares horizontally and one square vertically"""
        x_new, y_new = super().convert_coords_to_nums(destination)
        super().can_move(x_new, y_new)
        if abs(x_new - self.x) == 2 and abs(y_new - self.y) == 1 or \
                abs(x_new - self.x) == 1 and abs(y_new - self.y) == 2:
            self.x = x_new
            self.y = y_new
        else:
            raise BadStep


class Bishop(Piece):
    __slots__ = super().__slots__

    def __init__(self, source_coordinate):
        super().__init__(source_coordinate)

    def next_step(self, destination):
        """Can move diagonally by any number of cells"""
        x_new, y_new = super().convert_coords_to_nums(destination)
        super().can_move(x_new, y_new)
        if abs(x_new - self.x) == abs(y_new - self.y):
            self.x = x_new
            self.y = y_new
        else:
            raise BadStep


class Pawn(Piece):
    __slots__ = super().__slots__

    def __init__(self, source_coordinate):
        super().__init__(source_coordinate)

    def next_step(self, destination):
        """Can only move straight up for 1 or 2 cells"""
        x_new, y_new = super().convert_coords_to_nums(destination)
        super().can_move(x_new, y_new)
        if self.x == x_new and ((self.y == 2 and 0 < y_new - self.y <= 2)
                                or (y_new - self.y == 1)):
            self.y = y_new
        else:
            raise BadStep


class King(Piece):
    __slots__ = super().__slots__

    def __init__(self, source_coordinate):
        super().__init__(source_coordinate)

    def next_step(self, destination):
        """Can move for 1 cell in any direction"""
        x_new, y_new = super().convert_coords_to_nums(destination)
        super().can_move(x_new, y_new)
        if abs(x_new - self.x) <= 1 and abs(y_new - self.y) <= 1:
            self.x = x_new
            self.y = y_new
        else:
            raise BadStep


class Queen(Piece):
    __slots__ = super().__slots__

    def __init__(self, source_coordinate):
        super().__init__(source_coordinate)

    def next_step(self, destination):
        """Can move in any direction by any number of cells"""
        x_new, y_new = super().convert_coords_to_nums(destination)
        super().can_move(x_new, y_new)
        if abs(x_new - self.x) == abs(y_new - self.y) or x_new == self.x or y_new == self.y:
            self.x = x_new
            self.y = y_new
        else:
            raise BadStep
