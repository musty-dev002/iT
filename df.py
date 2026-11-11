import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "student": ["Musa", "Fatimah", "Aisha", "Ahmad", "Amena", "Aliyu"],
    "score": [82, 70, 50, 65, 90, 45         ]
})

print("----Your df is working----")
print(df)
print("\n---Describe---")
print(df.describe())

df.plot(kind='bar', x='student', y='score')
plt.title("SIWES Test Chart")
plt.show()