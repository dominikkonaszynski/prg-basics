def f(array):

    min_value = float('inf')
    row_min = -1
    col_min = -1
    
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] < min_value:
                min_value = array[i][j]
                row_min = i
                col_min = j
    
    return row_min == col_min


if __name__ == "__main__":
    print(f([[7,8],[5,3],[9,4]]))
    print(f([[7,8,5,3],[9,4,2,6]]))