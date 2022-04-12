import chess
# figure:rook, knight, bishop, pawn, king, queen
#
try:
    figure_name = input(">")
    source = input(">")
    dest = input(">")
    figure = chess.get_figure(figure_name, source)
    figure.next_step(dest)
    print(figure.get_coord()[0]+str(figure.get_coord()[1]))
except chess.BadStep:
    print("No")
except chess.WrongArgument :
    print("Format error")