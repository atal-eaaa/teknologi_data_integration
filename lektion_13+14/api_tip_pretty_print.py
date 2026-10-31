import requests
import json
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)

response = requests.get(
    "https://api.energidataservice.dk/dataset/PowerSystemRightNow",
    params={"limit": 1}
)

data = response.json()

# Linje 16 printer "almindeligt". Kør ført koden med denne lige aktiv.
# Flyt så fra 17 til 16 #, så du kører linje 17 i stedet. Se forskellen
pp.pprint(data)
# print(json.dumps(data, indent=4))