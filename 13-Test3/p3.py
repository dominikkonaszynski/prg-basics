def f(uid):
    result = map(lambda i: uid[i] in uid[:i], range(1, len(uid)))
    if any(result):
        return False
    else:
        return True
    
print(f(["berta3123", "DOM1N"]))
print(f(["berta3123", "berta3123"]))
print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
print(f(["abc123","ann","abc123","a10"]))