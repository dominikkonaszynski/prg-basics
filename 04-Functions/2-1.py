###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter_read = input('Enter the letter: ')
print(f"Your letter is: {letter_read}")

str_number_repr = int("20303")
print('The number representation of the string is', str_number_repr)

binary_repr = bin(304)
print('The binary representation of decimal number is', binary_repr)

hex_repr = hex(304)
print('The hexadecimal representation of the decimal number is', hex_repr)

absolute_value = abs(-17)
print('The absolute value of -17 is', absolute_value)
