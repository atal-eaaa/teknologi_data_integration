import requests
import time

# Opgave: Vi skal finde længde- og breddegrad på disse tre adresser
addresses = [
    "Sønderhøj 30, 8260 Viby J",
    "Banegårdspladsen 1, Aarhus",
    "Rådhuspladsen, København"
]

url = "https://nominatim.openstreetmap.org/search"

for address in addresses:
    # Vi looper igennem adresserne og fortager et API-kald for hver.
    # I linje 20 identificerer vi os overfor web-servicen, så de kan 
    # følge vores færden. Navn på User-Agent er valgfrit.
    response = requests.get(
        url,
        params={ "q": address, "format": "jsonv2" },
        headers={ "User-Agent": "EAAA-ØKIT Årgang 2025" }
    )

    data = response.json()

    if len(data) > 0:
        # APIet kunne finde adressen og gav os bl.a. længde- og 
        # breddegrad
        lat = data[0]["lat"]
        lon = data[0]["lon"]

        print(address)
        print(f"  Latitude : {lat}")
        print(f"  Longitude: {lon}")

    else:
        # APIet kunne ikke finde data på den angivne adresse
        print(f"Ingen resultater for: {address}")

    # God stil: Giv APIet et pusterum på et sekund, inden næste 
    # API-kald skydes af. Bemærk import i linje 2! 
    time.sleep(1)