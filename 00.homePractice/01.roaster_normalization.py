import pandas as pd
import numpy as np


data = {
    'Player_Name': ['Wissam', 'Alex', 'Jordan', 'Taylor', 'Morgan'],
    'Sprint_Speed': [85, 92, 60, 78, 99],       # Scale: ~0 to 100
    'Pass_Accuracy': [750, 420, 910, 680, 810]  # Scale: ~0 to 1000
}
df = pd.DataFrame(data)
print(df)
# Step 2: Isolate the Target Columns

target_cols = ['Sprint_Speed', 'Pass_Accuracy']

df_numerical = df[target_cols]
print(df_numerical)

normalized_values = (df_numerical - df_numerical.min())/ (df_numerical.max() - df_numerical.min())

print(normalized_values)

df[target_cols] = normalized_values

print(df)
