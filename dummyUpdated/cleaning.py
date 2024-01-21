import pandas as pd
import numpy as np

df = pd.read_excel('third.xlsx')

# Extract column names as a NumPy array
coli_array = df.columns.to_numpy()

# cleaned_coli_array = np.char.replace(coli_array, '.', '').replace('"', '')

for i in coli_array:
    print(i)

coli = np.sort(coli_array)

for i in coli:
    print(i)

