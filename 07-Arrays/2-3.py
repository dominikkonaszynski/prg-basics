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
total_transport_cost = 0
total_utilities_cost = 0
for i in range(len(monthly_expenses)):
    total_food_cost += monthly_expenses[i][0]
    total_transport_cost += monthly_expenses[i][1]
    total_utilities_cost += monthly_expenses[i][2]

total_week1_cost = sum(monthly_expenses[0])
total_week2_cost = sum(monthly_expenses[1])
total_week3_cost = sum(monthly_expenses[2])
total_week4_cost = sum(monthly_expenses[3])
total_cost = total_week1_cost + total_week2_cost + total_week3_cost + total_week4_cost

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',total_food_cost)
print('Transport:',total_transport_cost)
print('Utilities:',total_utilities_cost)
print('Week 1:',total_week1_cost)
print('Week 2:',total_week2_cost)
print('Week 3:',total_week3_cost)
print('Week 4:',total_week4_cost)
print('---------------')
print('TOTAL:',total_cost)