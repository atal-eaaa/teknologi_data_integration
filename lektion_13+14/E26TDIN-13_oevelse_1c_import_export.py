# %%
import requests
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt

url = "https://api.energidataservice.dk/dataset/ProductionConsumptionSettlement"

params = {
    'start'     : 'Now-P21D',
    'columns'   : 'PriceArea,HourDK,ExchangeNO_MWh,ExchangeSE_MWh,ExchangeGE_MWh,ExchangeNL_MWh,ExchangeGB_MWh',
    'filter'    : '{"PriceArea" : "DK1"}',
    'limit'     : 0
}

response = requests.get(url, params)
data = response.json()

# %%

df = pd.DataFrame(data['records'])
df = df.fillna(0)
df['HourDK'] = pd.to_datetime(df['HourDK'])

df['Total_MWh'] = df['ExchangeNO_MWh'] + \
                  df['ExchangeSE_MWh'] + \
                  df['ExchangeGE_MWh'] + \
                  df['ExchangeNL_MWh'] + \
                  df['ExchangeGB_MWh']

df['date'] = df['HourDK'].dt.date

df_agg = df.groupby('date', as_index=False)['Total_MWh'].sum()

# %%

df_agg.plot(
    kind = 'bar',
    x    = 'date',
    y    = 'Total_MWh',
    rot  = 90
)
plt.show()


# %%

df.plot(
    kind   = 'line',
    x      = 'HourDK',
    y      = 'Total_MWh',
    grid   = True,
    rot    = 90
)
