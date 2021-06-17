import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)


for i in range(100):
  latest_iteration.text(f'Iteration{i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'Done!!!!!!!'

left_column, rigth_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  rigth_column.write('ここは右カラムです。')

expander1 = st.beta_expander('問い合わせ')
expander1.write('問い合わせ内容を書く')
expander2 = st.beta_expander('問い合わせ')
expander2.write('問い合わせ内容を書く')
expander3 = st.beta_expander('問い合わせ')
expander3.write('問い合わせ内容を書く')

# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('今日の調子は？？', 0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション', condition

# if condition <= 30:
#   '今日はもう、、むり、、定時で帰らせて、、'
# elif condition <= 70:
#   'まあまあっすね。'
# elif condition <= 95:
#   'ノリノリっす。'
# else:
#   '超絶調子いいです。朝までいけます。'

# option = st.selectbox(
#   'あなたの好きな数字を教えてください。',
#   list(range(1,11))
# )

# 'あなたの好きな数字は、', option, 'です。'

# if st.checkbox('Show Image'):
#   img = Image.open('./japan.jpg')
#   st.image(img, caption='日本の富士山です。', use_column_width=True)


# df = pd.DataFrame(
#   np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
#   columns= ['lat','lon'],
# )

# st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)
# st.table(df)

# st.line_chart(df)

# st.area_chart(df)

# st.bar_chart(df)

# st.map(df)
