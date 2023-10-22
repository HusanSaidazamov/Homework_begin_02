import math

def find_s3(r1, r2):
    s1 = math.pi * r1**2
    s2 = math.pi * r2**2
    s3 = s1 - s2
    return s3

R1 = float(input("Birinchi doira radiusini kiriting: "))
R2 = float(input("Ikkinchi doira radiusini kiriting: "))

S3 = find_s3(R1, R2)

print("S3 =", S3)