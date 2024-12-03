#uloha 1 a 2 rovnou
import time


while True:
    try:
        Aprim = int(input("Hledame prvocisla, start v: "))
        Bprim = int(input("konec v: "))
        if Aprim < 0 or Bprim < 0:
            print("jen kladna cisla pls.")
        elif Aprim > Bprim:
            print("popletl jsi zacatek a konec, nechce se mi premyslet nad hanojskejma vezma uz.")
        else:
            break
    except ValueError:
        print("Nebud dement, cela, kladna cisla.")

#mereni casu aka dekorator
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        return result, elapsed_time
    return wrapper

#nalezeni prvosicel, s merenim casu
@measure_time
def find_primes(start, end):
    primes = []
    for num in range(max(2, start), end + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# prehledny vypis, pomoci ai
def print_primes(prime_numbers):
    print(f"Prvočísla v rozsahu {Aprim} až {Bprim}:")
    for i in range(0, len(prime_numbers), 10):
        print(", ".join(map(str, prime_numbers[i:i+10])))

# jedeme
prime_numbers, elapsed_time = find_primes(Aprim, Bprim)
print_primes(prime_numbers)
print(f"Time taken: {elapsed_time:.6f} seconds")
