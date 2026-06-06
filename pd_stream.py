import streamlit as st
import pandas as pd

st.title("Meu Primeiro App com Streamlit")
st.write("Sistema com Pandas")

df = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carla', 'Daniel'],
    'Idade': [23, 35, 29, 42],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
})

st.write(df)
st.bar_chart(df.set_index('Nome')['Idade'])
