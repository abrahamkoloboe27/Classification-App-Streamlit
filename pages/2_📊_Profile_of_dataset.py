import streamlit as st
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded")
st.header("Profile Dataset",divider='rainbow')
st.warning("Cela ne fonctionne pas pour le moment, veuillez réessayer plus tard !")
