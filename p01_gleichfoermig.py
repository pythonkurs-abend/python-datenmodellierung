import matplotlib as plt

kunden = [
    ['Vorname', 'Nachname', 'Alter'],
    ['Tanja', 'Huber', 54],
    ['Maria', 'Wagner', 0],
    {'Vorname': 'Maria', 'Nachname': 'Wagner', 'Alter': 0}
]

print(kunden[2][0])
print(kunden[3]['Vorname'])
print(type(kunden[3]))
print(isinstance(kunden[3], dict))
