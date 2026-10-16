# %%

import pandas as pd
import matplotlib.pyplot as plt

filename = "all_leagues.csv"

df = pd.read_csv(filename, sep=',', encoding='utf-8-sig')
print("--- DONE --- ")

# %%

df_foreigners = df[df['season'] == '2024/25']
df_foreigners['foreigners_pct'] = df_foreigners['foreigners'] / df_foreigners['squad'] * 100
df_foreigners['rank'] = df_foreigners['foreigners_pct'].rank(pct=False, ascending=False)
df_foreigners = df_foreigners[df_foreigners['rank'] <= 20]
df_agg = df_foreigners.groupby('tier')['rank'].count()
df_agg = df_agg.reset_index()

df_agg.plot(
    kind = 'bar',
    x    = 'tier',
    y    = 'rank'
)
plt.title('Top 20 af klubber med højst %-del af udlændinge')
plt.show()

# %%

df_m_value = df[df['season'] == '2025/26']
df_m_value['rank'] = df_m_value['total_market_value'].rank(pct=True, ascending=False)
df_m_value = df_m_value[df_m_value['rank'] <= 0.2]
df_agg = df_m_value.groupby('country')['rank'].count()
df_agg = df_agg.reset_index()

df_agg.plot(
    kind = 'bar',
    x    = 'country',
    y    = 'rank'
)
plt.title("Top 20% af klubber målt på markedsværdi")
plt.show()
# %%
