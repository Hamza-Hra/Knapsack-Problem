

def load(file):
    weights=[]
    values=[]
    try:
        with open(file,'r') as f:
            for line in f:
                _,weight,value=line.split()
                weights.append(int(weight))
                values.append(int(value))
    except Exception as e:
        print(e)
    return weights,values
