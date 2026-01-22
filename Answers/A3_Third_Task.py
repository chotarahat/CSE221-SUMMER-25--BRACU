def fast_power(a, b, mod):
    result = 1
    a = a % mod
    while b > 0:
        if b % 2 !=0:
            result = (result * a) % mod
        a = (a * a) % mod
        b //= 2
    return result
a, b = map(int, input().split())
mod = 107
print(fast_power(a, b, mod))