import numpy as np
import random

def tournament_selection(population,nbr_parents):
    parents = []
    population_size = len(population.individuals)

    for _ in range(nbr_parents):
        contestants_indices = random.sample(range(population_size), 5)  # Select k random indices
        tournament_contestants = [population.individuals[index] for index in contestants_indices]  # Get the candidates
        # calculate their fitnesses
        fitnesses = [candidate.fitness() for candidate in tournament_contestants]
        # select the tournament's winner
        winner = tournament_contestants[np.argmax(fitnesses)]
        parents.append(winner)

    return parents