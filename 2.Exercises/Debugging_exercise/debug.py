produkte = {
    "Apfel": 2,
    "Banane": 3,
    "Milch": 1,
    "Brot": 2
}

warenkorb = []

def produkt_hinzufuegen(produkt, menge):
    if produkt in produkte:
        warenkorb.append((produkt, menge))
        print(f"{menge}x {produkt} hinzugefügt.")
    else:
        print("Produkt nicht gefunden.")

def berechne_preis():
    gesamt = 0

    for produkt, menge in warenkorb:
        preis = produkte[produkt]
        gesamt = gesamt + preis

    return gesamt


def anzeigen():
    print("\nWarenkorb:")

    for produkt, menge in warenkorb:
        print(f"- {produkt}: {menge} Stück")

    print(f"Gesamtpreis: {berechne_preis()} CHF")


produkt_hinzufuegen("Apfel", 3)
produkt_hinzufuegen("Milch", 2)
produkt_hinzufuegen("Brot", 1)

anzeigen()