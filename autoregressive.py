import numpy as np
import pandas as pd
import streamlit as st

with st.sidebar:
    st.header("Modellkonfiguration")
    drift = st.number_input("Drift", min_value=-5.0, max_value=5.0, value=0.0)
    weight = st.number_input("Gewicht", min_value=-5.0, max_value=5.0, value=0.9)
    length = st.slider("Länge", min_value=0, max_value=10 * 365, value=365)
    st.button("Generieren")

rng = np.random.default_rng()
eps = rng.standard_normal(length - 1)
y = np.zeros((length,))

for i in range(length - 1):
    y[i + 1] = drift + weight * y[i] + eps[i]

df = pd.DataFrame({"y": y})
st.header("Simulierte Zeitreihe")
st.line_chart(df)
