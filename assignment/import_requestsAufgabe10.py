# Assignment 10:
# No.:1 
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL der Pokémon-Datenbank
url = "https://pokemondb.net/pokedex/all"

# HTTP-Request senden
response = requests.get(url)
response.raise_for_status()  # Fehler abfangen, falls die Anfrage fehlschlägt

# HTML-Inhalt parsen
soup = BeautifulSoup(response.text, 'html.parser')

# Die Tabelle finden
table = soup.find('table', {'id': 'pokedex'})

# Tabellenüberschriften extrahieren
headers = [header.text for header in table.find('thead').find_all('th')]

# Tabelleninhalte extrahieren
rows = table.find('tbody').find_all('tr')
data = []
for row in rows:
    cols = row.find_all('td')
    
     # Sprite-Bild URL extrahieren
    sprite_tag = row.find('img')  # Erstes Bild-Tag finden
    sprite_url = sprite_tag['src'] if sprite_tag else ""

    # Daten speichern
    row_data = [col.text.strip() for col in cols]
    row_data.insert(1, sprite_url)  # Sprite-URL an Position 1 einfügen
    
    
    
    data.append([col.text.strip() for col in cols])

# DataFrame erstellen
df = pd.DataFrame(data, columns=headers)

# DataFrame anzeigen
print(df)

# Optional: DataFrame als CSV speichern
df.to_csv('pokemon_data_with_sprites.csv', index=False)

# No. 2:
# Datenanalyse

print(df)
print(df.info())
print(df.columns)
print(df['Total'].dtype)

# a) a) Welches sind die stärksten Pokémon (jeweils pro Typ)?
# Habe ich leider nicht mehr geschafft, konnte das Problem mit der Umwandlung von Object in Nummer nicht lösen...
#strongest_pokemon_by_type = df.groupby('Type')["Total"].idxmax()]
#strongest_pokemon = df.loc[df.groupby("Type")["Total"].idxmax()]
#print(strongest_pokemon_by_type)

# b) Welche Pokémon haben den höchsten Angriffs-Wert?
best_attackers = df.sort_values(by="Attack", ascending=False).head(10)

# c) Wie sehen die Durchschnittswerte der Pokémon pro Typ aus?
df_grouped = df.groupby("Type")["Total"].mean()

