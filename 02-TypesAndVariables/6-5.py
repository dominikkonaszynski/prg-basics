###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input('Enter phone number: ')
print(f'Your phone number is: {phone[0:3]}-{phone[3:6]}-{phone[6:9]}')