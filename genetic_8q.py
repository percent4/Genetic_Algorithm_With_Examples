import random

# 产生父代基因
# 基因长度为length, 每个基因位来自geneSet
def generate_parent(length, geneSet, get_fitness):
    genes = []
    while len(genes) < length:
        sampleSize = min(length-len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))

    fitness = get_fitness(genes) # 适应度函数
    return Chromosome(genes, fitness) # 返回染色体

# 基因变异，每次只变异一个基因位
def mutate(parent, geneSet, get_fitness):
    index = random.randrange(0, len(parent.Genes))
    childGenes = list(parent.Genes)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGene
    genes = childGenes
    while len(set(genes)) != len(genes):
        index = random.randrange(0, len(genes))
        childGenes = list(genes)
        newGene, alternate = random.sample(geneSet, 2)
        childGenes[index] = alternate if newGene == childGenes[index] else newGene
        genes = childGenes
    fitness = get_fitness(genes) # 适应度函数
    return Chromosome(genes, fitness) # 返回染色体

# 产生最优个体
# optimalFitness：最佳适应度
def get_best(get_fitness, targetLen, optimalFitness, geneSet, display):
    Parent = generate_parent(targetLen, geneSet, get_fitness) # 产生父代
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