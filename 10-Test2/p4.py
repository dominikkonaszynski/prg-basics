def f(subjects):
    best_subject = ""
    max_average = 0
    for subject, grades in subjects.items():
        avg_grade = sum(grades)/len(grades)
        if avg_grade > max_average:
            max_average = avg_grade
            best_subject = subject
        
    return best_subject
    
if __name__ == "__main__": 
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))