# %%

import pandas as pd
import matplotlib.pyplot as plt

filename = "all_leagues.csv"

df = pd.read_csv(filename, sep=',', encoding='utf-8-sig')
print("--- DONE --- ")

the_big_three=['Real Madrid', 'FC Barcelona', 'Atlético Madrid']



# %%

df_b3    = df[(df['club_std_name'].isin(the_big_three)) & (df['season'] > '2006/07')]
df_b3_agg = df_b3.groupby('season')['foreigners'].mean()
df_b3_agg = df_b3_agg.reset_index()
# df_b3_agg = df_b3_agg.sort_values(by='total_market_value', ascending=False)

df_b3_agg.plot(
    kind ='bar',
    x = 'season',
    y = 'foreigners'
)
plt.title('Avg. foreigners i clubs - The Big Three')
plt.show()



# %%

df_rest    = df[(~df['club_std_name'].isin(the_big_three)) & (df['season'] > '2006/07')]
df_rest_agg = df_rest.groupby('season')['foreigners'].mean()
df_rest_agg = df_rest_agg.reset_index()
# df_b3_agg = df_b3_agg.sort_values(by='total_market_value', ascending=False)

df_rest_agg.plot(
    kind ='bar',
    x = 'season',
    y = 'foreigners'
)
plt.title('Avg. foreigners i clubs - Other LL clubs')
plt.show()

