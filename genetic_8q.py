import random

# 产生父代基因
# 基因长度为length, 每个基因位来自geneSet
def generate_parent(geneSet, get_fitness):
    random.shuffle(geneSet) # 随机产生父代基因
    genes = geneSet
    fitness = get_fitness(genes) # 适应度函数
    return Chromosome(genes, fitness) # 返回染色体

# 基因变异，每次交换一对基因位
def mutate(parent, geneSet, get_fitness):
    # 产生随机交换的两个位置
    i, j = random.sample(geneSet, 2)
    # 交换这个位置上的基因
    parent.Genes[i], parent.Genes[j] = parent.Genes[j], parent.Genes[i]
    genes = parent.Genes
    fitness = get_fitness(genes) # 适应度函数
    return Chromosome(genes, fitness) # 返回染色体

# 产生最优个体
# optimalFitness：最佳适应度
def get_best(get_fitness, optimalFitness, geneSet, display):
    Parent = generate_parent(geneSet, get_fitness) # 产生父代基因
    display(Parent) # 输出父代基因的信息

    # 父代基因适应度达到最优适应度时，则返回
    if Parent.Fitness == optimalFitness:
        return Parent

    # 不停地产生下一代，保证下一代的适应度大于上一代
    while True:
        # 变异产生下一代
        child = mutate(Parent, geneSet, get_fitness)

        # 当下一代适应度小于上一代，则跳过本次循环
        if Parent.Fitness <= child.Fitness:
            continue
        display(child) # 输出子代的信息

        # 当子代的适应度达到最优适应度时，返回子代
        if child.Fitness == optimalFitness:
            return child
        Parent = child

# 染色体类，属性为: Genes(基因), Fitness(适应度)
class Chromosome:
    Genes = None
    Fitness = None

    # 初始化染色体类
    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness