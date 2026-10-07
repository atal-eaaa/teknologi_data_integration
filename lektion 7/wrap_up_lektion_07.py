# ØVELSE 1:
# -------------------------------

import statistics as sts
units_sold  = [100, 350, 200, 400]
lst = []
for i in range(len(units_sold)):
    if i >= 2:
        lst.append(units_sold[i])

x = sts.mean(lst)
print(x)




# ØVELSE 2:
# -------------------------------

import statistics as sts
units_sold  = [100, 350, 200, 250, 400]
lst = []
for units in units_sold:
    if units >= 150 and units <= 350:
        lst.append(units)
x = sts.median(lst)
print(x)




# ØVELSE 3:
# -------------------------------

units_sold  = [100, 350, 200, 250, 400]
products     = ['Bananas', 'Apples', 'Pears', 'Oranges', 'Grapes']

lst = []
idx = products.index('Pears')
x = units_sold[idx]
print(x)




# ØVELSE 4:
# -------------------------------

products    = ['Bananas', 'Apples', 'Pears', 'Oranges', 'Grapes']
price_list  = [10, 20, 15, 25, 30]
amount_sold = [1, 3, 2, 2, 4]

total_sales = price_list[products.index('Apples')] * amount_sold[products.index('Apples')]
print(total_sales)


# ØVELSE 5:
# -------------------------------

products    = ['Bananas', 'Apples', 'Pears', 'Oranges', 'Grapes']
x = 0
for idx, product in enumerate(products):
    x += idx
print(x)




# ØVELSE 6:
# -------------------------------

products    = ['Bananas', 'Apples', 'Pears', 'Oranges', 'Grapes']
price_list  = [10, 20, 15, 25, 30]
amount_sold = [1, 3, 2, 2, 4]
total_sales = 0 
for idx, product in enumerate(products):
    if product > "Melons" :
        total_sales += price_list[idx] * amount_sold[idx]
print(total_sales)