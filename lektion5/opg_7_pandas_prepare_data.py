import pandas as pd

filepath_in = r"C:\Users\akch\OneDrive - EFIF\ØKIT Undervisere - Blåt spor\ØKIT-E25AB\3SEM - Teknologi og dataintegration\E26TDIN-05 Bank rust af Python\nyregistrede_biler_raw.csv"
filepath_out = r"C:\Users\akch\OneDrive - EFIF\ØKIT Undervisere - Blåt spor\ØKIT-E25AB\3SEM - Teknologi og dataintegration\E26TDIN-05 Bank rust af Python\nyregistrede_biler.csv"
delim    = ','

df = pd.read_csv(filepath_in, sep=delim, encoding="utf_8_sig")
print(len(df))

df = df[df['Month'].str.startswith('M')]
# df = df[df['Count'] > 0]


print(df.head())
print(len(df))

df.to_csv(filepath_out, sep=delim, encoding='utf-8-sig')
print('--- DONE ---')