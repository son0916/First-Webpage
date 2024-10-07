import streamlit as st
import random
import datetime

st.title(':sparkles:지후의 성적표:sparkles:')

def generate_lotto():
    lotto=set()

    while len(lotto)<6:
        number=random.randint(1,46)
        lotto.add(number)

    lotto=list(lotto)
    lotto.sort()
    return lotto

button=st.button('지후의 성적표를 생성해 주세요!')

if button:
    for i in range(1,6):
        st.subheader(f'{i}. 지후의 국어,영어,수학,사회,과학,역사: :green[{generate_lotto()}]')
    st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
