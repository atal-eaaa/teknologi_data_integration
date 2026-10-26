# %%
import pandas as pd
import matplotlib.pyplot as plt
f_name = r"C:\Users\akch\OneDrive - EFIF\Fag\3 - Blåt spor\26E - Teknologi- og Dataintegration\teknologi_data_integration\Lektion 9\wildfires_with_owid_regions.csv"


df = pd.read_csv(f_name, sep=",", encoding='utf-8-sig')

print(df.head())

# %%
df_year = df[(df['week'] ==  52)] 
df_year = df_year.sort_values(by='year')


# %%

print(df['code'].unique())


# %%

df_plt = df_year[df_year['code'] == 'OWID_WRL'] 

plt.figure(figsize=(10, 5))
plt.plot(df_plt['year'], df_plt['acc_hectares_burned'], marker="o")
plt.title('Areal afbrændt ved naturbrande - hele verden')
plt.ylabel('100 mio Ha')

plt.show()

# %%

df_plt = df_year[df_year['code'] == 'OWID_EU27'] 

plt.figure(figsize=(10, 5))
df_plt.plot(
    kind='bar',
    x = 'year', 
    y = 'acc_hectares_burned'
)
plt.title('Areal afbrændt ved naturbrande - hele verden')
plt.ylabel('Mio. Ha')

plt.show()
# %%

df_plt = df_year[df_year['code'] == 'ESP'] 

plt.figure(figsize=(10, 5))
df_plt.plot(
    kind='bar',
    x = 'year', 
    y = 'acc_hectares_burned'
)
plt.title('Areal afbrændt ved naturbrande - Spanien')
plt.ylabel('Ha')

plt.show()
# %%
