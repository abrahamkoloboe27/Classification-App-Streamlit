import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded")

@st.cache
@st.cache_data
def long_running_function(param1, param2):
    return "…"


if "df" not in st.session_state :
    st.session_state.df = None
if "data" not in st.session_state :
  st.session_state.data = None

if "columns_to_use" not in st.session_state :
    st.session_state.columns_to_use = None
if "target_variable" not in st.session_state :
    st.session_state.target_variable = None
    
if "setup_class" not in st.session_state :
    st.session_state.setup_class = None

st.header("Profile Dataset",divider='rainbow')
df = st.session_state.df
if df is not None : 
    profile = st.button("Profile Dataset")
    if profile:
        profile_df = df.profile_report()
        st_profile_report(profile_df)
else : 
    st.warning("No data to profile !")