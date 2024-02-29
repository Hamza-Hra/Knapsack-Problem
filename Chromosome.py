import numpy as np
import random
class Chromosome:
    def __init__(self,items):
        n=len(items)
        self.genes=[0]*n
    def fitness(self,weights,values,capacity):
        weight=np.sum(np.array(self.genes)*np.array(weights))
        if weights>capacity:
            f=0
            return f
        else:
            f=np.sum(self.genes*values)
            return f
    def permute(self):
        index=random.choice(range(0,len(self.genes)))
        print(f"i=={index}")
        if self.genes[index]==1:
            self.genes[index]=0
        else:
            self.genes[index] = 1





