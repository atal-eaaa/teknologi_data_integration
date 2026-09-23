kobesum = 437.50
rabat_kode = True
kunde_segment = "GOLD"


if kobesum >= 400 and kunde_segment == 'GOLD':
    rabat_sats = 0.2  # 20% rabat
elif kobesum >= 500 and (kunde_segment == 'SILVER' or kunde_segment == 'BRONZE'):
    rabat_sats = 0.1  # 10% rabat
elif rabat_kode == True and kunde_segment != 'BRONZE':
    rabat_sats = 0.07 # 7% rabat
elif (kobesum >= 500 and kunde_segment == 'BRONZE') or (kobesum > 400 and kunde_segment=='SILVER'):   
    rabat_sats = 0.06 # 6% rabat
else:
    rabat_sats = 0    # 0% rabat   

