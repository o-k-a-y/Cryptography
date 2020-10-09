def xgcd(a, b):
    prevx, x = 1, 0;  prevy, y = 0, 1
    while b:
        q = a/b
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        a, b = b, a % b
    return int(a), int(prevx), int(prevy)

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

print(modinv(5, 11))
print(modinv(55, 2953))