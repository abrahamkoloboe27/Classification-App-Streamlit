import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report


st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded")
st.header("Profile Dataset",divider='rainbow')
if "df" not in st.session_state :
  st.session_state.df = None
st.title("Profile Report")
df = st.session_state.df 
if df is not None : 
  pr = df.profile_report()

  st_profile_report(pr)
else :
  st.warning("Pas de données")