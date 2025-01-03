results = [37, 51, 44, 23, 78, 92, 39, 84, 83, 51]

def min_pts(limit):
   return lambda pts: pts >= limit

result_70 = list(filter(min_pts(70), results))
result_40 = list(filter(min_pts(40), results))
result_30 = list(filter(min_pts(30), results))

print(f"Min 70 pts: {result_70}")
print(f"Min 40 pts: {result_40}")
print(f"Min 30 pts: {result_30}")