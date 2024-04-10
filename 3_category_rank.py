import pandas as pd

# Load the data from CSV files
shares_df = pd.read_csv('cleaned_date_share_info.csv')
items_df = pd.read_csv('clean_item_info_for_use.csv')

# Merge the two datasets on item_id to associate shares with categories
merged_df = shares_df.merge(items_df, on='item_id')

# Group by cate_level1_id and count unique inviter_ids
category_share_counts = merged_df.groupby('cate_level1_id')['inviter_id'].nunique()

# Convert the series to a dataframe for better readability
category_share_counts_df = category_share_counts.reset_index()
category_share_counts_df.columns = ['cate_level1_id', 'unique_shares_count']

# Save the result to a new CSV file
output_file_path = 'category_rank.csv'
category_share_counts_df.to_csv(output_file_path, index=False)

category_share_counts_df.head()
