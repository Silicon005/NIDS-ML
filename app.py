import streamlit as st
from PIL import Image

st.set_page_config(page_title="File Uploader", page_icon="📁", layout="centered")

st.markdown("""
    <style>
        .main { background-color: #f9f7f7; color: #112D4E; }
        .stButton>button { background-color: #3F72AF; color: white; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

st.title("📁 Upload Your File")

uploaded_file = st.file_uploader("Choose a file", type=["txt", "csv", "png", "jpg", "pdf"])

if uploaded_file:
    st.success("✅ File uploaded successfully!")

    st.write({
        "Filename": uploaded_file.name,
        "Type": uploaded_file.type,
        "Size (KB)": round(uploaded_file.size / 1024, 2)
    })

    if uploaded_file.type.startswith("image"):
        image = Image.open(uploaded_file)
        st.image(image, caption="Preview", use_column_width=True)
    elif uploaded_file.type == "text/plain":
        content = uploaded_file.read().decode("utf-8")
        st.text_area("Content", content, height=200)
