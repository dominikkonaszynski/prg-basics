values = [48,47,54,50,42,68,39,46]
result = list(filter(lambda speed: speed > 50, values))

print(f"Recorded values: {', '.join(map(str, values))}")
print(f"Speed too high: {', '.join(map(str, result))}")