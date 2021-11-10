def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(30, 24))
print(gcd(24, 30))
print(gcd(20, 155))
print(gcd(100000, 5524312))