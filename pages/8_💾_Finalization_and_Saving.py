import streamlit as st 
from pycaret.classification import save_model
from pycaret.classification import finalize_model

if "setup_class" not in st.session_state :
    st.session_state.setup_class = None
if "compare_models_class" not in st.session_state :
    st.session_state.compare_models_class = None
if "compare_models_pull" not in st.session_state :
    st.session_state.compare_models_pull = None
    
@st.cache
@st.cache_data
def long_running_function(param1, param2):
    return "…"

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded")


model = st.session_state.compare_models_class
st.header("Finalization and Saving",divider='rainbow')
if model is not None:
    
    with st.form("Finalization and Saving") : 
        best_model = st.selectbox("Choice model",model)
        nom_model = st.text_input("Name your model")
        submit = st.form_submit_button("Save")
    if submit  :
            with st.spinner("Enregistrement en cours ...") :
                save_model(finalize_model(best_model), model_name=nom_model)
            st.success("Saving success ! ")
            # Download the model
            with open(f"{nom_model}.pkl", 'rb') as f: 
                st.download_button('Download Model', f, file_name=f"{nom_model}.pkl")
        
else:
    st.warning("No model trained ! ")
      