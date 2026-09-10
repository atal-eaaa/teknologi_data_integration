import pandas as pd

filepath = r"C:\Users\akch\OneDrive - EFIF\ØKIT Undervisere - Blåt spor\ØKIT-E25AB\3SEM - Teknologi og dataintegration\E26TDIN-05 Bank rust af Python\nyregistrede_biler.csv"

df = pd.read_csv(filepath, sep=',', encoding='utf-8-sig')

df['Count'] = df['Count'].astype('Int64')
df['ID'] = df['ID'].astype('Int64')
df['Month'] = df['Month'].str[1:]
df['Month'] = df['Month'].astype('Int64')
df = df[df['Count'] > 0]
df = df.drop(columns={'Unnamed: 0'})

"""
df[<kolonnenavn>] = df[<kolonnenavn>].astype('Int64')
df[<kolonnenavn>] = df[<kolonnenavn>].str[2:]

df = df[df[<kolonnenavn>] <= 1000]
df = df[(df[<kolonnenavn_1>] <= 1000) & (df[<kolonnenavn_2 == "xxx")]]
df = df[(df[<kolonnenavn_1>] <= 1000) | (df[<kolonnenavn_2 == "xxx")]]
df = df.drop(columns={<kolonnenavn_1>, .., <kolonnenavn_n>})
df = df[<kolonnenavn>].value_counts()
df = df.sort_values(by=[<kolonnenavn_1>, .., <kolonnenavn_n>], ascending=[True, .., False])
x  = df[<kolonnenavn].min()
x  = df[<kolonnenavn].sum()

"""

df1 = df[df['Year'] == df['Year'].max()]
df1 = df1[df1['Month'] == df1['Month'].max()]
print(df1.head())
          

#print(df.head())
#print(df['Year'].min())
#print(df['Drivmiddel'].value_counts())
