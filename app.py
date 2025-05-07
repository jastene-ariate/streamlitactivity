import streamlit as st

# Set page config
st.set_page_config(page_title="Hello, Streamlit!", page_icon="👋", layout="centered")

# Title and header
st.title("👋 Hello, Streamlit!")
st.markdown("### 🎯 *Objective: Understand basic components of a Streamlit app*")

# Section: Introduction box
with st.container():
    st.markdown("---")
    st.markdown("This app takes your **name** and **age**, then responds with a personalized greeting. 😊")
    st.markdown("---")

# Input section in columns
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("👤 Enter your name")

with col2:
    age = st.number_input("🎂 Enter your age", min_value=0, max_value=120, step=1)

# Display output if name is entered
if name:
    st.success(f"✅ Hello, **{name}**! 🎉")
    st.info(f"📌 You are **{int(age)}** years old.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
