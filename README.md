# Sephora Users Recommendation Based on Reviews

## Summary

This project aims to predict whether a Sephora user recommend the product sold on Sephora website based on the review left by that customer using Natural Languange Processing (NLP) model(s). This project use Sephora Products and Skincare Reviews dataset which contains information about reviews left on Sephora (USA) website, such as customers profile, product details, rating for that product, whether the customer recommends the product, and information about the review itself. This project also explores a little bit about the characteristics of recommended product by the product's rating, price, review length, and words most used in the review.

The result of this project is Long Short-Term Memory (LSTM) model that could predict whether a Sephora user recommend the product based on their review with accuracy around 84%. To enhance the model we could explore more about reviews sponsored by beauty brands and the impact to model's accuracy.

---

Project ini bertujuan untuk memprediksi apakah seorang pelanggan merekomendasikan produk yang ia beli berdasarkan review yang ia tinggalkan di website Sephora (USA) menggunakan metode Natural Language Processing (NLP). Dataset yang digunakan adalah Sephora Products and Skincare Reviews yang berisi informasi mengenai review atau ulasan yang ditinggalkan oleh pengguna Sephora USA pada produk make-up atau skin care yang dijual di website Sephora, seperti profil pengguna yang memberikan ulasan, detail produknya, rating dari produk, apakah pengguna merekomendasikan produk tersebut, serta isi dari ulasan dan informasi lain mengenai ulasan tersebut. Project ini juga mengeksplor mengenai karakteristik dari produk yang direkomendasikan oleh pengguna berdasarkan rating produk, harga produk, panjang ulasan, dan kata-kata yang sering digunakan dalam ulasan.

Dengan menggunakan model Long Short-Term Memory (LSTM), model dapat memprediksi apakah user merekomedasikan produk yang mereka review dengan akurasi sebesar 84%. Untuk meningkatkan performa model, dapat dieksplorasi lebih lanjut mengenai review ditinggalkan oleh user yang di-endorse atau disponsori oleh brand yang di-review.

## Tools Used

Python, Pandas, Numpy, Seaborn, Matplotlib, Scikit-Learn, RegEx, NLTK, TensorFlow, Streamlit, HuggingFace
