import datetime
import genetic
import random

# 基因库
geneSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !.,"

# 适应度函数, 猜测字符串guess与目标字符串target的重合字符的个数
def get_fitness(guess, target):
    return sum([1 for expected, actual in zip(target, guess) if expected == actual])

# 输出候选者的信息： Genes(基因), Fitness(适应度), timeDiff(时间差)
def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{0}\t{1}\t{2}".format(candidate.Genes, candidate.Fitness, str(timeDiff)))

# 猜单词函数
def guess_password(target):
    # 开始时间
    startTime = datetime.datetime.now()

    # 适应度函数
    def fnGetFitness(genes):
        return get_fitness(genes, target)

    # 输出信息函数
    def fnDisplay(candidate):
        display(candidate, startTime)

    # 最佳适应度设置为目标字符串的长度
    optimalFitness = len(target)
    # 得到最优个体，即使得猜测字符串等于目标字符串
    genetic.get_best(fnGetFitness, len(target), optimalFitness, geneSet, fnDisplay)

# 测试'Hello world!'字符串
def test_Hello_Word():
    target = 'Hello World!'
    guess_password(target)

# 测试'For I am fearfully and wonderfully made.'字符串
def test_for_I_am_fearlly_and_wonderfully_made():
    target = "For I am fearfully and wonderfully made."
    guess_password(target)

# 测试随机组成的长度为150的字符串
def test_Random():
    length = 150
    target = ''.join(random.choice(geneSet) for _ in range(length))
    guess_password(target)

# 主函数
def main():
    test_Hello_Word()
    test_for_I_am_fearlly_and_wonderfully_made()
    test_Random()

main()