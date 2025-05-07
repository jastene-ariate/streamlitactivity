import streamlit as st

# Page config
st.set_page_config(page_title="📐 Layout Demo", page_icon="🧩", layout="wide")

# Sidebar content
st.sidebar.title("🛠️ Controls")
user_name = st.sidebar.text_input("Enter your name")
theme = st.sidebar.selectbox("Choose a theme", ["Light", "Dark", "Colorful"])

st.sidebar.markdown("---")
show_details = st.sidebar.checkbox("Show extra details")

# Main area layout
st.title("📐 Streamlit Layout Demo")
st.write(f"Welcome, **{user_name or 'Guest'}**! You selected the **{theme}** theme.")

# Columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Column 1")
    st.write("This column can show a chart, stats, or info.")

with col2:
    st.subheader("📝 Column 2")
    st.write("Use it to compare data or show different content.")

# Expandable section
with st.expander("🔍 See more details"):
    st.write("""
        You can hide content in expandable boxes to keep the layout clean.
        This is useful for FAQs, technical descriptions, or hidden filters.
    """)

# Conditional container
if show_details:
    with st.container():
        st.markdown("### 📦 Extra Details")
        st.info("This content is shown because you checked the 'Show extra details' option in the sidebar.")
