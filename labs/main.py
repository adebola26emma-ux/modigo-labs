def is_prime(number):
    # TODO: return True if `number` is prime, False otherwise
    if number < 2:
        return False
    elif number < 4:
        return True
    for i in range(2, int(number**0.5)):
        if number%i==0:
            return False
    return True
print(is_prime(7))
print(is_prime(1))
print(is_prime(10))
print(is_prime(2))
print(is_prime(-5))
print(is_prime(0))