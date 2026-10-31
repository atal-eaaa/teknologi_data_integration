import requests
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt



url     = "https://api.energidataservice.dk/dataset/ConsumptionCoverageNationalDecl"

params  = {
            'start'    : 'Now-P14D',
            'end'      : 'Now-P7D',
            'columns'  : 'HourDK,ConnectedArea,ShareMWh',
            'limit'    : 10,
            'timezone' : 'DK'
          }
response = requests.get(url, params=params, timeout=5)

if response.status_code==200:
    data = response.json()
    pprint(data)
      
    df = pd.DataFrame(data['records'])
    
    df_agg = df.groupby('ConnectedArea')['ShareMWh'].sum().reset_index()

    df_agg.plot(
       kind = 'bar',
       x    = 'ConnectedArea',
       y    = 'ShareMWh'
    )

    plt.show()
    
else:
    print(f"Fejl: {response.status_code}")
    


