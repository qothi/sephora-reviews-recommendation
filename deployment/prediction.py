"""
Graded Challenge
Nama: Qothrunnadaa Alyaa
Batch: HCK-009

File ini digunakan untuk menjalankan model prediksi rekomendasi user Sephora USA berdasarkan review yang diberikan
"""

import streamlit as st
import pandas as pd
import numpy as np
import json
import nltk
import tensorflow as tf
from tensorflow.keras.models import load_model
from preprocessing import text_preprocessing
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('wordnet')

# Membuat function untuk dipanggil di app.py
def run():
    st.title('Sephora Products Recommendation Predictor')

    # Memasukkan review dari pelanggan/user
    review_text = st.text_input(label='Input your review here')

    # Menampilkan review yang dimasukkan user
    st.write(review_text)

    review_df = pd.DataFrame([review_text], columns=['review_text'])

    with open('stopwords.txt', 'r') as sw:
        stopwords = json.load(sw)
    stopwords = set(stopwords)

    lemmatizer = WordNetLemmatizer()

    review_df['review_text'] = review_df.apply(lambda row: text_preprocessing(row['review_text'], stopwords, lemmatizer), axis=1)


    # Memprediksi apakah user merekomendasikan produk yang dibeli berdasarkan review
    if st.button(label='Predict'):
        
        model = load_model('model_lstm_2')
            
        y_pred_inf = model.predict(review_df)
        
        if y_pred_inf <= 0.5:
            st.write('User did not recommend the product.')
        else:
            st.write('User recommend the product.')