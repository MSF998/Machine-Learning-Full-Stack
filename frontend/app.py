import streamlit as st
import requests
import os

st.header("Hello")

API_URL = os.getenv('API_URL','http://localhost:8000')

st.info((requests.get(f"{API_URL}/health-check").text))