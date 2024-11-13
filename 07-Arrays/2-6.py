square_matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for i in range(len(square_matrix)):
    square_matrix[i][i] = 1

for row in square_matrix:
    for number in row:
        print(number, end =" ")
    print()