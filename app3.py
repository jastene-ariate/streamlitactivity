import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="🦠 COVID-19 Stats Viewer", page_icon="🧬", layout="wide")

st.title("🦠 COVID-19 Global Statistics")
st.markdown("### 🎯 Data from [disease.sh](https://disease.sh/docs) | Visualized with 5+ chart types")

# Select country
country = st.selectbox("🌍 Select a country", ["USA", "India", "Brazil", "Germany", "France", "Japan"])

# Fetch API data
url = f"https://disease.sh/v3/covid-19/historical/{country}?lastdays=30"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    cases = data["timeline"]["cases"]
    deaths = data["timeline"]["deaths"]
    recovered = data["timeline"]["recovered"]

    # Create DataFrame
    df = pd.DataFrame({
        "Date": list(cases.keys()),
        "Cases": list(cases.values()),
        "Deaths": list(deaths.values()),
        "Recovered": list(recovered.values())
    })
    df["Date"] = pd.to_datetime(df["Date"])

    # 1. Line chart
    st.subheader("📈 Line Chart: Cases over Time")
    st.line_chart(df.set_index("Date")[["Cases", "Deaths", "Recovered"]])

    # 2. Bar chart
    st.subheader("📊 Bar Chart: Daily Deaths")
    df["Daily Deaths"] = df["Deaths"].diff()
    st.bar_chart(df.set_index("Date")["Daily Deaths"])

    # 3. Area chart
    st.subheader("📉 Area Chart: Recovered")
    st.area_chart(df.set_index("Date")["Recovered"])

    # 4. Pie chart
    st.subheader("🥧 Pie Chart: Latest Values")
    latest = df.iloc[-1]
    pie_df = pd.DataFrame({
        "Category": ["Cases", "Deaths", "Recovered"],
        "Value": [latest["Cases"], latest["Deaths"], latest["Recovered"]]
    })
    fig = px.pie(pie_df, values='Value', names='Category', title="Proportion of Cases")
    st.plotly_chart(fig)

    # 5. Heatmap (with Seaborn)
    st.subheader("🌡️ Heatmap: Correlation Matrix")
    corr = df[["Cases", "Deaths", "Recovered"]].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

else:
    st.error("Failed to fetch data from the API.")
