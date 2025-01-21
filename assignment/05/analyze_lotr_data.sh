#!/bin/bash

# Gesamtanzahl der Zeilen im Datensatz
echo "Gesamtanzahl der Zeilen im Datensatz:"
wc -l lotr_cleaned_.csv

echo "Einzigartige Wörter in 'dialog':"
cut -d',' -f2 lotr_cleaned_.csv | tr ' ' '\n' | tr -d '[:punct:]' | tr '[:upper:]' '[:lower:]' | sort | uniq -c | awk '$1 == 1 {print $2}'

# Top-5-Charaktere in der Spalte 'char'
echo "Top-5-Charaktere in 'char':"
cut -d',' -f2 lotr_cleaned_.csv | sort | uniq -c | sort -nr | head -5

# Top-5-Charaktere in den Dialogen
echo "Top-5-Charaktere in den Dialogen:"
awk -F',' 'NR > 1 { gsub(/"/, "", $3); split($3, words, " "); count[$1] += length(words) }
END { for (char in count) print count[char], char }' lotr_cleaned_.csv | sort -nr | head -5
