arr = [15, 8, 31, 47, 2, 19]
rev_arr = [15, 8, 31, 47, 2, 19] 

i = 0
while i < len(rev_arr):
    rev_arr[i] = arr[-(i+1)]
    i += 1

print(f'existed array: {arr}')
print(f'reverse array: {rev_arr}')