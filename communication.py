
#Import Libraries
import chess
import chess.engine

#Import functions
from InitialChecks import InitialChecker

#Initialize Board
board = chess.Board()
print(board)


#Initialize Chess Engine
engine = chess.engine.SimpleEngine.popen_uci(r"stockfish ")
engine.id.get("name")

MoveCounter = 0


while True:

    m = input()
    HumanMove = chess.Move.from_uci(m.strip()) #m strip will be changed by CV
    board.push(HumanMove)
    MoveCounter += 1 #Count After Human Move
    print(board)

    print('////////////')
    limit = chess.engine.Limit(time=2.0)
    result =engine.play(board, limit)  # doctest: +ELLIPSIS
    print(board)
    board.push(result.move)
    data = result.move
    print(type(data))
    print(result.move)
    #####

    board.variation_san([chess.Move.from_uci(m) for m in ["e2e4", "e7e5", "g1f3"]])
    print('////////////')
    print(board)
    MoveCounter += 1 #Count After Robot Move
    if MoveCounter == 4:
        break

print(board.variation_san(result.move))
engine.quit()