"""
Milestone 2
Nama: Qothrunnadaa Alyaa
Batch: HCK-009

File digunakan untuk menjalankan page EDA dari model prediksi rekomendasi user Sephora USA berdasarkan review yang diberikan
"""

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Membuat function untuk dipanggil pada app.py
def run():
    st.title('Exploratory Data Analysis')
    st.write('Laman ini berisi eksplorasi data dari dataset Sephora Products and Skincare Reviews. Dataset ini akan digunakan untuk memprediksi apakah user/pelanggan merekomendasikan produk yang dibeli di Sephora berdasarkan review yang diberikan.')

# Load csv dataset
    df = pd.read_csv('reviews_0-250.csv')

# Dataset yang digunakan
    st.header('Sephora Products and Skincare Reviews')
    st.table(df.head(10))

# Menampilkan rating produk berdasarkan apakah produk tersebut direkomendasikan oleh user
    st.header('Product Ratings by Users Recommendation')
    rate_recommend = Image.open('rating_recommend.png')
    st.image(rate_recommend, caption='Product Ratings by Users Recommendation')

# Penjelasan dari rating produk berdasarkan apakah produk tersebut direkomendasikan oleh user
    with st.expander('Explanation'):
        st.caption('Semakin tinggi rating yang diberikan oleh user, maka user tersebut semakin cenderung untuk merekomendasikan produk tersebut.')

# Menampilkan distribusi dari panjang review
    st.header("Review Length")
    review_len = Image.open('review_len.png')
    st.image(review_len, caption="Review Length")

# Penjelasan dari distribusi panjang review 
    with st.expander('Explanation'):
        st.caption('Tidak ada perbedaan yang terlalu jauh antara panjang review produk yang direkomenadasikan oleh user dengan produk yang tidak direkomendasikan oleh user. Panjang review dari produk yang direkomendasikan oleh user sedikit lebih panjang dibandingkan review produk yang tidak direkomendasikan oleh user.')

# Menampilkan word cloud dari produk yang direkomendasikan oleh user
    st.header("Recommended Products' Reviews Word Cloud")
    wordcloud_1 = Image.open('wordcloud_1.png')
    st.image(wordcloud_1, caption="Recommended Products' Reviews Word Cloud")

# Penjelasan dari word cloud produk yang direkomendasikan oleh user
    with st.expander('Explanation'):
        st.caption('Kata yang sering muncul merupakan kata-kata yang bersifat positif seperti love (the) product, great product, highly recommend, dan definitely recommend.')

# Menampilkan word cloud dari produk yang tidak direkomendasikan oleh user
    st.header("Not Recommended Products' Reviews Word Cloud")
    wordcloud_0 = Image.open('wordcloud_0.png')
    st.image(wordcloud_0, caption="Not Recommended Products' Reviews Word Cloud")

# Penjelasan dari word cloud produk yang tidak direkomendasikan oleh user
    with st.expander('Explanation'):
        st.caption('Sebagian besar kata yang muncul adalah jenis produknya seperti moisturizer dan cleanser, kata think, really, even, dan one. Kata wanted (to) love juga menjadi kata yang sering muncul, menandakan bahwa user sebenarnya ingin menyukai produk yang tidak mereka rekomendasikan.')        