import pandas as pd

# Load the dataset - update path as needed
file_path = r"C:\Users\user\Desktop\PLP\_WK3-10_PYTHON_S.ENG\WK 8\metadata.csv"
df = pd.read_csv(file_path)

# --- Handle missing data ---
# Check missing values per column
missing_counts = df.isna().sum()
print("Missing values per column:")
print(missing_counts[missing_counts > 0])

# Define key columns where missing values are critical - example: 'title', 'publish_time', 'abstract'
key_columns = ['title', 'publish_time', 'abstract']

# Drop rows with missing critical values to create a cleaned dataset
clean_df = df.dropna(subset=key_columns)

print(f"\nOriginal rows: {len(df)}, After cleaning: {len(clean_df)}")

# --- Prepare data for analysis ---
# Convert 'publish_time' to datetime, errors='coerce' will create NaT for invalid dates
clean_df['publish_time'] = pd.to_datetime(clean_df['publish_time'], errors='coerce')

# Extract year from 'publish_time' into a new column 'year'
clean_df['year'] = clean_df['publish_time'].dt.year

# Add a new column for abstract word count
clean_df['abstract_word_count'] = clean_df['abstract'].apply(lambda x: len(str(x).split()))

# Output snapshot to verify
print("\nSample cleaned data:")
print(clean_df[['title', 'publish_time', 'year', 'abstract_word_count']].head())
