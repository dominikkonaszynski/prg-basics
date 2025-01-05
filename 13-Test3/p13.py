import re
def f(mnubers):
    pattern = r'^[+-]?[1-7a-dA-D]+$'
    valid_numbers = len(list(filter(lambda num: re.match(pattern, num), mnubers)))
    return valid_numbers

print(f(["A15","-31","7abC","+D1","-gH"]))
print(f(["A05","-3+1","7ab8C","+D1","-22k"]))