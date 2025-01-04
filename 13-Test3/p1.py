def f(word):
    result = map(lambda i: word[:i] + word[i].upper() + word[i+1:].lower(), range(len(word)))
    return '-'.join(result)

print(f("book"))
print(f(""))