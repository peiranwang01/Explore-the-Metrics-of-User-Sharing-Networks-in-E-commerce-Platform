import pandas as pd
import json

# Replace this with the actual path to your JSON file
file_path = '/Users/patrickw/Downloads/CourseWork/Network/data/item_share_final_train_info.json'

def load_and_clean_json_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Create a DataFrame from the loaded data
        df = pd.DataFrame(data)

        # Convert the 'timestamp' column to datetime objects
        df['timestamp'] = pd.to_datetime(df['timestamp'])

        # If there are any missing values, decide how to handle them
        # For example, you could fill with a placeholder or the most common value
        # Here, we'll leave the missing value handling strategy to your discretion

        # Validate the data types of your columns (e.g., ensuring IDs are strings)
        df['inviter_id'] = df['inviter_id'].astype(str)
        df['item_id'] = df['item_id'].astype(str)
        # If there are other fields like 'voter_id', convert them as well

        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()

# Clean the data
cleaned_data = load_and_clean_json_data(file_path)

# Save the cleaned data to a CSV file
# Replace this with the actual path where you want to save the CSV
save_csv_path = '/Users/patrickw/Downloads/CourseWork/Network/data/cleaned_final_train_info.csv'
if not cleaned_data.empty:
    cleaned_data.to_csv(save_csv_path, index=False)
    print(f"Cleaned data saved to {save_csv_path}")
else:
    print("No data was loaded or cleaned.")
