###
# A program that prints your height both in cm and in feet and inches.
#
cm = float(input("Enter your height in cm: "))
feet = cm // 30.48 + (cm % 30.48 / 30.48 ) 
inches = cm // 2.54
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')
