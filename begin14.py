import math

def find_s_and_l(r):
    l = 2 * math.pi * r
    s = math.pi * r**2
    return l, s

R = float(input("Aylana radiusini kiriting: "))

L, S = find_s_and_l(R)

print("L =", L)
print("S =", S)