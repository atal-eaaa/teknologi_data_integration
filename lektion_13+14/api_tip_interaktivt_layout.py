import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    "Bogstav": ["A", "B", "C"],
    "Tal": [1, 2, 3]
})

df.plot(
    kind ='bar',
    x = 'Bogstav',
    y = 'Tal'
)

plt.show()