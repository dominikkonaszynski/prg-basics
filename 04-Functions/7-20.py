def f(number1,number2,number3):
    max_value = max(number1, number2, number3)
    min_value = min(number1, number2, number3)
    difference = max_value - min_value
    return difference

if __name__ == "__main__":
    print(f(7,4,9))
    print(f(2,12,8))