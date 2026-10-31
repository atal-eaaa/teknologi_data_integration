import requests


url = "https://api.energidataservice.dk/dataset/PowerSystemRightNow"

try:
    # foretag API-akald. Timeout sættes i linje 11 til fem sekunder. 
    response = requests.get(
        url,
        params={"limit": 5},
        timeout=5
    )

    # Python beder requests kontrollere HTTP-koden:
    # 200 - alt i orden!
    # 404 - kan ikke finde web-siden
    # 500 - Server-fejl
    response.raise_for_status()

    print("Kald lykkedes")

except requests.exceptions.Timeout:
    
    # Lidt speciel except. Tester KUN for timeout!
    print("API'et svarede ikke inden for 5 sekunder")

# Energinet svarer (næsten) garanteret inden for fem sekunder. Du kan
# fremprovokere en fejl og se timeout virkes ved at sætte parameteren 
# til f.eks. 0.01 sekund
