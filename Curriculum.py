import streamlit as st

# Lee el contenido del archivo Markdown
with open("CurriculumDaniel.md", "r", encoding="utf-8") as file:
    markdown_content = file.read()

# Muestra el contenido en Streamlit
st.markdown(markdown_content, unsafe_allow_html=True)

# Puedes agregar otros elementos de Streamlit si deseas
