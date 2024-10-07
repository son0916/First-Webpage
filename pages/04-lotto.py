import streamlit as st
import random
import datetime

candidates = ["흑수저 셰프 A", "흑수저 셰프 B", "백수저 셰프 C", "백수저 셰프 D", "백수저 셰프 E"]

st.title("흑백요리사 우승자 예측 프로그램")

def predict_winner():
    return random.choice(candidates)

button = st.button('우승자 예측하기')

if button:
    winner = predict_winner()
    st.subheader(f"예측된 우승자는: :trophy: {winner} 입니다!")
