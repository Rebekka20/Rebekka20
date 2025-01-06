#!/bin/bash

# Verzeichnis für die CSV-Datei
FILE="contacts.csv"

# 1. Alle E-Mail-Adressen extrahieren
echo "1. Extract all email addresses:"
grep -oP '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}' $FILE
echo ""

# 2. Alle Telefonnummern extrahieren
echo "2. Extract all phone numbers:"
grep -oP '\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}' $FILE
echo ""

# 3. Alle Namen, die mit "J" anfangen
echo "3. Extract all names that start with the letter 'J':"
grep -oP '\bJ[a-zA-Z]*\b' $FILE
echo ""

# 4. Alle Straßennamen, die "St" enthalten
echo "4. Extract all street names that contain the word 'St':"
grep -oP '\b\w+\s*St\w*\b' $FILE
echo ""

# 5. Alle Adressen in den USA extrahieren
echo "5. Extract all addresses in 'USA':"
grep -oP '.*\bUSA\b' $FILE | sed 's/,\s*USA.*//'
echo ""

# 6. Alle Nachnamen extrahieren
echo "6. Extract the last names of all people:"
grep -oP '^\S+\s(\S+)' $FILE | awk '{print $2}'
echo ""

# 7. Alle Domains von E-Mail-Adressen extrahieren
echo "7. Extract all email domains (part after the @ sign):"
grep -oP '@\K[\w.-]+' $FILE
echo ""

# 8. Alle Instanzen des Vornamens 'David' mit vollständiger Adresse (Straße und Stadt)
echo "8. Extract all instances of the first name 'David' along with their full address:"
grep -oP 'David\s+\S+\s*,\s*[^,]+,\s*[A-Za-z\s]+' $FILE
echo ""

# 9. Alle Einträge, bei denen die Telefonnummer mit "7" endet
echo "9. Find all entries where the phone number ends with '7':"
grep -P '.*\d{1,}7\b.*' $FILE
echo ""

# 10. Alle Instanzen von Vornamen, die mit "e" enden
echo "10. Extract all instances of first names that end with the letter 'e':"
grep -oP '^\b[A-Za-z]+e\b' $FILE
