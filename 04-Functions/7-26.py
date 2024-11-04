def f(product_code):
    if len(product_code) != 4:
        return False
    
    first_three_digits = product_code[:3]
    control_digit = int(product_code[3])
    digit_sum = sum(int(digit) for digit in first_three_digits)
    expected_control_digit = digit_sum % 7
    return control_digit == expected_control_digit

if __name__ == "__main__":
    print(f('1082'))