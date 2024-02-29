
from Chromosome import *
from LocalSearch import local_search
from Globals import max_iterations,weights
s0=Chromosome([0]*len(weights))
f0=s0.fitness()
sm,fm=local_search(s0,max_iterations)

print(f"S0={s0.genes}  f0={f0}  Sm={sm.genes}  fm={fm}")