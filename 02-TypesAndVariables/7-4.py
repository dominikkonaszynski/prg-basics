import math
circumference = float(input('Enter the circumference: '))
can_be_cut = circumference / math.pi >= 50
print(f'Tree can be cut: {can_be_cut}')