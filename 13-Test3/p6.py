def f(vname):
    if not (1 <= len(vname) <= 5):
        return False
    if not (vname[0].isalpha() or vname[0] == '_'):
        return False
    
    return all(map(lambda c: c.isalnum() or c == '_', vname[1:]))

print(f("abc")) 
print(f("Abc"))
print(f("aBC")) 
print(f("_ab_c")) 
print(f("abcdef")) 
print(f("8abc"))
print(f("_aB8_")) 
print(f("_4x"))