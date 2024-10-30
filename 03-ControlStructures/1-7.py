###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
is_bonus = False # does the employee receive a bonus
bonus = 0.15 # 15%

decision = input ("Does employee get bonus? Y/N :  ")

if decision == "Y" :
    is_bonus = True

if is_bonus:
    total_salary = basic_salary * (1 + bonus)
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {decision}')
print(f'Total salary: {total_salary}')