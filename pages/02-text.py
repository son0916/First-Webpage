import streamlit as st
st.title(" NICE TO MEET YOU")
st.title("스마일 :sunglasses:")
st.header("I'm happy to see you :sparkles:")
st.subheader("I hope you are happy")
st.caption("안녕하세요!")
sample_code='''
def function():
    print("hello")
'''
st.code(sample_code, language="python")
st.text("만나서 반갑습니다.")
st.markdown("**당신**의 **행복**을 지지합니다.")
st.markdown("당신의 :red[행복]은 **:blue[정해 지지]** 않았습니다.")
st.markdown(":ornage[$ax=b$]")
st.latex(r"ax=b")
