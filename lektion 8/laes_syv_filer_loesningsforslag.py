import pandas as pd

df_list = []

filename = r'C:\Users\akch\OneDrive - EFIF\ØKIT Undervisere - Blåt spor\ØKIT-E25AB\3SEM - Teknologi og dataintegration\E26TDIN-08 Bank rust af Pandas (I)\efl_league.csv'
df = pd.read_csv(filename, sep=',', encoding='utf-8-sig')
df_list.append(df)

filename = r'C:\Users\akch\OneDrive - EFIF\ØKIT Undervisere - Blåt spor\ØKIT-E25AB\3SEM - Teknologi og dataintegration\E26TDIN-08 Bank rust af Pandas (I)\la_liga.csv'
df = pd.read_csv(filename, sep=';', encoding='utf-8-sig')
df_list.append(df)

filename = r'C:\Users\akch\OneDrive - EFIF\ØKIT Undervisere - Blåt spor\ØKIT-E25AB\3SEM - Teknologi og dataintegration\E26TDIN-08 Bank rust af Pandas (I)\serie_a.csv'
df = pd.read_csv(filename, sep=',', encoding='utf-8-sig')
df_list.append(df)

filename = r'C:\Users\akch\OneDrive - EFIF\ØKIT Undervisere - Blåt spor\ØKIT-E25AB\3SEM - Teknologi og dataintegration\E26TDIN-08 Bank rust af Pandas (I)\league_championat.csv'
df = pd.read_csv(filename, sep=';', encoding='utf-8-sig')
df_list.append(df)

filename = r'C:\Users\akch\OneDrive - EFIF\ØKIT Undervisere - Blåt spor\ØKIT-E25AB\3SEM - Teknologi og dataintegration\E26TDIN-08 Bank rust af Pandas (I)\bundesliga.xlsx'
df = pd.read_excel(filename, sheet_name='BL1')
df_list.append(df)

filename = r'C:\Users\akch\OneDrive - EFIF\ØKIT Undervisere - Blåt spor\ØKIT-E25AB\3SEM - Teknologi og dataintegration\E26TDIN-08 Bank rust af Pandas (I)\bundesliga.xlsx'
df = pd.read_excel(filename, sheet_name='BL2')
df_list.append(df)

filename = r'C:\Users\akch\OneDrive - EFIF\ØKIT Undervisere - Blåt spor\ØKIT-E25AB\3SEM - Teknologi og dataintegration\E26TDIN-08 Bank rust af Pandas (I)\premier_league.xlsx'
df = pd.read_excel(filename, sheet_name='PL')
df_list.append(df)



for df in df_list:
    if list(df.columns) == list(df_list[0].columns):
        print("-> OK", list(df.columns ))
    else:
        print("-> FORSKEL!", list(df.columns))

df = pd.concat(df_list, ignore_index=True)

print(len(df))

filename = r'all_leagues.csv'
df.to_csv(filename, sep=',', index=False, encoding='utf-8-sig')

print("--- DONE ---")