from numpy.lib.function_base import place
import streamlit as st
from PIL import Image

st.set_option('deprecation.showfileUploaderEncoding', False) #deprecation?
st.title('머신러닝을 이용한 쓰레기 분리수거 방식 분류 서비스')
st.markdown("""
쓰레기 분리수거 방식을 제공합니다 분명하지 않을 수도 있습니다. """)

image2 = Image.open('trash.jpg')
st.image(image2, caption='쓰레기 분리수거 방식 분류 서비스', use_column_width=True)

# st.text("분리수거할 제품 사진을 올려주세요.")

from PIL import Image, ImageOps

from big_5_classification import big_5_classification
from paper_classification import paper_classification
from metal_classification import metal_classification
from glass_classification import glass_classification

uploaded_file = st.file_uploader("분리수거할 제품 사진을 업로드 해주세요.", type=['jpg', 'png','jpeg','jfif'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded garbage', use_column_width=True)
    st.write("")
    st.write("처리 중입니다...")
    label = big_5_classification(image, 'big_5_clf.h5')
    if label == 0: #cardboard
        st.write("cardboard")
    elif label == 1: #glass
        label = glass_classification(image, 'glass_clf.h5')
        # 0 glass
        # 1 plastic cup
        # 2 juice
        if label == 0:
            st.write("glass")
        elif label == 1:
            st.write('plastic cup')
        elif label == 2:
            st.write('plastic bottle')
    elif label == 2: #metal
        label = metal_classification(image, 'metal_clf.h5')
        # 0 plastic bag
        # 1 can
        if label == 0:
            st.write("plastic bag")
        elif label == 1:
            st.write("can")
    elif label == 3: #paper
        label = paper_classification(image, 'paper_clf.h5')
        # 0 receipt
        # 1 book
        # 2 carton pack
        # 3 paper cup
        # 4 newspaper
        if label == 0:
            st.write("receipt")
        elif label == 1:
            st.write("book")
        elif label == 2:
            st.write("carton pack")
        elif label == 3:
            st.write("paper cup")
        elif label == 4:
            st.write("newspaper")
    elif label == 4: #plastic
        st.write("plastic")



    