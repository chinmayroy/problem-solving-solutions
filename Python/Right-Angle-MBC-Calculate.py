import math
AB = int(input())
BC = int(input())

H = math.sqrt(AB**2 + BC**2)
H = H/2
adj = BC/2

output = int(round(math.degrees(math.acos(adj/H))))

output = str(output)
print(output+ u"\N{DEGREE SIGN}")
