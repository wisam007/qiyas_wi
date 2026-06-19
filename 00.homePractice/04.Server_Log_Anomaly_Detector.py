import pandas as pd
import numpy as np

# 1. Create a dictionary representing raw out-of-order server logs
log_data = {
    'timestamp': ['2026-06-11 12:00:00', '2026-06-11 12:05:00', '2026-06-11 12:01:00', '2026-06-11 12:10:00', '2026-06-11 12:15:00'],
    'request_count': [120, 1500, 95, 110, 3200]  # Normal traffic vs unexpected spikes
}

df_logs = pd.DataFrame(log_data)

print("--- Step 1: Raw String Logs ---")
print(df_logs.dtypes)  # Shows 'timestamp' is just a generic object/string

df_logs["timestamp"] = pd.to_datetime(df_logs["timestamp"])

print(df_logs)
df_logs = df_logs.set_index('timestamp')
print(df_logs)

df_logs = df_logs.sort_index()
print(df_logs)

print("Index Type:", type(df_logs.index))