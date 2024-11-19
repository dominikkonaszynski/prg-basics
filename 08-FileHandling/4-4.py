company_file = 'it_company.csv'
with open(company_file) as file:
    i = 0
    lines = file.readlines()
    total_lines = len(lines)
    
    while i < total_lines:
        for j in range(i, min(i + 5,total_lines)):
            print(lines[j])
        input("\nPress Enter key to continue...")
        i += 5