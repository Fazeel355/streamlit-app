import streamlit as st
import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'Numbers': [1, 2, 3, 4, 5],
    'Letters': ['A', 'B', 'C', 'D', 'E']
}
df = pd.DataFrame(data)

# Display the DataFrame
st.write('Original DataFrame:')
st.dataframe(df)

# Perform a mathematical operation on the DataFrame
multiplier = st.slider('Select a multiplier', 1, 10, 2)
df['Multiplied'] = df['Numbers'] * multiplier

# Display the modified DataFrame
st.write('Modified DataFrame:')
st.dataframe(df)
