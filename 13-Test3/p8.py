def f(n):
    odd_digits = list(filter(lambda x: int(x) % 2 != 0, str(n)))
    if not odd_digits:
        return -1
    
    odd_digits = list(map(int, odd_digits))

    return max(odd_digits) - min(odd_digits)

print(f(10852))