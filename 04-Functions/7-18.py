def f(number):
    # Convert the number to a string to iterate over each digit
    number_str = str(number)
    
    # Create a dictionary to count the occurrences of each digit
    digit_count = {}
    
    # Count the occurrences of each digit
    for digit in number_str:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1
            
    # Calculate the sum of repeated digits
    repeated_sum = 0
    for digit, count in digit_count.items():
        if count > 1:
            repeated_sum += int(digit) * count
            
    return repeated_sum

# Example usage:
print(f(1027))        # returns 0
print(f(230335))      # returns 9
print(f(513553007))   # returns 21