
def local_search(solution,max_iterations):
    sbest=solution.create_copy()
    fbest=sbest.fitness()
    i=0
    for i in range(max_iterations):
        s1=sbest.permute()
        f1=s1.fitness()
        if f1>fbest:
            sbest=s1
            fbest=f1
    return sbest,fbest


