def f(array2D):
    for i in range(len(array2D)):
        row_sum = sum(array2D[i])
        col_sum = sum(array2D[j][i] for j in range(len(array2D)))
        if row_sum == col_sum:
            return True
        else:
            return False

if __name__ == "__main__": 
    print(f([[3,7,2],[4,2,5],[5,2,1]]))
    print(f([[3,7,2],[4,2,5],[9,2,1]]))