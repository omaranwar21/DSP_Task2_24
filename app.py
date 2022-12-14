import streamlit as st
from utils import *



st.set_page_config(
    page_title="Equalizer",
    page_icon="🔉",
    layout="wide"
)


with open("style.css") as design:
    st.markdown(f"<style>{design.read()}</style>", unsafe_allow_html=True)


left_col, right_col = st.columns((1, 4))
left_spectrogram_col, right_spectrogram_col, sub_right_spectrogram_col = st.columns(
    (1, 2, 2))
audio_left_col, audio_right_col = st.columns((1, 4))
sliders_cols = st.columns((1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
labels_cols = st.columns(11)


with left_col:
    signal, samplingRate = getFile()

