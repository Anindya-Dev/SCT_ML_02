# SCT_ML_02
# 🧠 Customer Segmentation using K-Means (Streamlit App)

This Streamlit application allows you to perform **K-Means clustering** on retail customer data. It uses features like **Annual Income** and **Spending Score** to group customers into clusters and visualize them interactively.

---

## 🚀 Features

- Upload your own `Mall_Customers.csv` file.
- Automatically applies K-Means clustering (k=5).
- Visualizes customer segments using a scatter plot.
- Displays clustered data with assigned labels.

---

## 📁 Files Included

- `app.py` – Main Streamlit application script.
- `Mall_Customers` -Dataset
- `requirements.txt` – Python dependencies for running the app.
- `README.md` – This file.

---

## 📊 Input CSV Format

Your CSV should contain at least the following columns:

- `CustomerID`
- `Annual Income (k$)`
- `Spending Score (1-100)`

You can use the public **Mall_Customers.csv** dataset as an example.

---
## Clone the repository:

git clone https://github.com/Anindya-Dev/SCT_ML_02.git
cd SCT_ML_02


## ▶️ How to Run

### 1. Install dependencies:

```bash
pip install -r requirements.txt
#Use this command to run the app on a localhost server
streamlit run app.py

