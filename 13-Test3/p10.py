def f(d):
    average_number = sum(d.values())/ len(d)

    return len(list(filter(lambda passengers: passengers > average_number, d.values())))

print(f({"LO231":150,"BA787":120,"NZ15":30}))
print(f({"LO231":150,"BA787":20,"NZ15":30}))