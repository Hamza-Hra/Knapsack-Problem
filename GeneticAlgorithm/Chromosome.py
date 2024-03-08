import numpy as np
import random
from Globals import weights,values,max_capacity,Pmut
class Chromosome:
    weights=weights
    values=values
    def __init__(self,genes):
        self.genes=genes
    def create_copy(self):
        return Chromosome(list(self.genes))
    def fitness(self,capacity=max_capacity):
        weight=np.sum(np.array(self.genes)*np.array(self.weights))
        if weight>capacity:
            f=0
            return f
        else:
            f=np.sum(np.array(self.genes)*np.array(self.values))
            return f
    def permute(self):
        new_chromosome=self.create_copy()
        index=random.choice(range(0,len(new_chromosome.genes)))
        if new_chromosome.genes[index]==1:
            new_chromosome.genes[index]=0
        else:
            new_chromosome.genes[index] = 1
        return new_chromosome


    def mutate(self, Pmut=Pmut):
        p = random.uniform(0, 1)
        if p <= Pmut:
            newoffspring=self.permute()
            return newoffspring
        else:
            return self




