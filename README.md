# 📊 CORD-19 Metadata Analysis — Streamlit App

This project is part of the **Python Frameworks Assignment**.  
It analyzes the **CORD-19 metadata dataset** and provides interactive visualizations through a **Streamlit web application**.

---

## 🚀 Live App

🔗 **https://covid-19metadataanalysis.streamlit.app/**  
Use this link to access the deployed web app.

---

## 📂 Project Overview

The goal of this project is to:

- Load and explore the CORD-19 metadata dataset  
- Clean and prepare the data  
- Perform basic analysis  
- Create visualizations  
- Build an interactive Streamlit application to display insights  

The dataset contains information about COVID-19 scientific papers, including:

- Titles  
- Abstracts  
- Publication dates  
- Journals  
- Sources  

---

## 🧪 Features of the Streamlit App

### ✔ 1. Upload Your Own `metadata.csv`
The user can upload the dataset directly through the app interface.

### ✔ 2. Data Cleaning
- Convert `publish_time` to datetime  
- Remove rows with missing titles or publication dates  
- Fill missing journals with "Unknown"  
- Generate abstract word counts  

### ✔ 3. Interactive Filters
Includes a **year range slider** to filter the dataset dynamically.

### ✔ 4. Visualizations Provided
The app generates:

- 📅 **Publications per year** (bar chart)  
- 🏛 **Top 10 journals** (horizontal bar chart)  
- ✍ **Abstract word count histogram**  
- ☁ **Word cloud of paper titles**  

---
CORD-19_Metadata_Analysis/
│── app.py # Streamlit application
│── requirements.txt # Dependencies
│── README.md # Project documentation 
│── notebooks/ # Jupyter analysis 


---

## 📦 Installation (Optional: Run Locally)

1. Clone the repository:

   ```bash
   git clone https://github.com/abbaimam3/CORD-19_Metadata_Analysis.git
   cd CORD-19_Metadata_Analysis


Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py

📥 Using the App

Visit the live link

Upload the metadata.csv file

Explore the charts and insights

Filter results using the sidebar

🔍 Requirements
streamlit
pandas
matplotlib
seaborn
wordcloud

📝 Reflection

This project helped me understand:

Real-world dataset handling

Cleaning and preprocessing large datasets

Building data visualizations

Creating web apps using the Streamlit framework

Deploying apps on Streamlit Cloud

👤 Author

Abba Imam
PLP Academy — Python Frameworks Assignment

✅ Status

✔ Fully deployed
✔ Fully functional
✔ Ready for submission

