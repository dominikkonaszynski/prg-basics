number = int(input("Enter the number: "))

if number > 0:
    sign = "positive"
elif number == 0:
    sign = "zero"
else:
    sign = "negative"

print(f'Your number is {sign}')