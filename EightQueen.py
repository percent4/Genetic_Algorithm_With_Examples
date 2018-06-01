import datetime
import genetic_8q

def get_fitness(genes, size):
    board = Board(genes, size)
    rowsWithQueens = set()
    colsWithQueens = set()
    northEastDiagonalsWithQueens = set()
    southEastDiagonalsWithQueens = set()
    for row in range(size):
        for col in range(size):
            if board.get(row, col) == 'Q':
                rowsWithQueens.add(row)
                colsWithQueens.add(col)
                northEastDiagonalsWithQueens.add(row+col)
                southEastDiagonalsWithQueens.add(size-1-row+col)
    total =   size - len(rowsWithQueens) \
            + size - len(colsWithQueens) \
            + size - len(northEastDiagonalsWithQueens) \
            + size - len(southEastDiagonalsWithQueens)
    return total

def display(candidate, startTime, size):
    timeDiff = datetime.datetime.now() - startTime
    board = Board(candidate.Genes, size)
    board.print()
    print("{}\t- {}\t{}".format(' '.join(map(str, candidate.Genes)), candidate.Fitness, timeDiff))

class Board:
    def __init__(self, genes, size):
        board = [['.']*size for _ in range(size)]
        for index in range(len(genes)):
            row = index
            column = genes[index]
            board[row][column] = 'Q'
        self._board = board

    def get(self, row, column):
        return self._board[column][row]

    def print(self):
        # 0,0 prints in bottom left corner
        for i in range(len(self._board)):
            print(' '.join(self._board[i]))

def main():
    size = 8
    geneset = [i for i in range(size)]
    startTime = datetime.datetime.now()

    def fnDisplay(candidate):
        display(candidate, startTime, size)

    def fnGetFitness(genes):
        return get_fitness(genes, size)

    optimalFitness = 0
    genetic_8q.get_best(fnGetFitness, size, optimalFitness, geneset, fnDisplay)

main()