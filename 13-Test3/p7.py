def f(arr2D):
    result = list(map(lambda col: sum(map(lambda row: row[col], arr2D)), range(len(arr2D[0]))))
    return any(result.count(x) > 1 for x in result)

print(f([[3,4,2],[5,1,6]]))
print(f([[3,4,2],[5,1,7]]))