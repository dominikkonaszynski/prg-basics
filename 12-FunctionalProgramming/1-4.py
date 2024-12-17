n1 = int(input("Enter the speed in m/s: "))

ms_to_kmh = lambda x : x*3.6

result = ms_to_kmh(n1)
print(f'{n1} m/s = {result} km/h')