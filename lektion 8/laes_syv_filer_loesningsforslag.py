import pandas as pd

df_list = []

filename = r'<Sti til filen - der hvor du har lagt den>'
df = pd.read_csv(filename, sep=',', encoding='utf-8-sig')
df_list.append(df)

filename = r'<Sti til filen - der hvor du har lagt den>'
df = pd.read_csv(filename, sep=';', encoding='utf-8-sig')
df_list.append(df)

filename = r'<Sti til filen - der hvor du har lagt den>'
df = pd.read_csv(filename, sep=',', encoding='utf-8-sig')
df_list.append(df)

filename = r'<Sti til filen - der hvor du har lagt den>'
df = pd.read_csv(filename, sep=';', encoding='utf-8-sig')
df_list.append(df)

filename = r'<Sti til filen - der hvor du har lagt den>'
df = pd.read_excel(filename, sheet_name='BL1')
df_list.append(df)

filename = r'<Sti til filen - der hvor du har lagt den>'
df = pd.read_excel(filename, sheet_name='BL2')
df_list.append(df)

filename = r'<Sti til filen - der hvor du har lagt den>'
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