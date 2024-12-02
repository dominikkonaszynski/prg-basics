import csv
print("GRAPHIC DESIGNERS")
print("===============")

csv_file = "it_company.csv"
with open(csv_file) as file:
    file_content = csv.DictReader(file)
    for row in file_content:
        if row["Job Title"] == "Graphic Designer":
            print(f'{row["First Name"]} {row["Last Name"]}, {row["Email"]}')