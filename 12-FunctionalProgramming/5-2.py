from functools import reduce

numbers = [2,4,6,3,7,5]
even = list(filter(lambda values: values % 2 == 0, numbers))
result = reduce(lambda x, y: x + y, even)

print(f"Even numbers from list are: {', '.join(map(str, even))}")
print(f"Sum of these numbers is {result}")