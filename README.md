# Frameworks_Assignment
Final Project PLP WK 8::
COVID-19 Data Exploration and Visualization Project
Project Overview
This project provides a beginner-friendly end-to-end analysis and interactive visualization of COVID-19 research metadata using Python. It leverages the COVID-19 dataset to perform fundamental data science tasks including data loading, cleaning, exploratory analysis, visualization and creating a simple web app for user interaction.

Key Features::
Data Loading & Cleaning: Basic handling of missing data and date parsing for publication times.

Exploratory Analysis: Counting publications per year, identifying top journals, and extracting frequent words in paper titles.

Visualizations: Bar charts for publication trends over time and journal popularity.

Interactive Web App: Streamlit application allowing users to filter data by publication year and explore insights interactively.

Technologies Used::
Python 3.7+

pandas for data manipulation

matplotlib for visualizations

Streamlit for building the interactive application

Getting Started::
Clone the repository and download the metadata.csv file from the COVID-19 dataset.

Install dependencies:

bash
pip install pandas matplotlib streamlit
Run analysis scripts sequentially::

part1.py — Data loading and basic exploration

part2.py — Data cleaning and preparation

part3.py — Analysis and visualization

Launch the Streamlit app to interact with the data::

bash
streamlit run part4_streamlit_app.py

Reflection and Challenges::
This project introduced working with a real-world large dataset, building confidence in data cleaning and exploratory analysis. Handling missing or inconsistent data and transforming date fields were key learning points. The visualizations offered clear insights, and building the Streamlit app helped connect data science with user-centric presentation.

Future improvements could include advanced text analysis like topic modeling or NLP, and more sophisticated interactive visual components.
