import streamlit as st
import requests
import os

st.header("Hello")

API_URL = os.getenv('API_URL','http://localhost:8000')

test_btn = st.button("TEST")

if test_btn:
    st.info(API_URL)
    st.info((requests.get(f"{API_URL}/").text))