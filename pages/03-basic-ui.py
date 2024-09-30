import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime
button=st.button('버튼을 눌러보세요')
if button:
  st.write(':blue[지후]에 대해서:sparkles:')
dataframe=pd.DataFrame({
  'first column':['kor','eng','math','science'],
  'second column':[10,20,30,40]
})
st.download_button(
  label='CSV로 성적표 다운로드',
  data=dataframe.to_csv(),
  file_name='sample.csv',
  mime='text/csv'
)
agree=st.checkbox('동의하십니까?')
if agree:
  st.write('동의 해주셔서 감사합니다:100:')
mbti=st.radio('당신의 MBTI는 무엇입니까?',
              ('ISTJ',  'ENFP', '선택지 없음'))
if mbti=='ISTJ':
  st.write('당신은 :blue[현실주의자] 이시네요.')
elif mbti=='ENFP':
  st.write('당신은 :green[활동가] 이시네요.')
else:
  st.write('당신에 대해 :red[알고 싶어요]:grey_exclamation:')

