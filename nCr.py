#nCr mod p の計算
def ncr(n, r, p):
    num = den = 1 
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p

n, r, p = map(int, input().split())
print(ncr(n, r, p)
# a^n mod p は pow(a, n, p)
