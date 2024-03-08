import random
from GeneticAlgorithm.Chromosome import Chromosome
def crossover(parent1,parent2):

    index1,index2=random.sample(range(1,len(parent1.genes)-1),k=2)
    start,end=sorted([index1,index2])
    genes1=parent1.genes[:start]+parent2.genes[start:end]+parent1.genes[end:]
    genes2=parent2.genes[:start]+parent1.genes[start:end]+parent2.genes[end:]
    child1=Chromosome(genes=genes1)
    child2=Chromosome(genes=genes2)
    return child1,child2