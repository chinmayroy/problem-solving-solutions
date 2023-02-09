import itertools

c = input().split()
string, number = sorted(c[0]), int(c[1])
print(*list(map(''.join, itertools.permutations(string, number))), sep='\n')
