transactions_in_eur = [15.90, 38.47, 4.07, 132.70, 9.15]
transactions_in_pln = list(map(lambda values:values * 4.5, transactions_in_eur))
formatted_result = [f'{payment:.2f}' for payment in transactions_in_pln]
print(formatted_result)