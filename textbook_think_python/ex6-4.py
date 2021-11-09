def is_power(a, b):
    if a == b:
        return True
    elif a % b == 0:
        return is_power(a/b, b)
    else:
        return False
    
print(is_power(2, 100))
print(is_power(3, 99))
print(is_power(13, 15231))
print(is_power(1, 141))
print(is_power(2, 3))
print(is_power(12, 12))
print(is_power(5, 55))
    