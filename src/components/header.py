import streamlit as st

def header_home():

   
    st.markdown("""
                <div style='display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px;'>
               <img src='https://i.ibb.co/YTYGn5qV/logo.png' style='height:100px;'>
                <h1 style='text-align:center; color:#e0e3ff'>SNAP<br>CLASS</h2>

                </div>
                
                """,unsafe_allow_html=True)
    

def header_dashboard():

   
    st.markdown("""
                <div style='display:flex;align-items:center; gap:14px; '>
               <img src='https://i.ibb.co/YTYGn5qV/logo.png' style='height:90px;'>
                <h2 style='text-align:left; color:#3b3b3b;margin-top:20px'>SNAP<br>CLASS</h2>

                </div>
                
                """,unsafe_allow_html=True)

