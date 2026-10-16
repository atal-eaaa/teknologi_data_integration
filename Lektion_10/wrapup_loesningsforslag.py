import pandas as pd

df = pd.read_excel(r'biografbilletter_2025.xlsx')

#%% 
# inspicer data

# df.info()
# print(df.head())


#%% 
# Hvor mange tyske film havde premiere i danske biografer i 2025? 
len(df[(df.LAND_NAVN == 'TYSKLAND') & (df.premiereaar == 2025)])


#%%
# Hvor mange tyske film havde premiere i andet halvår af 2025?

df_tyskland_2025_H2 = df[(df.LAND_NAVN == 'TYSKLAND') & (df.premiereuge > 26) & (df.premiereaar == 2025)]
len(df_tyskland_2025_H2)

# %%
# Hvor mange danske film, tilladt over 11 år med premiere i 2024 opnåede et salg på mere end 50.000 billetter?

tilladt_over_11_kolonner = ['Tilladt for børn over 11 år', 'Frarådet for børn under 7 år', 'Tilladt for alle' ]

df_dansk_over11_2024_over50k = df[(df.nationalitet == 'DAN') & 
                                  (df.premiereaar == 2024) & 
                                  (df.solbil > 50000) & 
                                  (df.CENSUR.isin(tilladt_over_11_kolonner))] 

len(df_dansk_over11_2024_over50k)


#%%
# Hvor mange film havde premiere i uge 7, 42 eller 52 i 2021-2023?
len(df[(df.premiereuge.isin([7, 42, 52])) & (df.premiereaar.isin([2021,2022,2023]))])

#%%
# Hvor mange engelske eller franske spillefilm for voksne har haft premiere siden 1. januar 2022?
len(df[(df.nationalitet.isin(['FRA', 'STO'])) & (df.premiereaar >= 2022)])

#%%
# Hvor mange ikke-amerikanske film med en spilletid på mere end 120 minutter har haft efter uge 26 i 2024 og frem til udgangen af 2025?
tidsperiode = ((df.premiereaar == 2024) & (df.premiereuge > 26)) | (df.premiereaar == 2025) # enten over uge 26 i år 2024 eller år 2025
len(df[(df.nationalitet != 'USA') & (df.LAENGDE > 120) & tidsperiode])


# %%
# Hvor mange forskellige lande kom premierefilmene fra? 
df.nationalitet.nunique()

#%%
# Og hvor mange fra hvert land?
df.nationalitet.value_counts()
