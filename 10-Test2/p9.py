import csv
csv_file = "data.csv"

def f(value):
    count = 0
    with open(csv_file) as file:
        file_content = csv.DictReader(file)
        for worker in file_content:
            if int(worker["salary"]) >= value:
                count +=1
    return count
        
if __name__ == "__main__":
    print(f(9200))
    print(f(11640))
    print(f(17700))