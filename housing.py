import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load the data
housing = pd.read_csv("housing.csv")

# Custom CSS for styling
st.markdown("""
    <style>
        .title {
            font-size: 35px;
            font-weight: bold;
            color: #2E86C1;
        }
        .section {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title with an icon
st.markdown('<p class="title">🏠 Housing Data Analysis Dashboard</p>', unsafe_allow_html=True)

# First and last few rows of the dataset
st.markdown('<div class="section">', unsafe_allow_html=True)
st.write("### 📈 First 5 rows of the dataset")
st.write(housing.head())
st.write("### 📉 Last 5 rows of the dataset")
st.write(housing.tail())
st.markdown('</div>', unsafe_allow_html=True)

# Scatter Plot 1
st.markdown('<div class="section">', unsafe_allow_html=True)
st.write("### Scatter plot of 'Gr Liv Area' vs 'SalePrice'")
fig1 = sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice')
st.pyplot(fig1)
st.markdown('</div>', unsafe_allow_html=True)

# Scatter Plot 2 with customized style
st.markdown('<div class="section">', unsafe_allow_html=True)
st.write("### Scatter plot with 'Overall Qual' as hue and 'Garage Area' as size")
fig2 = sns.relplot(
    data=housing, 
    x='Gr Liv Area', 
    y='SalePrice', 
    hue='Overall Qual', 
    palette='RdYlGn', 
    size='Garage Area', 
    sizes=(1, 300)
)
st.pyplot(fig2)
st.markdown('</div>', unsafe_allow_html=True)

# Advanced Scatter Plot
st.markdown('<div class="section">', unsafe_allow_html=True)
st.write("### Advanced scatter plot with 'Rooms' as style and 'Year' as columns")
fig3 = sns.relplot(
    data=housing, 
    x='Gr Liv Area', 
    y='SalePrice', 
    hue='Overall Qual', 
    palette='RdYlGn', 
    size='Garage Area', 
    sizes=(1, 500), 
    style='Rooms', 
    col='Year'
)
st.pyplot(fig3)
st.markdown('</div>', unsafe_allow_html=True)
