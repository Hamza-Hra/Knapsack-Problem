import random
from GeneticAlgorithm.Chromosome import Chromosome
import numpy as np
class Population:
    def __init__(self,population_size,chromosome_size):
        genomes=[random.choices([0,1], k=chromosome_size) for _ in range(population_size)]
        self.individuals=[Chromosome(genes) for genes in genomes]
    def update(self,selected_parents,new_offsprings):
        self.individuals=selected_parents+new_offsprings
    def get_best_individual(self):
        fitnesses=[individual.fitness() for individual in self.individuals]
        best=self.individuals[np.argmax(fitnesses)]
        return best


