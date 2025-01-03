temperatures = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
result = list(map(lambda item: item[0], filter(lambda item: item[1] > 0, temperatures.items())))
print(f"Cities with positive temperature: {', '.join(result)}")