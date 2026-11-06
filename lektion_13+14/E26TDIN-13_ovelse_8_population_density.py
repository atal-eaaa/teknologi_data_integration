#%%
import requests
from pprint import pprint
import matplotlib.pyplot as plt

url     = 'https://api.restcountries.com/countries/v5'
headers = {'Authorization': 'Bearer XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' } 



# %%

params = { 
    'codes.alpha_3' : 'DNK'
}
r      = requests.get( url, params=params, headers=headers)
data   = r.json()
pprint(data)




# %%

countries          = ['Germany', 'Norway' , 'Holland', 'Denmark', 'Belgium']
iso_3_codes        = ['DEU', 'NOR', 'NLD', 'DNK', 'BEL']
population_density = []

for iso_3_code in iso_3_codes:

    params = { 
        'codes.alpha_3' : iso_3_code
    }
    r      = requests.get( url, params=params, headers=headers)
    data   = r.json()

    if r.status_code == 200:
        # pprint(data['data']['objects'][0])
        
        population = data['data']['objects'][0]['population']
        area       = data['data']['objects'][0]['area']['kilometers']
        density    = population / area
        population_density.append(density)
    else:
        print('Fejl')    


plt.bar(countries, population_density)





#%%


url = 'https://api.restcountries.com/countries/v5'
nor = ""
# params = { 'names.common' : 'Norway'}
params = { 'codes.alpha_3' : 'NOR'}
r      = requests.get( url, params=params, headers=headers)
nor    = r.json()


# %%

pprint(nor)
# %%
