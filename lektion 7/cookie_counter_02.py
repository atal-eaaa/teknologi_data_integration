amount       = [2, 3, 1, 5, 3, 2, 1, 3, 6, 1, 1, 2, 3]
cookie_type  = ['Chokolade', 'Chokolade','Nødder','Vanilje', 'Nødder','Vanilje', 'Chokolade','Nødder', 'Vanilje','Nødder','Chokolade','Vanilje','Vanilje']
cookie_types = ['Chokolade', 'Vanilje', 'Nødder']
cookie_price = [3.00, 1.50, 2.50]



# DAN UNIT_PRICE_LIST
# -----------------------------------------------------

unit_price = []
for cookie in cookie_type:
    idx = cookie_types.index(cookie)
    price = cookie_price[idx]
    unit_price.append(price)
print(unit_price)    


# DAN TO_PAY_LIST
# -----------------------------------------------------

to_pay = []
for idx, price in enumerate(unit_price):
    total = amount[idx] * price
    to_pay.append(total)
print(to_pay)
  
