# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Returns a week day name
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

# Returns a string with day meal names separated by commas
def day_meal_plan(meal_plan, day_number):
   # Fetch meals for the specific day
   meals = meal_plan[day_number - 1]
   # Return the formatted string: Breakfast, Lunch, Dinner
   return f"{meals[0]}, {meals[1]}, {meals[2]}"
   
   # Loop through days 1 to 7
for i in range(1, 8):
    # Get the weekday name and meal plan for the day
    day_name = weekday(i)
    meals = day_meal_plan(meal_plan, i)
    print(f"{day_name}: {meals}")

# Call the function to print the meal plan

