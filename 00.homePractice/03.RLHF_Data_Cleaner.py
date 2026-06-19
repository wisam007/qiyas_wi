import pandas as pd 
import numpy as np

raw_rlhf_data = {
    'prompt': ['  Write a python loop   ', 'Explain gravity simply', ' how to bake bread? ', 'Write a poem about AI'],
    'chosen_response': ['Here is the loop...', 'Gravity is a force...', np.nan, 'Silicon minds wander...'],
    'rejected_response': ['Looping is done by...', None, 'Mix flour and water.', 'Error: cannot compute']
}

df = pd.DataFrame(raw_rlhf_data)

print(df)
print("\n" + "="*50 + "\n")

# Drop empty sections
df_dropped = df.dropna(subset=["chosen_response","rejected_response"])

print(df_dropped)
print("\n" + "="*50 + "\n")

# Create a copy to prevent SettingWithCopyWarning

df_clean = df_dropped.copy()
# 4. Strip whitespace and enforce lowercase consistency across text features
df_clean["prompt"] = df_clean['prompt'].str.strip().str.lower()

df_clean["choosen_response"] = df_clean['chosen_response'].str.strip()

print(df_clean)
print("\n" + "="*50 + "\n")



df_clean["prompt_length"] = df_clean["prompt"].str.len()

print(df_clean)