import pandas as pd
import os

# Provide the relative or full absolute path to the metadata.csv file
# Replace this with the actual full path of your metadata.csv file
file_path = r"C:\Users\user\Desktop\PLP\_WK3-10_PYTHON_S.ENG\WK 8\metadata.csv\metadata.csv"

# Print current working directory and the target file path for debugging
print("Current working directory:", os.getcwd())
print("Attempting to read file from:", file_path)

try:
    # Load the file with the absolute path
    df = pd.read_csv(file_path)
    
    print("First 5 rows:")
    print(df.head())

    print("\nDataset size (rows, columns):", df.shape)

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values per column:")
    print(df.isna().sum())

    print("\nBasic statistics for numerical columns:")
    print(df.describe())

except PermissionError:
    print("Permission denied: Ensure no program (Excel, etc) is currently using the file and you have read access.")
except FileNotFoundError:
    print("File not found: Check the file path and name are correct.")
except Exception as e:
    print("An error occurred:", e)
