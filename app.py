import streamlit as st
import os
import cv2
import tempfile

st.set_page_config(page_title="Pembaca Bahasa Isyarat", layout="centered")

st.title("📹 Pembaca Video Bahasa Isyarat")
st.write("Unggah video berisi bahasa isyarat, nanti akan ditampilkan.")

uploaded_file = st.file_uploader("Upload Video", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    st.video(tfile.name)

    cap = cv2.VideoCapture(tfile.name)
    ret, frame = cap.read()
    cap.release()

    if ret:
        st.image(frame, caption="Frame Pertama")

    st.success("Video berhasil diunggah dan ditampilkan!")

st.markdown("---")
st.info("Fitur deteksi gesture menyusul 👋")
