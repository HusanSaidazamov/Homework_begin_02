import math

# Ikkita qarama-qarshi cho'qqi koordinatalari
x1=float(input())
x2=float(input())
y1 = float(input())
y2 = float(input())

# Tomonlar uzunligini hisoblash
uzunlik = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Enni tomonlar orasidagi masofa bilan o'lchash
masofa = abs(x2 - x1)

# Perimetri hisoblash
perimetri = 2 * (uzunlik + masofa)

# Maydoni hisoblash
maydoni = uzunlik * masofa

print("Perimetri:", perimetri)
print("Maydoni:", maydoni)