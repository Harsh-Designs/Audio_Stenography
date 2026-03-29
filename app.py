import streamlit as st
from encode import encode_audio
from decode import decode_audio
import os

st.set_page_config(page_title="Audio Steganography 🔐", layout="centered")

st.title("🔐 Secure Audio Steganography System")

menu = st.sidebar.selectbox("Choose Option", ["Encode", "Decode"])

uploaded_file = st.file_uploader("Upload WAV file", type=["wav"])

# ----------- ENCODE -----------
if menu == "Encode":
    msg = st.text_area("Enter Secret Message")

    if st.button("Encrypt & Hide"):
        if uploaded_file is not None and msg != "":
            with open("temp.wav", "wb") as f:
                f.write(uploaded_file.read())

            try:
                encode_audio("temp.wav", "stego.wav", msg)

                st.success("Message Hidden Successfully ✅")
                st.audio("stego.wav")

                with open("stego.wav", "rb") as f:
                    st.download_button(
                        "Download Stego Audio",
                        f,
                        "stego.wav"
                    )

            except Exception as e:
                st.error(str(e))
        else:
            st.warning("Upload WAV file and enter message")

# ----------- DECODE -----------
elif menu == "Decode":
    if st.button("Extract Message"):
        if uploaded_file is not None:
            with open("temp.wav", "wb") as f:
                f.write(uploaded_file.read())

            try:
                message = decode_audio("temp.wav")
                st.success("Hidden Message: " + message)

            except Exception as e:
                st.error(str(e))
        else:
            st.warning("Upload WAV file")