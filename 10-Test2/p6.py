import json
json_file = 'data.json'

def f(years,course,average_grade):
    count = 0
    with open (json_file) as file:
        file_content = json.load(file)
        for student in file_content:
            if student['age'] >= years:
                for course_data in student['studies']['courses']:
                    if course_data['name'] == course:
                        grades = course_data['grades']
                        average = sum(grades)/len(grades)
                        if average >= average_grade:
                            count += 1 
    return count

if __name__ == "__main__":
    print(f(10, "statistics", 1))