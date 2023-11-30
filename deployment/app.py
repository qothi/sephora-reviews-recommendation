"""
Graded Challenge 7
Nama: Qothrunnadaa Alyaa
Batch: HCK-009

File ini digunakan untuk menjalankan home page model prediksi rekomendasi user Sephora USA berdasarkan review yang diberikan
"""

import streamlit as st
import eda
import prediction


page = st.sidebar.selectbox(label='Pilih menu untuk memulai:', options=['Home Page', 'Exploratory Data Analysis', 'Prediction Model'])

if page == 'Home Page':
    st.header('Welcome to Sephora Products Recommendation Predictor!') 
    st.write('')
    st.subheader('Graded Challenge 7')
    st.write('Nama      : Qothrunnadaa Alyaa')
    st.write('Batch     : HCK-009')
    st.write('Dataset   : Sephora Products and Skincare Reviews')
    st.write('')
    st.write('')
    st.write('')
    with st.expander('Objektif'):
        st.caption('Memprediksi apakah seorang pelanggan merekomendasikan produk yang ia beli dari review yang ia tinggalkan di website Sephora')

    with st.expander('Problem Statement'):
        st.caption('Bagaimana cara memprediksi apakah user merekomendasikan suatu produk yang mereka review dari isi review pada website Sephora?')

    with st.expander('Kesimpulan'):
        st.caption('Review yang diberikan oleh user Sephora USA dapat memprediksi apakah user tersebut merekomendasikan produk yang di-review atau tidak menggunakan model Long Short-Term Memory (LSTM) dengan akurasi sebesar 84%.')

elif page == 'Exploratory Data Analysis':
    eda.run()

else:
     prediction.run()