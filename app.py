import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

st.title("🛍️ Customer Segmentation using K-Means")
st.markdown("Upload your retail customer dataset and visualize clusters based on purchase behavior.")
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of Uploaded Data", df.head())
    required_columns = ['Annual Income (k$)', 'Spending Score (1-100)']
    if all(col in df.columns for col in required_columns):

        X = df[required_columns]
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        k = 5
        kmeans = KMeans(n_clusters=k, random_state=42)
        df['Cluster'] = kmeans.fit_predict(X_scaled)
        st.write("### Data with Cluster Labels", df.head())
        st.write("### Cluster Visualization")
        fig, ax = plt.subplots()
        scatter = ax.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'],
                             c=df['Cluster'], cmap='viridis')
        ax.set_xlabel("Annual Income (k$)")
        ax.set_ylabel("Spending Score (1-100)")
        ax.set_title("Customer Segments (K-Means)")
        st.pyplot(fig)

    else:
        st.error(f"CSV must contain columns: {required_columns}")
