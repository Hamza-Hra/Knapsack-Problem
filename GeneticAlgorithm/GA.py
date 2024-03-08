from GeneticAlgorithm.Globals import *
from Population import Population
from TournamentSelection import tournament_selection
from Crossover import crossover
from GeneticAlgorithm.Chromosome import Chromosome
def genetic_algorithm(generations):
    population=Population(population_size,chormosome_size)
    k=1

    while k<=generations:
        selected_parents=tournament_selection(population,nbr_parents)
        offsprings = []
        for i in range(0, len(selected_parents), 2):
            # get selected parents in pairs
            child1,child2=crossover(selected_parents[i],selected_parents[i+1])
            child1=child1.mutate()
            child2=child2.mutate()
            offsprings.extend([child1, child2])
        # Get the genetic material and calculate fitnesses
        fitnesses=[offspring.fitness() for offspring in offsprings]
        genomes=[offspring.genes for offspring in offsprings]
        offsprings_info = sorted(zip(fitnesses, genomes), key=lambda x: x[0])
        genomes=[offspring_info[1] for offspring_info in offsprings_info]
        genomes=genomes[:newgenration_size]
        new_generation=[ Chromosome(genes) for genes in genomes]
        population.update(selected_parents,new_generation)
        k+=1
    best=population.get_best_individual()
    return best




