import re

def main():
    # Öffnen der Datei orders.csv und Lesen des Inhalts
    with open('orders.csv', 'r') as f_in:
        content = f_in.read()

    # 1. Alle Bestellnummern extrahieren
    order_numbers = re.findall(r'\d{5}', content)
    print(f"Bestellnummern: {order_numbers}")

    # 2. Alle Produktnamen extrahieren
    product_names = re.findall(r'Product\s+([A-Za-z]+)', content)
    print(f"Produktnamen: {product_names}")

    # 3. Alle Preise extrahieren
    prices = re.findall(r'\d+\.\d{2}', content)
    print(f"Preise: {prices}")

    # 4. Alle Bestelldaten extrahieren
    order_dates = re.findall(r'(\d{4})-(\d{2})-(\d{2})', content)
    print(f"Bestelldaten (YYYY-MM-DD): {order_dates}")

    # 5. Alle Bestellungen mit Preisen über 500 $ finden
    prices_over_500 = [price for price in prices if float(price) > 500]
    print(f"Bestellungen mit Preisen über 500 $: {prices_over_500}")

    # 6. Datum von YYYY-MM-DD auf DD/MM/YYYY umwandeln
    formatted_dates = [re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', f"{date[0]}-{date[1]}-{date[2]}") for date in order_dates]
    print(f"Umgewandelte Bestelldaten (DD/MM/YYYY): {formatted_dates}")

    # 7. Produktnamen mit mehr als 6 Zeichen extrahieren
    long_product_names = [name for name in product_names if len(name) > 6]
    print(f"Produktnamen mit mehr als 6 Zeichen: {long_product_names}")

    # 8. Häufigkeit der Produkte zählen
    product_count = {product: product_names.count(product) for product in set(product_names)}
    print(f"Häufigkeit der Produkte: {product_count}")

    # 9. Bestellungen mit Preisen, die auf .99 enden, extrahieren
    prices_ending_with_99 = [price for price in prices if price.endswith('.99')]
    print(f"Bestellungen mit Preisen, die auf .99 enden: {prices_ending_with_99}")

    # 10. Den günstigsten Preis finden
    cheapest_price = min(prices, key=float)
    print(f"Günstigster Preis: {cheapest_price}")

if __name__ == "__main__":
    main()
