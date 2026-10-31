import pandas as pd


# EKSEMPEL 1: Konverter en liste af dicts til Pandas DataFrame
data = [
    {"navn": "Anna", "alder": 22},
    {"navn": "Bo", "alder": 25},
    {"navn": "Carl", "alder": 21}
]

df = pd.DataFrame(data)
print(df)



# EKSEMPEL 2: Konverter et dict og dicts til Pandas DataFrame
data = {
    "Anna": {"alder": 22},
    "Bo": {"alder": 25},
    "Carl": {"alder": 21}
}

df = pd.DataFrame.from_dict(data)
print(df)



# EKSEMPEL 3: Konverter et dict of lists til Pandas DataFrame
data = {
    "navn": ["Anna", "Bo", "Carl"],
    "alder": [22, 25, 21]
}

df = pd.DataFrame(data)
print(df)



# EKSEMPEL 4: Konverter en list of lists til Pandas DataFrame
data = [
    ["Anna", 22],
    ["Bo", 25],
    ["Carl", 21]
]

df = pd.DataFrame(
    data,
    columns=["navn", "alder"]
)

print(df)