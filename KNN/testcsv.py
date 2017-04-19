from operator import itemgetter
a = [(1,6),(2,5),(3,4)]

b = sorted(a, key = itemgetter(1))
print(b)



