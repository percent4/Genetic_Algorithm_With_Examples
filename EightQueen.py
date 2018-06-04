import datetime
import genetic_8q

# 定义八皇后问题的适应度函数
# 适应度函数为： 4*size-rowsWithQueens-colsWithQueens
#                    -northEastDiagonalsWithQueens
#                    -southEastDiagonalsWithQueens
# rowsWithQueens: 皇后所在的行的集合
# colsWithQueens: 皇后所在的列的集合
# northEastDiagonalsWithQueens：皇后所在的副对角线的集合
# southEastDiagonalsWithQueens：皇后所在的主对角线的集合
def get_fitness(genes, size):
    # 定义棋盘
    board = Board(genes, size)
    rowsWithQueens = set()
    colsWithQueens = set()
    northEastDiagonalsWithQueens = set()
    southEastDiagonalsWithQueens = set()
    for row in range(size):
        for col in range(size):
            # 当某个位置为皇后时
            if board.get(row, col) == 'Q':
                rowsWithQueens.add(row)
                colsWithQueens.add(col)
                northEastDiagonalsWithQueens.add(row+col)
                southEastDiagonalsWithQueens.add(size-1-row+col)
    # total为适应度
    total =   size - len(rowsWithQueens) \
            + size - len(colsWithQueens) \
            + size - len(northEastDiagonalsWithQueens) \
            + size - len(southEastDiagonalsWithQueens)
    return total

# 输出棋盘信息， 适应度， 消耗时间
def display(candidate, startTime, size):
    timeDiff = datetime.datetime.now() - startTime
    board = Board(candidate.Genes, size)
    board.print()
    print("%s\t- %s\t%s"%(candidate.Genes, candidate.Fitness, timeDiff))

# 定义棋盘类，参数为genes, size
class Board:
    # 棋盘初始化
    def __init__(self, genes, size):
        board = [['.']*size for _ in range(size)]
        for index in range(size):
            row = index
            column = genes[index]
            board[row][column] = 'Q'
        self._board = board

    # 获取位置为(row, column)的棋子
    def get(self, row, column):
        return self._board[column][row]

    # 输出棋盘
    def print(self):
        # 0,0 prints in bottom left corner
        for i in range(len(self._board)):
            print(' '.join(self._board[i]))

# 主函数，用来测试
def main():
    size = 8 # 棋盘的尺寸
    geneset = list(range(size)) # 基因库
    startTime = datetime.datetime.now() # 开始时间

    # 输出函数
    def fnDisplay(candidate):
        display(candidate, startTime, size)

    # 适应度函数
    def fnGetFitness(genes):
        return get_fitness(genes, size)

    # 最佳适应度为0， 即该问题的解的适应度
    optimalFitness = 0
    genetic_8q.get_best(fnGetFitness, optimalFitness, geneset, fnDisplay)

main()