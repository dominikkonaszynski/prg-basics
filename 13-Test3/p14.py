def f(d):
    in_park = list()

    for reg_num, action in d:
        if action == "in":
            in_park.append(reg_num)
        elif action == "out":
            in_park.remove(reg_num)
    
    return sorted(list(in_park))

cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]
print(f(cars))