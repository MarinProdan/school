

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_prime():
    prime = []
    cislo = 2
    while len(prime) < 20:
        if is_prime_number(cislo):
            prime.append(cislo)
        cislo += 1
    return prime

lop=is_prime()
print(lop)
