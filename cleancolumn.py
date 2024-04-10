# To remove the 'cate_id' column from a CSV file, you can use the pandas library in Python.
# Here's a script that reads the CSV, drops the 'cate_id' column, and then saves the modified DataFrame back to a CSV file.

import pandas as pd

# Path to the CSV file
csv_file_path = './cleaned_item_info.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Drop the 'cate_id' column
df = df.drop('cate_id', axis=1)

# Save the modified DataFrame back to a new CSV file
output_file_path = 'clean_item_info_for_use.csv'
df.to_csv(output_file_path, index=False)


