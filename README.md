# 📊 COVID-19 Metadata Analysis — Streamlit App

This project is part of the **Python Frameworks Assignment**. It analyzes the **COVID-19 metadata dataset** and provides interactive visualizations through a **Streamlit web application**.

---

## 🚀 Live App

🔗 **[Access the deployed app here](https://covid-19metadataanalysis.streamlit.app/)**

---

## 📂 Project Overview

The goal of this project is to:

- Load and explore the **CORD-19 metadata dataset**
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

- Users can upload the dataset directly through the app interface.

### ✔ 2. Data Cleaning

- Convert `publish_time` to datetime  
- Remove rows with missing titles or publication dates  
- Fill missing journals with `"Unknown"`  
- Generate abstract word counts  

### ✔ 3. Interactive Filters

- **Year range slider** to filter the dataset dynamically

### ✔ 4. Visualizations

- 📅 **Publications per year** (bar chart)  
- 🏛 **Top 10 journals** (horizontal bar chart)  
- ✍ **Abstract word count histogram**  
- ☁ **Word cloud of paper titles**  

---

## 🎬 Preview

*(Add a GIF or screenshot of the app here to showcase functionality)*  

---

## 📦 Installation (Run Locally)

1. **Clone the repository**:

```bash
git clone https://github.com/abbaimam3/CORD-19_Metadata_Analysis.git
cd CORD-19_Metadata_Analysis
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run the app**:

```bash
streamlit run app.py
```

---

## 📥 Using the App

1. Visit the live app link or run locally  
2. Upload the `metadata.csv` file  
3. Explore charts and insights  
4. Filter results using the sidebar  

---

## 🔍 Requirements

```text
streamlit==1.35.0
pandas==2.2.2
numpy==1.26.4
matplotlib==3.9.0
seaborn==0.13.2
wordcloud==1.9.3
```

---

## 📝 Reflection

This project helped me understand:

- Handling real-world datasets  
- Cleaning and preprocessing large datasets  
- Building interactive data visualizations  
- Creating web apps using **Streamlit**  
- Deploying apps on **Streamlit Cloud**  

---

## 👤 Author

**Abba Imam**  
PLP Academy — Python Frameworks Assignment  

---

## ✅ Status

✔ Fully deployed  
✔ Fully functional  
✔ Ready for submission

