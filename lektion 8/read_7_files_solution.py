import pandas as pd
import os

workdir = os.getcwd() 
folder_path = workdir + r'/lektion 8/' 
concat_and_save = True
df_list = []

data_files_excel = [['bundesliga.xlsx', 'BL1'], ['bundesliga.xlsx', 'BL2'], ['premier_league.xlsx', 'PL']]  # [[file name, sheet name]]
data_files_csv = [['efl_league.csv', ','], ['la_liga.csv',';'], ['serie_a.csv',','], ['league_championat.csv',';'] ] # [[file name, sep]]

# load csv files
for filename, separator in data_files_csv:
    df = pd.read_csv(folder_path + filename, sep=separator, encoding='utf-8-sig')
    df_list.append(df)

# load excel files
for filename, sheetname  in data_files_excel:
    df = pd.read_excel(folder_path + filename, sheet_name=sheetname)
    df_list.append(df)

# check column names before concat 
for df in df_list:
    if list(df.columns) == list(df_list[0].columns):
        print("-> OK", list(df.columns ))
    else:
        print("-> FORSKEL!", list(df.columns))
        concat_and_save = False # don't concat when columns don't match

if concat_and_save:
    df = pd.concat(df_list, ignore_index=True)
    print(len(df))
    filename = r'all_leagues.csv'
    df.to_csv(folder_path + filename, sep=',', index=False, encoding='utf-8-sig')
    print("--- DONE ---")