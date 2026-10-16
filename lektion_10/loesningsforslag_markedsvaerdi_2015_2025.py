# %%

import pandas as pd
import matplotlib.pyplot as plt

filename = "all_leagues.csv"

df = pd.read_csv(filename, sep=',', encoding='utf-8-sig')
print("--- DONE --- ")

# %%

df_tmv    = df[df['season'] == '2015/16']
df_tmv_agg = df_tmv.groupby('tier')['total_market_value'].sum()
df_tmv_agg = df_tmv_agg.reset_index()
df_tmv_agg = df_tmv_agg.sort_values(by='total_market_value', ascending=False)

df_tmv_agg.plot(
    kind ='bar',
    x = 'tier',
    y = 'total_market_value'
)
plt.title('Total Market Value 2015/16')
plt.show()



# %%

df_tmv    = df[df['season'] == '2025/26']
df_tmv_agg = df_tmv.groupby('tier')['total_market_value'].sum()
df_tmv_agg = df_tmv_agg.reset_index()
df_tmv_agg = df_tmv_agg.sort_values(by='total_market_value', ascending=False)

df_tmv_agg.plot(
    kind ='bar',
    x = 'tier',
    y = 'total_market_value'
)
plt.title('Total Market Value 2025/26')
plt.show()



# %%
df_ger = df[(df['country'] == 'GER') & (df['season'] >= '2015/16')]
df_ger_agg = df_ger.groupby('season')['total_market_value'].sum()
df_ger_agg = df_ger_agg.reset_index()

df_ger_agg.plot(
    kind ='line',
    x = 'season',
    y = 'total_market_value'
)
plt.title('Total Market Value, german leagues')
plt.show()

# %%
