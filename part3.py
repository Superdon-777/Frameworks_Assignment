import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

# Load cleaned data from Part 2 - update path as needed
file_path = r"C:\Users\user\Desktop\PLP\_WK3-10_PYTHON_S.ENG\WK 8\metadata.csv"
df = pd.read_csv(file_path)

# Convert 'publish_time' to datetime and extract year (if not already done)
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

# Drop rows with missing year
df = df.dropna(subset=['year'])
df['year'] = df['year'].astype(int)

# Count papers by publication year
papers_per_year = df['year'].value_counts().sort_index()

# Identify top 10 journals publishing COVID-19 research
top_journals = df['journal'].value_counts().head(10)

# Find most frequent words in titles (excluding common stopwords)
titles = df['title'].dropna().str.lower().tolist()
words = []
stopwords = set([
    'the', 'and', 'to', 'of', 'in', 'a', 'for', 'is', 'on', 'with', 
    'by', 'an', 'from', 'at', 'as', 'that', 'this', 'are', 'be', 'or'
])

for title in titles:
    tokens = re.findall(r'\b\w+\b', title)
    words.extend([w for w in tokens if w not in stopwords])

word_freq = Counter(words)
most_common_words = word_freq.most_common(10)

# --- Visualizations ---

# Publications over time
plt.figure(figsize=(10, 5))
plt.bar(papers_per_year.index, papers_per_year.values, color='skyblue')
plt.title('Number of COVID-19 Research Publications by Year')
plt.xlabel('Year')
plt.ylabel('Number of Papers')
plt.xticks(papers_per_year.index)
plt.tight_layout()
plt.show()

# Top 10 Journals Bar Chart
plt.figure(figsize=(10, 5))
top_journals.plot(kind='bar', color='salmon')
plt.title('Top 10 Journals Publishing COVID-19 Research')
plt.ylabel('Number of Papers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Print the most common words in titles
print("Top 10 most frequent words in paper titles (excluding common stopwords):")
for word, count in most_common_words:
    print(f"{word}: {count}")
