import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime
button=st.button('버튼을 눌러보세요')
if button:
  st.write(':blue[지후]에 대해서:sparkles:')
dataframe=pd.DataFrame({
  'first column':['kor','eng','math','science'],
  'second column':['F','F','F','F']
})
st.download_button(
  label='지후의 성적표',
  data=dataframe.to_csv(),
  file_name='sample.csv',
  mime='text/csv'
)
agree=st.checkbox('지후의 성적표 서명해주세요.')
if agree:
  st.write('서명해주셔서 감사합니다.')
mbti=st.radio('당신의 MBTI는 무엇입니까?',
              ('ISTJ',  'ENFP', '선택지 없음'))
if mbti=='ISTJ':
  st.write('당신은 :blue[지후]가 아니네요.')
elif mbti=='ENFP':
  st.write('당신은 :green[지후]네요.')
else:
  st.write('당신에 대해 :red[알고 싶어요]:grey_exclamation:')
title=st.text_input(
  label='지후가 가고 싶은 여행지가 있나요?',
  placeholder='여행지를 입력해 주세요'
)
st.write(f'지후가 선택한 여행지: :violet[{title}]')
values=st.slider(
  '범위의 값을 다음과 같이 지정할 수 있어요:sparkels:',
  0.0, 100.0, (25.0, 75.0))
st.write('선택 범위:', values)

