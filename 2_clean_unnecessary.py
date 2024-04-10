import pandas as pd

# Load the data
shares_df = pd.read_csv('cleaned_date_share_info.csv')
users_df = pd.read_csv('cleaned_user_info.csv')

# Find all unique user_ids from both inviter_id and voter_id columns
unique_user_ids = set(shares_df['inviter_id']).union(set(shares_df['voter_id']))

# Filter the users_df to keep only those user_ids that appear in unique_user_ids
final_cleaned_users_df = users_df[users_df['user_id'].isin(unique_user_ids)]

# Save the final cleaned users dataframe to a new CSV file
final_cleaned_users_df.to_csv('final_cleaned_user_info.csv', index=False)

final_cleaned_users_df.head()
