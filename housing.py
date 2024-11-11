import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load the data
housing = pd.read_csv("housing.csv")

# Custom CSS for styling the dashboard
st.markdown("""
    <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #2E86C1;
            text-align: center;
        }
        .section {
            background-color: #f4f4f4;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
            margin-bottom: 30px;
            margin-top: 20px;
        }
        .dropdown-container {
            margin-bottom: 20px;
        }
        .sidebar .sidebar-content {
            background-color: #2E86C1;
        }
        .sidebar .sidebar-header {
            font-size: 20px;
            color: white;
        }
        .footer {
            font-size: 12px;
            text-align: center;
            color: #808080;
            margin-top: 40px;
        }
        .button-container {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Title with an icon
st.markdown('<p class="title">🏠 Housing Data Analysis Dashboard</p>', unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.header("Navigation Panel")
chart_selection = st.sidebar.selectbox(
    "Select a chart to view:",
    options=[
        "Overview of Dataset",
        "Scatter plot of 'Gr Liv Area' vs 'SalePrice'",
        "Scatter plot with 'Overall Qual' as hue and 'Garage Area' as size",
        "Advanced Scatter Plot"
    ]
)

# First and last few rows of the dataset
if chart_selection == "Overview of Dataset":
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.write("### 📈 First 5 rows of the dataset")
    st.write(housing.head())
    st.write("### 📉 Last 5 rows of the dataset")
    st.write(housing.tail())
    st.markdown('</div>', unsafe_allow_html=True)

# Scatter Plot 1
elif chart_selection == "Scatter plot of 'Gr Liv Area' vs 'SalePrice'":
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.write("### Scatter plot of 'Gr Liv Area' vs 'SalePrice'")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=housing, x='Gr Liv Area', y='SalePrice', ax=ax1)
    ax1.set_title("Living Area vs Sale Price", fontsize=16, weight='bold')
    st.pyplot(fig1)
    st.markdown('</div>', unsafe_allow_html=True)

# Scatter Plot 2 with customized style
elif chart_selection == "Scatter plot with 'Overall Qual' as hue and 'Garage Area' as size":
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.write("### Scatter plot with 'Overall Qual' as hue and 'Garage Area' as size")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.scatterplot(
        data=housing, 
        x='Gr Liv Area', 
        y='SalePrice', 
        hue='Overall Qual', 
        palette='RdYlGn', 
        size='Garage Area', 
        sizes=(20, 200),
        ax=ax2
    )
    ax2.set_title("Living Area vs Sale Price (with Quality & Garage Size)", fontsize=16, weight='bold')
    st.pyplot(fig2)
    st.markdown('</div>', unsafe_allow_html=True)

# Advanced Scatter Plot with multiple columns (for each year)
elif chart_selection == "Advanced Scatter Plot":
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.write("### Advanced scatter plot with 'Rooms' as style and 'Year' as columns")
    fig3 = sns.relplot(
        data=housing, 
        x='Gr Liv Area', 
        y='SalePrice', 
        hue='Overall Qual', 
        palette='RdYlGn', 
        size='Garage Area', 
        sizes=(20, 300), 
        style='Rooms', 
        col='Year',
        height=6, aspect=1.5
    )
    st.pyplot(fig3)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer to add more information
st.markdown('<div class="footer">', unsafe_allow_html=True)
st.write("Created with ❤️ by your data science team. Reach out for more insights!")
st.markdown('</div>', unsafe_allow_html=True)
