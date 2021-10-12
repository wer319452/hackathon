from numpy.lib.function_base import place
import streamlit as st
from PIL import Image

st.set_option('deprecation.showfileUploaderEncoding', False) #deprecation?
st.title('머신러닝을 이용한 쓰레기 분리수거 방식 분류 서비스')
st.markdown("""
쓰레기 분리수거 방식을 제공합니다 분명하지 않을 수도 있습니다. """)

image2 = Image.open('trash.jpg')
st.image(image2, caption='쓰레기 분리수거 방식 분류 서비스', use_column_width=True)

st.text("")

from PIL import Image, ImageOps

from first_classification import first_classification
from paper_classification import paper_classification
from metal_classification import metal_classification
from glass_classification import glass_classification

uploaded_file = st.file_uploader("분리수거할 제품 사진을 업로드 해주세요.", type=['jpg', 'png','jpeg','jfif'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded garbage', use_column_width=True)
    st.write("")
    st.write("처리 중입니다...")
    label = first_classification(image, 'first_clf.h5')
    # 0 종이류
    # 1 유리
    # 2 캔
    # 3 플라스틱
    # 4 종이팩
    # 5 라면 용기
    # 6 건전지
    # 7 계란껍질
    # 8 과일 포장재
    # 9 땅콩호두껍질
    # 10 밤
    # 11 빨대
    # 12 스티로폼
    # 13 아이스팩
    # 14 양파마늘껍질
    # 15 조개껍질
    # 16 치킨뼈
    # 17 플라스틱 숟가락
    # 18 형광등

    if label == 0: #종이류
        st.write("종이류")
        label = paper_classification(image, 'paper_clf.h5')
        # 0 영수증
        # 1 책
        # 2 종이컵
        # 3 신문지
        # 4 종이상자
        # 5 햇반
        if label == 0:
            st.write("영수증")
        elif label == 1:
            st.write('책')
        elif label == 2:
            st.write('종이컵')
        elif label == 3:
            st.write('신문지')
        elif label == 4:
            st.write('종이상자')
        elif label == 5:
            st.write('햇반')

    elif label == 1: #유리
        label = glass_classification(image, 'glass_clf.h5')
        # 0 glass
        # 1 plastic
        # 2 pet
        # 3 식용유

        if label == 0:
            st.write("유리")
        elif label == 1:
            st.write('plastic')
        elif label == 2:
            st.write('pet')
        elif label == 3:
            st.write('식용유')

    elif label == 2: #캔
        label = metal_classification(image, 'metal_clf.h5')
        # 0 metal
        # 1 glass
        # 2 plastic cup
        # 3 부탄가스-살충제
        # 4 에프킬라


        if label == 0:
            st.write("metal")
        elif label == 1:
            st.write("glass")
        elif label == 2:
            st.write("plastic cup")
        elif label == 3:
            st.write("부탄가스-살충제")
        elif label == 4:
            st.write("에프킬라")

    elif label == 3: #플라스틱
        st.write("plastic")

    elif label == 4: #종이팩
        st.write("종이팩")

    elif label == 5: #라면 용기
        st.write("라면 용기")
    elif label == 6: #건전지
        st.write("건전지")
    elif label == 7: #계란껍질
        st.write("계란껍질")
    elif label == 8: #과일 포장재
        st.write("과일 포장재")
    elif label == 9: #땅콩호두껍질
        st.write("땅콩호두껍질")
    elif label == 10: #밤
        st.write("밤")
    elif label == 11: #빨대
        st.write("빨대")
    elif label == 12: #스티로폼
        st.write("스티로폼")
    elif label == 13: #아이스팩
        st.write("아이스팩")
    elif label == 14: #양파마늘껍질
        st.write("양파마늘껍질")
    elif label == 15: #조개껍질
        st.write("조개껍질")
    elif label == 16: #치킨뼈
        st.write("치킨뼈")
    elif label == 17: #플라스틱 숟가락
        st.write("플라스틱 숟가락")
    elif label == 18: #형광등
        st.write("형광등")
