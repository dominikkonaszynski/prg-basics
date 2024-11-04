def f(expression):
    total = 0
    current_number = ''
    operation = '+'  # Start with addition

    for char in expression:
        if char.isdigit():
            current_number += char
        else:
            total += int(current_number) if operation == '+' else -int(current_number)
            current_number = ''
            operation = char

    # Handle the last number
    total += int(current_number) if operation == '+' else -int(current_number)

    return total

if __name__ == "__main__":
    print(f("2+3"))         # Should return 5
    print(f("3+8+1"))       # Should return 12
    print(f("2+3-4+5-0"))   # Should return 6
