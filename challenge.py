names = ['fluffy', 'spot', 'cujo']
ages = [3, 7, 12]
animal_type = ['cat', 'dog', 'mean dog']

# {fluffy: {age: 3, animal_type: cat}, ... }

pets = {}

for i in names:
    ind = names.index(i)
    pets.update({i: {'age': ages[ind], 'animal_type': animal_type[ind]}})

print(pets)

print(pets.keys())
for x in pets.keys():
    print(f'{x} is {pets[x]["age"]} and a {pets[x]["animal_type"]}')
