test_results = [
   {"name":"Peter","result":27},
   {"name":"Anna","result":63},
   {"name":"Robert","result":92},
   {"name":"Paul","result":46},
   {"name":"Barbara","result":52}]

result = list(filter(lambda student: student["result"] > 50 and student["result"] < 70, test_results))
for student in result:
    print(f'{student["name"]}: {student["result"]} points')