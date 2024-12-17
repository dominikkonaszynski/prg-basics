names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']


sorted_names = sorted(names, key= lambda name: len(name))
print("Sorted names: ")
for name in sorted_names:
    print(name)