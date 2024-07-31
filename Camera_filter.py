import streamlit as st
from PIL import Image, ImageFilter, ImageEnhance
import io

st.title("CAMERA FILTER APP")

with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    img = Image.open(camera_image)

    # Add filters
    filter_options = ["Grayscale", "Blur", "Contour", "Edge Enhance", "Sepia", "Emboss", "Rotate"]
    selected_filter = st.selectbox("Select Filter", filter_options)

    if selected_filter == "Grayscale":
        filtered_img = img.convert("L")
    elif selected_filter == "Blur":
        filtered_img = img.filter(ImageFilter.BLUR)
    elif selected_filter == "Contour":
        filtered_img = img.filter(ImageFilter.CONTOUR)
    elif selected_filter == "Edge Enhance":
        filtered_img = img.filter(ImageFilter.EDGE_ENHANCE)
    elif selected_filter == "Sepia":
        filtered_img = img.convert("L").convert("RGB")
        filtered_img = ImageEnhance.Color(filtered_img).enhance(0.5)
    elif selected_filter == "Emboss":
        filtered_img = img.filter(ImageFilter.EMBOSS)
    elif selected_filter == "Rotate":
        angle = st.slider("Rotate Angle", 0, 360, 90)
        filtered_img = img.rotate(angle)

    # Display filtered image
    st.image(filtered_img)

    # Create a download button
    buffer = io.BytesIO()
    filtered_img.save(buffer, format="JPEG")
    buffer.seek(0)

    st.download_button(
        label="Download Image",
        data=buffer,
        file_name="filtered_image.jpg",
        mime="image/jpeg"
    )







