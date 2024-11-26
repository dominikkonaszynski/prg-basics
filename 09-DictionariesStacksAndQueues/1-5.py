countries = [
{"name":"Poland", "population":38000000},
{"name":"Germany", "population":85000000},
{"name":"USA", "population":300000000},
{"name":"UK", "population":68000000},
{"name":"Spain", "population":48000000},
]

print(f'{"COUNTRY"}  {"POPULATION"}')
for country in countries:
    print(f'{country['name']}  {country['population']}')