import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('child_sexual.sav', 'rb'))

st.title('Prediksi Kesadaran Pelecehan Seksual Anak')
c1, c2 = st.columns(2)

with c1:
   Children_safe = st.number_input('Anak-anak aman di antara anggota keluarga')
   Male_children_dont_need_sexual_abuse = st.number_input('Anak laki-laki tidak membutuhkan pengetahuan pencegahan pelecehan seksual')
   child_grooming = st.number_input('Tahukah Anda apa itu child grooming')
   need_counseling_for_recovering = st.number_input('Apakah anak-anak membutuhkan konseling pasca pelecehan')

with c2:
   Children_are_bused = st.number_input('Anak-anak terutama dilecehkan oleh orang asing')
   Teaching_sexual_abuse = st.number_input('Mengajarkan pencegahan pelecehan seksual di sekolah')
   signs_your_child_has_been_abused = st.number_input('Tanda-tanda untuk mengidentifikasi apakah anak Anda telah dilecehkan?')
   take_legal_action = st.number_input('Apakah Anda harus mengambil tindakan hukum terhadap pelaku kekerasan anak')

prediksi = ''
if st.button('Hasil Prediksi'):
    prediksi = model.predict([[Children_safe, Children_are_bused, Male_children_dont_need_sexual_abuse,
                                Teaching_sexual_abuse, child_grooming, signs_your_child_has_been_abused,
                                need_counseling_for_recovering, take_legal_action]])

    if (prediksi [0] == 0):
        prediksi = ('Mulai Memahami Tentang Kekerasan Seksual Pada Anak')
    else:
        prediksi = ('Sudah Memahami Tentang Kekerasan Seksual Pada Anak')
st.success(prediksi)