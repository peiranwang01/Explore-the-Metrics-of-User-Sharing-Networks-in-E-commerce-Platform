import pandas as pd
from datetime import datetime

# Load the data
# Assuming the CSV file is named 'data.csv' and is in the current working directory.
df = pd.read_csv('./cleaned_item_share_train_info.csv')

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Filter data for the given date range
start_date = "2021-12-27"
end_date = "2022-4-30"

# Mask to filter dataframe
mask = (df['timestamp'] >= start_date) & (df['timestamp'] <= end_date)
filtered_df = df.loc[mask]

# Save the filtered data to a new CSV file
filtered_df.to_csv('./cleaned_date_share_info.csv', index=False)
