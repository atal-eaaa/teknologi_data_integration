import requests
from io import StringIO
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


# matplotlib.use('QtAgg')
resource = "https://api.statbank.dk/v1/data/bil51/CSV"

params={
    'Tid'       : '*',
    'DRIV'      : '*',
    'EJER'      : '*',
 }   

response = requests.get(resource, params=params)
# print(response)
# print(response.text)

if response.status_code == 200:
    df = pd.read_csv(StringIO(response.text), sep=";")
    df['INDHOLD'] = pd.to_numeric(df['INDHOLD'], errors='coerce')
    df.info()
    df_diesel = df[(df['DRIV'] == "Diesel") & (df['EJER'] == 'I alt')]
    df_diesel.plot(
        kind = 'bar',
        x = 'TID',
        y = 'INDHOLD',
        rot = 90
    )

    df_el = df[(df['DRIV'] == "El") & (df['EJER'] == 'I alt')]
    df_el.plot(
        kind = 'bar',
        x = 'TID',
        y = 'INDHOLD',
        rot = 90
    )

    df_benzin = df[(df['DRIV'] == "Benzin") & (df['EJER'] == 'I alt')]
    df_benzin.plot(
        kind = 'bar',
        x = 'TID',
        y = 'INDHOLD',
        rot = 90
    )

    plt.show()

else:
    print(f"Fejl i API-kald : {response.status_code}")