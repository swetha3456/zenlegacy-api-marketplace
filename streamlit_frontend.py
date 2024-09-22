import streamlit as st
import os
from create_api import deploy_code

st.title("AI-Powered API Marketplace")
ip_address = "3.91.28.105"

prompt = st.text_input("Enter your prompt:", "API to store and retrieve employee data")

if st.button("Deploy!"):
    deploy_code(prompt)
    st.markdown(f"Use this IP address and port: http://{ip_address}:8080/")
    st.markdown(f"FastAPI Documentation: http://{ip_address}:8080/docs")
    os.system("uvicorn main:app --host 0.0.0.0 --port 8080 --reload")