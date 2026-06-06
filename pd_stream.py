import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carla', 'Daniel'],
    'Idade': [23, 35, 29, 42],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
})

st.write(df)