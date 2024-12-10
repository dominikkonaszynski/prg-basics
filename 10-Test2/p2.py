def f(arr):
    if arr[0] == arr[1]:
        majority = arr[0]
    elif arr[0] == arr[2]:
        majority = arr[0]
    else:
        majority = arr[1]

    for i in range(len(arr)):
        if arr[i] != majority:
            return arr[i]
        
if __name__ == "__main__":
    print(f([7,7,7,7,7,5,7,7]))
    print(f([1,1,1,2,1]))   
    print(f([3,3,3,3,5,3]))