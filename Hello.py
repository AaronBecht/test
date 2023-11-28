import streamlit as st

st.write('Hello World')

import streamlit as st

option = st.selectbox(
    'Welche Uni ist die mit den allerbesten Studenten?',
    ('Goethe Uni', 'Goethe Uni', 'Goethe Uni'))

st.write('You selected:', option)

import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.scatter_chart(chart_data)