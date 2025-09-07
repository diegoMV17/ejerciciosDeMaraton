def sieve_of_eratosthenes(n):
    # Criba de Eratóstenes para encontrar todos los números primos hasta n
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 y 1 no son primos
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes

def count_almost_primes(n):
    primes = sieve_of_eratosthenes(n)
    almost_primes_count = 0
    
    # Recorremos todos los números desde 1 hasta n
    for i in range(2, n + 1):
        prime_factors = 0
        # Contamos cuántos factores primos distintos tiene el número
        for j in range(2, i + 1):
            if primes[j] and i % j == 0:
                prime_factors += 1
            if prime_factors > 2:
                break
        
        if prime_factors == 2:
            almost_primes_count += 1
    
    return almost_primes_count

# Entrada
n = int(input().strip())

# Salida
print(count_almost_primes(n))