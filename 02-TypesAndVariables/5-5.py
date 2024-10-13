# A program to calculate price after discount.
price_string = input('Enter the price : ')
price = float(price_string)
price = round(price,2)
discount_string = input('Enter the discount % : ')
discount = int(discount_string)
price_after_discount = price * (1 - discount/100)
price_after_discount = round(price_after_discount,2)
reduction = price - price_after_discount
reduction = round(reduction,2)
print(f'Enter price : {price}')
print(f'Enter discount % : {discount}')
print(f'Price with discount : {price_after_discount} ')
print(f'Reduction : {reduction}')
