import streamlit as st
import pickle
import pandas as pd

def display(name):
    counts = new.get_group(name)['sentiment_2'].value_counts()
    st.write("Sentiment Counts:")
    st.markdown("Positive reviews :", counts.get('positive', 0))
    st.write("Negative reviews:", counts.get('negative', 0))
    st.write("Neutral reviews:", counts.get('neutral', 0))

df = pickle.load(open('product.pkl','rb'))
df = pd.DataFrame(df)
new = df.groupby('product_name')

st.title("Flipkart Product Reviews")
name = st.selectbox(
    'select a product',
    [None]+list(df['product_name'].unique())
)

if st.button('Display'):
    if name:
        display(name)
