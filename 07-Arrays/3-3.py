arr = [8, 2, 5, 1, 9]
arr2 = [8, 2, 5, 1, 9]

i = 0
while i < len(arr2):
    arr2[i] = (arr[i])**2
    i += 1

print(f'Array: {arr}')
print(f'2nd power: {arr2}')