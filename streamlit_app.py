import streamlit as st

st.set_page_config(page_title="My App", layout="wide")

page = st.navigation([
    # st.Page("pages/home.py", title="홈", icon="🏠"),
    st.Page("pages/chart.py", title="차트", icon="📈"),
    # st.Page("pages/data.py", title="데이터", icon="🧾"),
])

page.run()
