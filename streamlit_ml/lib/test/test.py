import streamlit as st

def upload(message='Upload file'):
    return st.file_uploader(message)

