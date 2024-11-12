# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]


# Calculates expenses
# Use loop statements
total_food_cost = 0
for i in range(len(monthly_expenses)):
    food_cost = monthly_expenses[i][0]
    total_food_cost += food_cost



# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',total_food_cost)
print('Transport:',...)
print('Utilities:',...)
print('Week 1:',...)
print('Week 2:',...)
print('Week 3:',...)
print('Week 4:',...)
print('---------------')
print('TOTAL:',...)