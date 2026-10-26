# %%

import pandas as pd
import matplotlib.pyplot as plt

filename = "all_leagues.csv"

df = pd.read_csv(filename, sep=',', encoding='utf-8-sig')
print("--- DONE --- ")

# %%

df_sa     = df[df['tier'] == 'SA']
df_sa_agg = df_sa.groupby('season')['squad'].mean()
df_sa_agg = df_sa_agg.reset_index()

df_sa_agg.plot(
    kind ='bar',
    x = 'season',
    y = 'squad'
)
plt.show()


# %%

df_other = df[df['tier'] != 'SA']
df_other_agg = df_other.groupby('season')['squad'].mean()
df_other_agg = df_other_agg.reset_index()

df_other_agg.plot(
    kind ='bar',
    x = 'season',
    y = 'squad'
)
plt.show()




# %%
print(df_agg)

df_2025 = df[df['season'] == '2025/26']
df_agg = df_2025.groupby('tier')['squad'].agg(['mean', 'median'])
print(df_agg)


# %%
