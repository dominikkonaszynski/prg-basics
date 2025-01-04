def f(x,y,digit):
    digit = str(digit)
    counts = sum(map(lambda number: str(number).count(digit), range(x, y + 1)))
    return counts

print(f(10,15,1))
