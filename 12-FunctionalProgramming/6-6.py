employees = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

list = list(map(lambda name: f"{name[0].upper()}, {name[1]}", employees))

for name in list:
    print(name)