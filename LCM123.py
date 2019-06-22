import math
z,j2=input().split()
z=int(z)
j2=int(j2)
z3=(math.gcd(z,j2))
print((z*j2)//z3)
