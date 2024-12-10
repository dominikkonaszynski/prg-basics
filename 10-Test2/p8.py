def f(expression):
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
    
    return stack.pop()

if __name__ == "__main__":
    print(f("2 3 +"))
    print(f("2 6 + 4 5 - +"))
    print(f("11 7 + 15 - 14 +"))
    print(f("10 5 - 7 2 + 8 4 - + +"))
