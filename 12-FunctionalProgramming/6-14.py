fillings = [508,500,512,499,492,511,503,476,501,509]

def filling(limit):
   return lambda amount: amount <= 500 - (500 * limit * 0.01) or amount >= 500 + (500 * limit * 0.01)

incorrect_bottles = list(filter(filling(2), fillings))
incorrect_percentage = (len(incorrect_bottles)/ len(fillings)) * 100
print("Bottle capacity:    500ml")
print("Filling tolerance:  2%")
print(f"Filled bottles:     {','.join(map(str, fillings))}")
print(f"Incorrectly filled: {incorrect_percentage:.0f}%")