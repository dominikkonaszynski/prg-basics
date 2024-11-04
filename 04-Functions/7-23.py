def f(expression):
    total = 0
    current_number = ''
    operation = '+'

    for char in expression:
        if char.isdigit():
            current_number += char
        else:
            total += int(current_number) if operation == '+' else -int(current_number)
            current_number = ''
            operation = char

    total += int(current_number) if operation == '+' else -int(current_number)

    return total

if __name__ == "__main__":
    print(f("2+3"))         
    print(f("3+8+1"))       
    print(f("2+3-4+5-0"))  
