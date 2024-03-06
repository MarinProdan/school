def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

# Získání vstupu od uživatele
num = int(input("Zadejte celé číslo: "))

# Zavolání funkce is_prime() a výpis výsledku
if is_prime(num):
    print(f"{num} je prvočíslo.")
else:
    print("{num} není prvočíslo.")
