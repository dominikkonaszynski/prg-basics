###
# Calculates the sum of the digits in a number
#
def sum_of_digits(number):
    # Handle negative numbers
    number = abs(number)
    
    # Convert the number to a string
    number_str = str(number)
    
    # Initialize a total to sum the digits
    total = 0
    
    # Iterate over each character in the string representation
    for digit in number_str:
        total += int(digit)  # Convert character back to integer and add to total
        
    return total

# Main program to read a number from the user and print the sum of its digits
if __name__ == "__main__":
    user_input = int(input("Enter an integer: "))  # Read an integer input
    result = sum_of_digits(user_input)  # Calculate the sum of digits
    print(f"The sum of the digits in {user_input} is: {result}")  # Output the result