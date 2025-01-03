employees = [
    'SMITH Lucy',
    'JONES Janet',
    'LEE Jerry',
    'JACKSON Peter',
    'JOHNSON Rick',
    'LEWIS Terry',
    'CLARKE Robin']

result = list(filter(lambda name: name[0] == "J", employees))
print(result)