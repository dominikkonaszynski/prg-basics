###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1 - 12): '))

if 10 <= month <= 12:
    quarter = 4
elif 7 <= month < 10:
    quarter = 3
elif 4 <= month < 7:
    quarter = 2
elif 1 <= month < 4:
    quarter = 1   
else:
    print("You entered wrong month ")
    quarter = None

if quarter is not None:
    print(f'Month {month} is in quarter {quarter}')