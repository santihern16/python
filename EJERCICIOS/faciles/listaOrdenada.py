def is_sorted(lista):
    return lista == sorted(lista)

#test
print(is_sorted([1,2,3,4,6,7]))
print(is_sorted([2,6,4,7,1,0]))