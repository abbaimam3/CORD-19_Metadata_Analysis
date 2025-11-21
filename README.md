# 📊 CORD-19 Research Dataset Explorer

A Streamlit web application that allows users to upload and explore the **CORD-19 metadata dataset**.  
The app provides filtering options, visualizations, and insights generated from the dataset.

---

## 🚀 Features

### ✅ **Upload & Load Dataset**
- Upload your own `metadata.csv` file (from the CORD-19 Kaggle dataset or any dataset with similar columns).
- Automatically cleans:
  - Missing publish dates
  - Missing titles
  - Missing journal names
  - Missing abstracts

---

## 📁 **Data Processing**
The app performs:
- Date parsing and extraction of publication year
- Abstract word count calculation
- Dropping invalid rows
- Basic exploratory data analysis

---

## 📊 **Visualizations**
The app includes **four key visualizations**:

1. **Publications per Year (Bar Chart)**  
   Shows the number of published papers per year.

2. **Top 10 Journals (Horizontal Bar Chart)**  
   Displays the most frequent journals in the dataset.

3. **Abstract Word Count Distribution (Histogram)**  
   Helps understand how detailed the abstracts are.

4. **Word Cloud of Paper Titles**  
   Visual representation of the most common keywords in titles.

---

## 🧩 **Technologies Used**

- **Python**
- **Streamlit**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **WordCloud**
