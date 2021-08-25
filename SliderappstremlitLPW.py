import streamlit as st

st.subheader("Streamlit Sliders")

st.subheader("Slider 1:")

x = st.slider('A number between 0-100', value = 50)

st.write("Slider number:", x)

st.subheader("Slider 2:")

y = st.slider('Choose between 0-1 by 0.1',
              min_value = 0.0, max_value=1.0, step=0.1)

st.write("Slider number:", y)
