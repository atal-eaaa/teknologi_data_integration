import requests
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt

url = "https://api.energidataservice.dk/dataset/ConsumptionCoverageNationalDecl/download?start=Now-P14D&end=Now-P7D&columns=HourDK%2CConnectedArea%2CShareMWh&limit=5&timezone=DK"
response = requests.get(url, timeout=5)


if response.status_code==200:
    data = response.json()
    df = pd.DataFrame(data)
    df_agg = df.groupby('ConnectedArea')['ShareMWh'].sum().reset_index()

    df_agg.plot(
       kind = 'bar',
       x    = 'ConnectedArea',
       y    = 'ShareMWh'
    )

    plt.show()
    
else:
    print(f"Fejl: {response.status_code}")
    


"""
Her er de dokumenterede el-netforbindelser (“grids”) for de to danske prisområder — dvs. hvilke andre zoner DK1 og DK2 er forbundet til (direkte):

DK1 (Vestdanmark)
 * NO2 (Norge) – Skagerrak-forbindelsen. 
 * SE3 (Sverige) – Konti-Skan. 
 * DE (Tyskland / DE-LU zone) – Jylland–Tyskland-forbindelserne. 
 * NL (Holland) – COBRAcable (HVDC). 
 * DK2 – Storebæltsforbindelsen (intern DK1↔DK2 DC-link). 

DK2 (Østdanmark)
 * SE4 (Sverige) – Øresund-/København–Malmö-forbindelser (AC) m.fl. 
 * DE (Tyskland / DE-LU zone) – KONTEK (HVDC) til 50Hertz-området. 
 * DK1 – Storebæltsforbindelsen (intern DK1↔DK2 DC-link). 

 Kilderne ovenfor er Energinet/ENS/ENTSO-E-dokumenter, der omtaler de konkrete interconnectors og grænser (DK1-NO2, DK1-SE3, DK1-DE, DK1-NL, DK2-SE4, DK2-DE samt DK1-DK2).
"""