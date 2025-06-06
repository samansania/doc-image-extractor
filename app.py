import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

st.title("Document Extractor App")

uploaded_file = st.file_uploader("Upload your scanned document", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Read image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    st.image(img, caption="Uploaded Document", use_column_width=True)

    # Define fixed coordinates for photo, signature, thumb impression (example)
    # You will adjust these later for your document format

    # Example boxes (x, y, w, h) - change these as per your doc layout
    photo_box = img[50:200, 50:200]
    signature_box = img[600:700, 50:250]
    thumb_box = img[600:700, 300:450]

    st.subheader("Extracted Photo")
    st.image(photo_box, use_column_width=False)

    st.subheader("Extracted Signature")
    st.image(signature_box, use_column_width=False)

    st.subheader("Extracted Thumb Impression")
    st.image(thumb_box, use_column_width=False)
