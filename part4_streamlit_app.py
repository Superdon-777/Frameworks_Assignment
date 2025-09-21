import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

# Load data
file_path = r"C:\Users\user\Desktop\PLP\_WK3-10_PYTHON_S.ENG\WK 8\metadata.csv"
df = pd.read_csv(file_path)

# Convert 'publish_time' to datetime and extract year
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df = df.dropna(subset=['publish_time'])
df['year'] = df['publish_time'].dt.year.astype(int)

# Streamlit app title and description
st.title("CORD-19 Data Explorer")
st.write("Exploration of COVID-19 research papers metadata")

# Year range selector
min_year = int(df['year'].min())
max_year = int(df['year'].max())
year_range = st.slider("Select publication year range", min_year, max_year, (min_year, max_year))

# Filter data by selected years
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Plot publications over time
pub_counts = filtered_df['year'].value_counts().sort_index()
st.subheader("Publications by Year")
fig1, ax1 = plt.subplots()
ax1.bar(pub_counts.index, pub_counts.values, color='skyblue')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Papers')
st.pyplot(fig1)

# Top journals
top_journals = filtered_df['journal'].value_counts().head(10)
st.subheader("Top 10 Journals")
fig2, ax2 = plt.subplots()
top_journals.plot(kind='bar', ax=ax2, color='salmon')
ax2.set_ylabel("Number of Papers")
ax2.set_xticklabels(top_journals.index, rotation=45, ha='right')
st.pyplot(fig2)

# Frequent words in titles
titles = filtered_df['title'].dropna().str.lower().tolist()
words = []
stopwords = set(['the', 'and', 'to', 'of', 'in', 'a', 'for', 'is', 'on', 'with',
                 'by', 'an', 'from', 'at', 'as', 'that', 'this', 'are', 'be', 'or'])

for title in titles:
    tokens = re.findall(r'\b\w+\b', title)
    words.extend([w for w in tokens if w not in stopwords])

word_freq = Counter(words)
most_common_words = word_freq.most_common(10)

st.subheader("Top 10 Most Frequent Words in Titles")
for word, count in most_common_words:
    st.write(f"{word}: {count}")
