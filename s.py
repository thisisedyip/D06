import itertools

def nested_sum():
    t = [[1,2,3],[4,5,6],[7],[8,9]]
    oneDarray = list(itertools.chain(*t))
    print(oneDarray)
    print(sum(oneDarray))


nested_sum()