import streamlit as st
import pandas as pd
@st.cache
@st.cache_data
def long_running_function(param1, param2):
    return "…"
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded")


def load_data(file, formats,sp):
    if formats == "csv":
        data = pd.read_csv(file,sep=sp)
    else :
        data = pd.read_excel(file)
    return data
if "df" not in st.session_state :
    st.session_state.df = None
if "data" not in st.session_state :
  st.session_state.data = None

if "columns_to_use" not in st.session_state :
    st.session_state.columns_to_use = None
if "target_variable" not in st.session_state :
    st.session_state.target_variable = None

formats = ["csv","xlsx"]

col_1,col_2,col_3 = st.columns([1,1,7])
with col_1 :
  selected_format = st.radio('Format', formats)

with col_2 :
  sep = st.radio("Sep",[",",";"])
with col_3 :
  file = st.file_uploader("Upload your data here", type=[selected_format])


if file is not None:
    data = load_data(file, selected_format,sep)
    st.session_state.data = data
    

    st.dataframe(data,use_container_width=True)
    columns_to_use = []
    st.header("Select columns")

    columns_to_use = st.multiselect("\nSelect columns  to exclude for classification",options = data.columns)

    valider = st.button("Valider")
    
    if valider : 
        df = data.drop(columns_to_use, axis=1)
        st.session_state.df  = df

        st.dataframe(df,use_container_width=True)

    st.session_state.columns_to_use = columns_to_use
else : 
  st.image("img/img.jpeg")