def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False

    return True


primes = []
candidate = 2

while len(primes) < 10:
    if is_prime(candidate):
        primes.append(candidate)
    candidate += 1

print(*primes)