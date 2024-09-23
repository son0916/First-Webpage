import streamlit as st
st.title(" NICE TO MEET YOU")
st.title("스마일 :sunglasses:")
st.header("저는 원의 방정식에 대해 설명해 보려고 합니다:sparkles:")
st.subheader("먼저 원의 정의는 평면 상에서 중심으로부터 거리가 같은 점들의 집합입니다.")
st.caption("이해했나요?")
sample_code='''
def function():
    print("No")
'''
st.code(sample_code, language="python")
st.text("No 말고 Yes라고 대답해주세요.")
st.markdown("그 다음으로 **원의 방정식의 식**에 대해 설명하자면.")
st.markdown("원의 방정식의 식은 **:blue[피타고라스 정리]**로부터 유도하는데요.")
st.latex(":red[$x^2+y^2=1$]")
st.text("입니다.")
