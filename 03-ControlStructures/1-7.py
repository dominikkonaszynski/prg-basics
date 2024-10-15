###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
is_bonus = True # does the employee receive a bonus
bonus = 0.3 # 15%

decision = input ("Does employee get bonus? Y/N :  ")

if decision == ("Y") :
    total_salary = basic_salary * 1.3
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {decision}')
print(f'Total salary: {basic_salary * (1 +bonus)}')