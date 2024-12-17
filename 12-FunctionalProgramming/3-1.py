payments = [15.90, 38.47, 4.07, 132.70, 9.15]
conversion = lambda payment: payment * 4.5
result = list(map(conversion, payments))
formatted_result = [f'{payment:.2f}' for payment in result]
print(formatted_result)