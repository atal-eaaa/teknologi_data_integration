from math import radians, sin, cos, sqrt, asin
import requests
from pprint import pprint

def distance(lat1, lon1, lat2, lon2):

    # Beregner Haversine-værdien og ganger med jordens radius. Haversine-formlen er en klassisk formel 
    # til beregning af afstanden mellem to punkter på en kugle. Input
    #    lat1  : breddegrad (latitude) på første adresse
    #    lon1  : længdegrad (longitude) på første adresse
    #    lat2  : breddegrad (latitude) på anden adresse
    #    lon2  : længdegrad (longitude) på anden adresse
        
    R = 6371

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = ( sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2 )
    c = 2 * asin(sqrt(a))
    distance = R * c

    return distance




url = "https://nominatim.openstreetmap.org/search"

params = {
    "q"      : "Aarhus Rådhus, Park Allé, Aarhus, Denmark", 
    "format" : "jsonv2"
}

headers  = {"User-Agent": "EAAA-API-undervisning/1.0"}
response = requests.get(url=url, params=params, headers=headers)
response.raise_for_status()

data = response.json()
pprint(data)