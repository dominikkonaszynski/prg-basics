###
# Calculates the final grade for a test based
# on the number of points obtained
#
points = int(input("Enter the amount of points you got: "))
def pts_to_grade(points):
    if points >= 18:
        grade = 'Excellent'
    elif points >=14:
        grade = 'Good'
    elif points >=10:
        grade = 'Satisfactory'
    else: 
        grade = 'Fail'
    return grade

test_result = points
final_grade = pts_to_grade(test_result)
print(f'You scored {points} points on the test. Your final grade is {final_grade}')