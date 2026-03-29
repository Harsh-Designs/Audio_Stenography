# 🔐 Secure Audio Steganography System

This project is a Python-based web application that hides secret messages inside WAV audio files using LSB (Least Significant Bit) steganography combined with encryption.

The system ensures secure communication by encrypting the message before embedding it into the audio file. A user-friendly interface built with Streamlit allows easy encoding and decoding of messages.

---

## 🚀 Features

* Hide secret messages inside audio files
* AES-based encryption for added security
* Encode and decode functionality
* Simple web interface using Streamlit
* Upload and download audio files

---

## 🛠️ Technologies Used

* Python
* Streamlit
* NumPy
* SciPy
* Cryptography

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Deployment

The project is deployed using Streamlit Cloud for easy online access.

---

## ⚠️ Important Notes

* Only WAV files are supported
* Keep the secret.key file unchanged
* Do not convert stego audio to MP3

---

## 📌 Concept Used

* Steganography (LSB technique)
* Cryptography (Fernet / AES encryption)

---

Secure communication using a combination of steganography and encryption.
 
