import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

# st.header('st.button')

# if st.button('버튼 누르기'):
#     st.write('누름')
# else:
#     st.write('안누름')



st.header('st.write')

st.write('Hello, *World!* :sunglasses:')

st.write(1234)

df = pd.DataFrame({
                  'first column': [1, 2, 3, 4],
                  'second column': [10, 20, 30, 40]
                  })

st.write(df)

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')


df2 = pd.DataFrame(
     np.random.randn(100, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
     
st.write(c)

