from Load_Data import load
max_iterations=1000
max_capacity=200
weights,values=load('../Data.txt')
Pmut=0.9
population_size,chormosome_size=700,len(weights)
nbr_parents=50
newgenration_size=20
generations=1000