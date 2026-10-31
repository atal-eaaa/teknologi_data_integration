import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude"        : 56.1629,
    "longitude"       : 10.2039,
    "hourly"          : "temperature_2m,relative_humidity_2m,wind_speed_10m,wind_speed_100m,sunshine_duration",
    "wind_speed_unit" : "ms",
    "past_days"       : 1,
    "timezone"        : "auto",
    "format"          : "json",
    "limit"           : 5
}
response = requests.get(url, params=params)
data1 = response.json()

#pprint(data1)


for key, item in data1.items():
    print( key, item)





"""

DOKUMENTATION 
|----------------------------------------------------------------------------------------------------|
|                                                                                                    |     
| https://open-meteo.com/en/docs                                                                     |
|                                                                                                    |     
|----------------------------------------------------------------------------------------------------|



|----------------------------------------------------------------------------------------------------|
| Grundelementer i kaldet                                                                            |
|----------------------------------------------------------------------------------------------------|
| variable                                  | Beskrivelse                                            |
| ----------------------------------------- | ------------------------------------------------------ |
| latitude,longitude:                       | WGS84-koordinater                                      |
| elevation                                 | Valgfri højde over havet (m)                           |
| timezone:                                 | auto for lokal tid (Danmark / CEST), eller f.eks. UTC  |
| format:                                   | csv eller json                                         |
| ----------------------------------------- | ------------------------------------------------------ |


|----------------------------------------------------------------------------------------------------|
| Tid                                                                                                |
|----------------------------------------------------------------------------------------------------|
| variable                                  | Beskrivelse                                            |
| ----------------------------------------- | ------------------------------------------------------ |
| past_days:                                | Antal dage historiske data (0–92)                      |
| forecast_days:                            | Fremtidige prognosedage (0–16)                         |
| forecast_hours, past_hours,               | Finere kontrol over antal tidssteg (minutter/time)     |
| past_minutely_15, forecast_minutely_15:   |                                                        |
| ----------------------------------------- | ------------------------------------------------------ |


|----------------------------------------------------------------------------------------------------|
| Forecast / historik                                                                                |
|----------------------------------------------------------------------------------------------------|
| variable                                  | Beskrivelse                                            |
| ----------------------------------------- | ------------------------------------------------------ |
| hourly:                                   | Liste over timeværdier (se liste)                      |
| daily:                                    | Liste over døgndata                                    |
| current:                                  | Øjebliksværdier                                        |
| ----------------------------------------- | ------------------------------------------------------ |


|----------------------------------------------------------------------------------------------------|
| Hourly-parametre                                                                                   |
|----------------------------------------------------------------------------------------------------|
| variable                                                       | Beskrivelse                       |
| -------------------------------------------------------------- | --------------------------------- |
| `temperature_2m`                                               | Temperatur ved 2 m højde          |
| `relative_humidity_2m`                                         | Relativ luftfugtighed             |
| `windspeed_10m`                                                | Vindhastighed ved 10 m            |
| `winddirection_10m`                                            | Vindretning ved 10 m              |
| `pressure_msl`                                                 | Lufttryk (mean sea level)         |
| `cloudcover`                                                   | Sky­dække som brøkdel              |
| `precipitation`                                                | Sum af nedbør de seneste timer    |
| `sunshine_duration`                                            | Solbeskinnet varighed             |
| `uv_index`                                                     | Ultraviolet indeks                |
| `uv_index_clear_sky`                                           | UV indeks uden skyer              |
| `is_day`                                                       | Dag-/natflag                      |
| `wet_bulb_temperature`                                         | Temperatur ved konstant fugtighed |
| `total_columns_integrated_water_vapour`                        | Vanddamp kolonne-integreret       |
| `cape`, `lifted_index`, `convective_inhibition`                | Convective stability parametre    |
| `freezing_level_height`                                        | Fryse-niveau højde                |
| `boundary_layer_height_pbl`                                    | Planetarisk grænselagshøjde       |
| `soil_temperature_0cm_to_2cm`, `soil_moisture_10cm_to_40cm`, … | Jordfugtighed og temperatur i lag |
|----------------------------------------------------------------------------------------------------|


"""