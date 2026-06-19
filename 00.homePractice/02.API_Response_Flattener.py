import pandas as pd

api_response = [
    {
        "user_id": 101,
        "username": "w_jemal",
        "profile": {"role": "Web Developer", "dept": "Engineering"},
        "activity": {"logins": 142, "status": "active"}
    },
    {
        "user_id": 102,
        "username": "a_smith",
        "profile": {"role": "UI Designer", "dept": "Design"},
        "activity": {"logins": 54, "status": "inactive"}
    },
    {
        "user_id": 103,
        "username": "j_doe",
        "profile": {"role": "Data Scientist", "dept": "Engineering"},
        "activity": {"logins": 210, "status": "active"}
    }
]

print(type(api_response), "Containing: " , type(api_response[0]))


# Flaten the nested dictionaries to columns
df_flat = pd.json_normalize(api_response)
print(df_flat)

print(df_flat.columns)

# 3. Rename columns to replace dot notation with clean snake_case
df_clean = df_flat.rename(columns={
    'profile.role':"role", 
    'profile.dept':"department",
    'activity.logins':"login_count",
    'activity.status':"status"
})

print(df_clean)

# Remove the unwanted column

df_final = df_clean.drop(columns=["status"])

print(df_final)
