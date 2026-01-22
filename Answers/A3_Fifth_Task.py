def mod_pow(a, n, m):
    result = 1
    a %= m
    while n > 0:
        if n % 2 == 1:
            result = result * a % m
        a = a * a % m
        n //= 2
    return result

def mod_sum(a, n, m):
    if n == 0:
        return 0
    if n == 1:
        return a % m
    if n % 2 == 0:
        half = mod_sum(a, n // 2, m)
        return (half + mod_pow(a, n // 2, m) * half % m) % m
    else:
        return (mod_sum(a, n - 1, m) + mod_pow(a, n, m)) % m

T = int(input())
for _ in range(T):
    a, n, m = map(int, input().split())
    print(mod_sum(a, n, m))