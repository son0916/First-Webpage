import streamlit as st
st.title("My first web sevice!")
name=st.text_input("이름을 입력해주세요!")
menu=st.selectbox("좋아하는 음식을 선택해주세요!",['칼국수','라면','냉면','우동'])
if st.button("인사말 생성하기"):
  st.write(name+"님! 당신이 좋아하는 음식은 "+menu+"이군요! 저도 좋아요!")
