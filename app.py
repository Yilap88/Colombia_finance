import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="My app",
    layout="wide"
)

st.write("""
# My first app
Hello *world!*
""")

html = Path("grafico.html").read_text(encoding="utf-8")

st.components.v1.html(
    html,
    height=600,
    scrolling=True


)
