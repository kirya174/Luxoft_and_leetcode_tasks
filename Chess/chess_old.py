class Chessboard:
    """Class for storing current location of Pieces on board"""

    def __init__(self):
        """Create empty board"""
        self.board = [[0 for x in range(8)] for y in range(8)]

    def __getitem__(self, key):
        return self.board[key]

    def add_to_board(self, x, y):
        self.board[x - 1][y - 1] = 1

    def remove_from_board(self, x, y):
        self.board[x - 1][y - 1] = 0

    def print_board(self):
        for row in self.board:
            print(row)


class Piece:
    """Super class for Pieces on Board"""

    def __init__(self, board, x, y):
        """Initial position of an element on the board"""
        self.x = x
        self.y = y
        self.board = board
        self.board.add_to_board(x, y)

    def step(self, x_new, y_new):
        """Defines how an element can be moved on a board"""
        pass

    def can_move(self, x, y) -> bool:
        """Check if selected coordinates are inside the board and not reserved by another element"""
        return 1 <= x <= 8 and 1 <= y <= 8 and self.board[x - 1][y - 1] == 0


class Pawn(Piece):
    """Logic for Pawn's movements"""
    Piece_type = "Pawn"

    def __init__(self, board, x, y, color):
        super().__init__(board, x, y)
        self.color = color
        print(f"Current coordinates for {self.Piece_type} are {self.x}:{self.y}")

    def step(self, x_new, y_new):
        """Can only move straight up or down depending on the color"""
        if super().can_move(x_new, y_new):
            if self.x == x_new and \
                    ((y_new > self.y and self.color == "white") or (y_new < self.y and self.color == "black")) and \
                    (((self.y == 2 or self.y == 7) and abs(y_new - self.y) <= 2) or (abs(y_new - self.y) == 1)):
                self.board.remove_from_board(self.x, self.y)
                self.y = y_new
                self.board.add_to_board(self.x, self.y)
                print(f'New coordinates for {self.Piece_type} are {self.x}:{self.y}')
                return
        print("Incorrect coordinates")


class King(Piece):
    """Logic for King's movements"""
    Piece_type = "King"

    def __init__(self, board, x, y):
        super().__init__(board, x, y)
        print(f"Current coordinates for {self.Piece_type} are {self.x}:{self.y}")

    def step(self, x_new, y_new):
        """Can move for 1 cell in any direction"""
        if super().can_move(x_new, y_new):
            if abs(x_new - self.x) <= 1 and abs(y_new - self.y) <= 1:
                self.board.remove_from_board(self.x, self.y, False)
                self.x = x_new
                self.y = y_new
                self.board.add_to_board(self.x, self.y, True)
                print(f'New coordinates for {self.Piece_type} are {self.x}:{self.y}')
                return
        print("Incorrect coordinates")


class Queen(Piece):
    """Logic for Queen's movements"""
    Piece_type = "Queen"

    def __init__(self, board, x, y):
        super().__init__(board, x, y)
        print(f"Current coordinates for {self.Piece_type} are {self.x}:{self.y}")

    def step(self, x_new, y_new):
        """Can move in any direction by any number of cells"""
        if super().can_move(x_new, y_new):
            if abs(x_new - self.x) == abs(y_new - self.y):
                self.board.remove_from_board(self.x, self.y, False)
                self.x = x_new
                self.y = y_new
                self.board.add_to_board(self.x, self.y, True)
                print(f'New coordinates for {self.Piece_type} are {self.x}:{self.y}')
                return
        print("Incorrect coordinates")


class Rook(Piece):
    """Logic for Rook's movements"""
    Piece_type = "Rook"

    def __init__(self, board, x, y):
        super().__init__(board, x, y)
        print(f"Current coordinates for {self.Piece_type} are {self.x}:{self.y}")

    def step(self, x_new, y_new):
        """Can move up, down, left or right by any number of cells"""
        if super().can_move(x_new, y_new):
            if x_new == self.x or y_new == self.y:
                self.board.remove_from_board(self.x, self.y, False)
                self.x = x_new
                self.y = y_new
                self.board.add_to_board(self.x, self.y, True)
                print(f'New coordinates for {self.Piece_type} are {self.x}:{self.y}')
                return
        print("Incorrect coordinates")


class Bishop(Piece):
    """Logic for Bishop's movements"""
    Piece_type = "Bishop"

    def __init__(self, board, x, y):
        super().__init__(board, x, y)
        print(f"Current coordinates for {self.Piece_type} are {self.x}:{self.y}")

    def step(self, x_new, y_new):
        """Can move diagonally by any number of cells"""
        if super().can_move(x_new, y_new):
            if abs(x_new - self.x) == abs(y_new - self.y):
                self.board.remove_from_board(self.x, self.y, False)
                self.x = x_new
                self.y = y_new
                self.board.add_to_board(self.x, self.y, True)
                print(f'New coordinates for {self.Piece_type} are {self.x}:{self.y}')
                return
        print("Incorrect coordinates")


class Knight(Piece):
    """Logic for Knight's movements"""
    Piece_type = "Knight"

    def __init__(self, board, x, y):
        super().__init__(board, x, y)
        print(f"Current coordinates for {self.Piece_type} are {self.x}:{self.y}")

    def step(self, x_new, y_new):
        """The move forms an "L"-shape: two squares vertically and one square horizontally,
        or two squares horizontally and one square vertically"""
        if super().can_move(x_new, y_new):
            if abs(x_new - self.x) == 2 and abs(y_new - self.y) == 1 or \
                    abs(x_new - self.x) == 1 and abs(y_new - self.y) == 2:
                self.board.remove_from_board(self.x, self.y, False)
                self.x = x_new
                self.y = y_new
                self.board.add_to_board(self.x, self.y, True)
                print(f'New coordinates for {self.Piece_type} are {self.x}:{self.y}')
                return
        print("Incorrect coordinates")


new_board = Chessboard()

new_pawn = Pawn(new_board, 2, 2, "white")
new_pawn.step(2, 4)
new_pawn.step(int(input("Input X coordinate between 1 and 8: ")), int(input("Input Y coordinate between 2 and 8: ")))
new_king = King(new_board, 3, 3)

new_board.print_board()
