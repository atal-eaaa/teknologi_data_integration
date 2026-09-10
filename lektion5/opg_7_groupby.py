import pandas as pd

filepath = r"C:\Users\akch\OneDrive - EFIF\ØKIT Undervisere - Blåt spor\ØKIT-E25AB\3SEM - Teknologi og dataintegration\E26TDIN-05 Bank rust af Python\nyregistrede_biler.csv"

df = pd.read_csv(filepath, sep=',', encoding='utf-8-sig')

year  = 2026
# df = df[(df['Year'] == year) & (df['Segment'] == 'Personbil')]

df_agg = df.groupby(['Producent_nationalitet'])['Count'].sum()
df_agg = df_agg.reset_index()
df_agg['Count'] = df_agg['Count'].astype('Int64')
df_agg['Markedsandel'] = round(df_agg['Count'] / df_agg['Count'].sum() * 100,1)



print(df_agg)


