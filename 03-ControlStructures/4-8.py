###
# Calculates values for the following fractions: 1/2, 1/3, ..., 1/10
#
dividend = 1

for divider in range(1,11):
    sum = dividend / divider
    print(f'{dividend}/{divider} = {sum:.2f}')