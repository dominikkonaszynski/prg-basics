price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

for key,value in price_list.items():
    print(key,value)

total = 0
for key,value in price_list.items():
    total += value

print(f'Total price: {total:.2f}')

for key,value in price_list.items():
    price_list[key] = value * 0.9

for key,value in price_list.items():
    print(f'{key}: {value:.2f}')

sum = 0
for key,value in price_list.items():
    sum += value

print(f'The total price of products after discount is: {sum:.2f}')
