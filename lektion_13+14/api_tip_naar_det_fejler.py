import requests

# Specificerer url - denne findes ikke og giver fejl!
url = "https://api.energidataservice.dk/dataset/FindesIkke"


try:
    # API-kald: forsøger at hente data
    response = requests.get(url)

    # Python beder requests kontrollere HTTP-koden:
    # 200 - alt i orden!
    # 404 - kan ikke finde web-siden
    # 500 - Server-fejl
    response.raise_for_status()
    print("Kald lykkedes")

except requests.exceptions.HTTPError:
    
    # Hvis kaldet fejler, udskrives fejlen
    print(f"Fejl {response.status_code}")


    