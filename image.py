from PIL import Image,ImageFilter
import streamlit as st
st.title("Image Filter")
img = st.file_uploader("select Image",type=["jpg","jpeg","png"])
if img:
    option=st.selectbox("Select Filter",["0riginal","Grayscale","Contour","Blur"])
    img=Image.open(img)
    if option == "Grayscale":
        img = img.convert("L")
    elif option == "Contour":
        img = img.filter(ImageFilter.CONTOUR)
    elif option == "Blur":
        img = img.filter(ImageFilter.BLUR)
    st.image(img)


