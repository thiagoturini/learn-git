import pandas as pd
import numpy as np

data = [{"product": "tennis Adidas", "quatity": 1, "value": 120.99},
        {"product": "tennis YYYY", "quatity": 1, "value": 150.99},
        {"product": "sticker", "quatity": 1, "value": 1.99},
        {"product": "socks", "quatity": 1, "value": 10.99},
        {"product": "socks WWW", "quatity": 1, "value": 20.99},
        {"product": "tennis ZZZZ", "quatity": 1, "value": 120.99}]



df = pd.DataFrame(data)
print(df)
min_value = df['value'].min()
max_value = df['value'].max()

Q3, Q1 = np.percentile(df['value'], [75, 25])
IQR = Q3 - Q1
print(f"The IQR is: {IQR}")
