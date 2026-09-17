sales = [
    ['East', 300], 
    ['East', 600], 
    ['West', 100], 
    ['North', 600], 
    ['West', 200], 
    ['North', 400], 
    ['South', 500], 
    ['East',300]
]

r_w = 0
r   = 0
for sale in sales:
    if sale[0] == "West":
        r_w += sale[1]
    r += sale[1]
s = r_w / r * 100    

print( r_w, r, s)


