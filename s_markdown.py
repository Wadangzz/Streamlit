import streamlit as st

st.title("마크다운 뷰어")

with open("markdown_practice.md", "r", encoding='utf-8') as f: # 파일 인코딩 명시 (UTF-8)
    markdown_text = f.read()

st.markdown(markdown_text)