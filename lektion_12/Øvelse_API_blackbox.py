
import requests

url = ""


response = requests.get(url)
data = response.json()

print("Tidspunkt \t\t CO2-emission \t Produktion > 100MW \t Produktion < 100MW \t Offshore Wind \t Onshore Wind")
print("-" * 120)
for rec in data["records"]:
    print(f'{rec["Minutes1DK"]} \t {int(rec["CO2Emission"])} \t\t {int(rec["ProductionGe100MW"])} \t\t\t {int(rec["ProductionLt100MW"])} \t\t\t {int(rec["OffshoreWindPower"])} \t\t {int(rec["OnshoreWindPower"])}')
print("-" * 120)
    
    