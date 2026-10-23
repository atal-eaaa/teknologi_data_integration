

# Klargør til øvelsen
# -----------------------------------------------------------------

import json

filename = r"C:\Users\akch\OneDrive - EFIF\ØKIT Undervisere - Blåt spor\ØKIT-E25AB\3SEM - Teknologi og dataintegration\E26TDIN-11 Dictionaries og JSON\hjemmeopgave.json"

with open(filename, 'r', encoding='utf-8-sig') as f:
    data = json.load(f)


# Spørgsmål 1:
# -----------------------------------------------------------------

kundenr = input("Tast kundenummer :")
if kundenr in data['customers'].keys():
    print(f'Kundenummer : {kundenr} :')
    print('-' * 50)
    for key, oplysning in data['customers'][kundenr].items():
        print(f'{key} :  {oplysning}')    
    print('-' * 50)

else:
    print('kunden findes ikke i kundebasen')            




# Spørgsmål 2:    
# -----------------------------------------------------------------

print('\n\n Ordrestatistik :')
print('-' * 50)
for kundenr in data['customers'].keys():
    antal_ordrer = 0
    for ordrenr, ordre in data['orders'].items():
        if ordre['customer_id'] == kundenr:
            antal_ordrer += 1
    print(f'Kundenummer {kundenr} : {antal_ordrer}')    
print('-' * 50)




# Spørgsmål 3:    
# -----------------------------------------------------------------

print('\n\n Største kunde :')
print('-' * 50)
storste_kunde = ''
storste_omsaetning = 0
for kundenr in data['customers'].keys():
    omsaetning = 0
    for ordrenr, ordre in data['orders'].items():
        if ordre['customer_id'] == kundenr:
            for line in ordre['order_lines']:  
                omsaetning += line['amount']
    if omsaetning > storste_omsaetning:
        storste_kunde = kundenr    
        storste_omsaetning = omsaetning
    
    print(f"Kundenummer {storste_kunde} {data['customers'][storste_kunde]['name']}: {storste_omsaetning}")    
print('-' * 50)