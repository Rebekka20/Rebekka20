#!/bin/bash

# Aufgabe 1: Erste 3 Zeilen der Datei '2014-01_JA.tsv'
echo "Aufgabe 1: Erste 3 Zeilen der Datei 2014-01_JA.tsv"
head -n 3 2014-01_JA.tsv
echo

# Aufgabe 2: Gesamtanzahl der Zeilen in jeder .tsv-Datei
echo "Aufgabe 2: Gesamtanzahl der Zeilen in jeder .tsv-Datei"
wc -l *.tsv
echo

# Aufgabe 3: Datei mit der höchsten Zeilenanzahl
echo "Aufgabe 3: Datei mit der höchsten Zeilenanzahl"
wc -l *.tsv | sort -n | tail -1
