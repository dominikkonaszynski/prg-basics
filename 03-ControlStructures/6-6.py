hours = int(input("Enter the amount of hours you have parked: "))
if hours == 0:
    print("Your parking was free!")
elif hours >= 1 and hours <=2:
    print("Fee is 5PLN")
elif hours >=3 and hours <=6:
    print("Fee is 15PLN")
elif hours >6:
    print("Fee is 20PLN")