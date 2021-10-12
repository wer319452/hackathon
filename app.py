import streamlit as st
from PIL import Image

st.set_option('deprecation.showfileUploaderEncoding', False) #deprecation?
st.title('머신러닝을 이용한 쓰레기 분리수거 방식 분류 서비스')
st.markdown("""
쓰레기 분리수거 방식을 제공합니다 분명하지 않을 수도 있습니다. """)

image2 = Image.open('tresh.jpg')
st.image(image2, caption='쓰레기 분리수거 방식 분류 서비스', use_column_width=True)

st.text("분리수거할 제품 사진을 올려주세요.")

from PIL import Image, ImageOps

from image_classification import tresh_classification

uploaded_file = st.file_uploader("분리수거할 제품 사진을 업로드 해주세요.", type=['jpg', 'png','jpeg','jfif'])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Tresh', use_column_width=True)
    st.write("")
    st.write("처리 중입니다...")
    label = tresh_classification(image, 'keras_model.h5')
    if label == 0:
        st.write("골판지 박스입니다.")
    elif label == 1:
        st.write("형광등")
    elif label == 2:
        st.write("영수증")
    elif label == 3:
        st.write("책")
    elif label == 4:
        st.write("캔")
    elif label == 5:
        st.write("유리병")
    elif label == 6:
        st.write("종이팩")
    elif label == 7:
        st.write("종이컵")
    elif label == 8:
        st.write("컵라면 용기")
    elif label == 9:
        st.write("볼펜")
    elif label == 10:
        st.write("생선 가시")
    elif label == 11:
        st.write("멀티탭")
    elif label == 12:
        st.write("계란 껍데기")
    elif label == 13:
        st.write("닭 뼈")
    elif label == 14:
        st.write("칫솔")
    elif label == 15:
        st.write("폐건전지")
    elif label == 16:
        st.write("과자 봉지")
    elif label == 17:
        st.write("라면 봉지")
    elif label == 18:
        st.write("플라스틱 컵")
    elif label == 19:
        st.write("페트병")

    