categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

# Find the index of the maximum expense
max_expense_index = expenses.index(max(expenses))

# Output the category with the highest expense
print(f"The most expensive category is {categories[max_expense_index]} with an expense of {expenses[max_expense_index]}")