import csv

csv_file = "clothing.csv"
with open(csv_file) as file:
    file_content = csv.DictReader(file)
    for row in file_content:
        if float(row["Price"]) < 60 and int(row["Stock_Quantity"]) < 40:
            print(f'{row["Product_Name"]}, Size: {row["Size"]}')