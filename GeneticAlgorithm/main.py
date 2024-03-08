from GeneticAlgorithm.Globals import generations
from GA import genetic_algorithm

best=genetic_algorithm(generations)
print(f' the best solution found: {best.genes} with a cost function: {best.fitness()}')




