def f(n):
    count = 0
    current = 1  # Start checking from the number 1

    while count < n:
        current += 1  # Check the next number
        is_prime = True  # Assume current is prime

        # Check if current is prime
        for i in range(2, int(current**0.5) + 1):
            if current % i == 0:
                is_prime = False  # Found a divisor, so it's not prime
                break
        
        if is_prime:
            count += 1  # Found a prime number

    return current

if __name__ == "__main__":
    print(f(1))  # Should return 2
    print(f(5))  # Should return 11
    print(f(10)) # Should return 29
