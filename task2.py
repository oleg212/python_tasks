import math

def is_prime(n):
    if n <= 1:
        return False
    up = int(math.sqrt(n)) + 1
    for i in range(2, up):
        if n % i == 0:
            return False
    return True

def find_nth_prime_number(n):
    count = 0
    number = 2
    while count < n:
        if is_prime(number):
            count += 1
        number += 1
    return number - 1
print("Введите N:")
n = int(input())
nth_prime = find_nth_prime_number(n)
print("N-ое простое число:", nth_prime)