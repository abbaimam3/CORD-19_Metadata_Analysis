# paste the full Streamlit code here
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# ----------------------------------------------------
# STREAMLIT APP LAYOUT
# ----------------------------------------------------

st.set_page_config(page_title="CORD-19 Explorer", layout="wide")

st.title("📊 CORD-19 Research Dataset Explorer")
st.write("""
This application allows you to explore the **CORD-19 metadata dataset**.  
You can filter the data, view visualizations, and interact with the results.
""")

# ----------------------------------------------------
# UPLOAD SECTION
# ----------------------------------------------------

uploaded_file = st.file_uploader("Upload metadata.csv file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("Dataset loaded successfully!")

    # Basic cleaning
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df = df.dropna(subset=['publish_time', 'title'])
    df['year'] = df['publish_time'].dt.year
    df['journal'] = df['journal'].fillna("Unknown")
    df['abstract'] = df['abstract'].fillna("")
    df['abstract_word_count'] = df['abstract'].apply(lambda x: len(x.split()))

    # ----------------------------------------------------
    # SIDEBAR FILTERS
    # ----------------------------------------------------

    st.sidebar.header("Filters")

    min_year = int(df['year'].min())
    max_year = int(df['year'].max())

    year_range = st.sidebar.slider(
        "Select Year Range",
        min_year,
        max_year,
        (min_year, max_year)
    )

    # Filter data by year
    df_filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

    # ----------------------------------------------------
    # SHOW DATA SAMPLE
    # ----------------------------------------------------

    st.subheader("📄 Data Sample")
    st.write(df_filtered.head())

    # ----------------------------------------------------
    # VISUALIZATION: Publications per Year
    # ----------------------------------------------------

    st.subheader("📅 Publications by Year")

    year_counts = df_filtered['year'].value_counts().sort_index()

    fig1, ax1 = plt.subplots(figsize=(10,5))
    ax1.bar(year_counts.index, year_counts.values)
    ax1.set_title("Publications per Year")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Number of Papers")
    st.pyplot(fig1)

    # ----------------------------------------------------
    # VISUALIZATION: Top Journals
    # ----------------------------------------------------

    st.subheader("🏛️ Top 10 Journals")

    top_journals = df_filtered['journal'].value_counts().head(10)

    fig2, ax2 = plt.subplots(figsize=(12,6))
    sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax2)
    ax2.set_title("Top 10 Journals Publishing COVID-19 Papers")
    ax2.set_xlabel("Number of Papers")
    ax2.set_ylabel("Journal")
    st.pyplot(fig2)

    # ----------------------------------------------------
    # VISUALIZATION: Abstract Word Count Histogram
    # ----------------------------------------------------

    st.subheader("📝 Abstract Word Count Distribution")

    fig3, ax3 = plt.subplots(figsize=(10,5))
    ax3.hist(df_filtered['abstract_word_count'], bins=40)
    ax3.set_title("Distribution of Abstract Word Count")
    ax3.set_xlabel("Word Count")
    ax3.set_ylabel("Frequency")
    st.pyplot(fig3)

    # ----------------------------------------------------
    # WORD CLOUD OF TITLES
    # ----------------------------------------------------

    st.subheader("☁ Word Cloud of Paper Titles")

    titles_text = " ".join(df_filtered['title'].tolist())

    wordcloud = WordCloud(width=1200, height=600, background_color='white').generate(titles_text)

    fig4, ax4 = plt.subplots(figsize=(14,7))
    ax4.imshow(wordcloud, interpolation='bilinear')
    ax4.axis("off")
    st.pyplot(fig4)

else:
    st.warning("Please upload metadata.csv to begin.")
