import pandas as pd

df = pd.DataFrame({
    'name': ['Maria', 'Bernd', 'Tanja'],
    'alter': [20, 30, 40],
})

# Ersten Datensatz ausgeben
print(df.head(1))
print('---------')

# Letzte Zeile
print(df.tail(1))
print('---------')

# Ausgewählte Zeile(n) ausgeben
print(df[1:2])
print('---------')

# Zugriff auf die Erste Spalte
print(df['name'])
print('---------')

# Zugriff auf den ERSTEN Namen
print(df['name'][0])
print('---------')

print(df.index)
print('---------')
print(df.columns)
print('---------')
print(df.describe())
print('---------')

print(df)
print('---------')

df = df.sort_values(by='name')
print(df)
print('---------')

print(df['alter'] > 29)

df2 = df[df['alter'] > 29]

print(df2)
print(df)

df2.to_csv('df2.csv', sep=';')
print('---------')

# Daten ersetzen / ändern
# df['name'][0] = 'Ersetzt'
df.at[0, 'name'] = 'Ersetzt'
# df.iat[1, 0] = 'Ersetzt'
print(df)
print('---------')

df3 = pd.concat(
    [df,
     pd.DataFrame({
         'name': ['Michael'],
         'alter': 42,
     })],
    ignore_index=True
)

print(df3)
