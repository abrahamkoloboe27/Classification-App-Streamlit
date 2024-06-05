import streamlit as st
import pandas as pd
from pycaret.classification import pull, compare_models
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded")

if "setup_class" not in st.session_state :
    st.session_state.setup_class = None
if "compare_models_class" not in st.session_state :
    st.session_state.compare_models_class = None
if "compare_models_pull" not in st.session_state :
    st.session_state.compare_models_pull = None
    
if "metric" not in st.session_state :
    st.session_state.metric = None
    
dic = {
    "Logistic Regression" :  "lr",                      "K Neighbors Classifier" : "knn",
    "Naive Bayes" : "nb",                               "Decision Tree Classifier" :  "dt",
    "SVM - Linear Kernel" : "svm",                      "SVM - Radial Kernel" : "rbfsvm" ,
    "Gaussian Process Classifier" : "gpc",              "MLP Classifier" : "mlp",
    "Ridge Classifier" : "ridge",                       "Random Forest Classifier": "rf",
    "Quadratic Discriminant Analysis" : "qda",          "Ada Boost Classifier" : "ada",
    "Gradient Boosting Classifier" : "gbc",             "Linear Discriminant Analysis" : "lda",
    "Extra Trees Classifier" : "et",                    "Extreme Gradient Boosting" : "xgboost" ,
    "Light Gradient Boosting Machine" : "lightgbm",     "CatBoost Classifier" : "catboost" 
    }
n_mod = 18
@st.cache
@st.cache_data
def long_running_function(param1, param2):
    return "…"

st.header("Training models",divider='rainbow')

exclude = ["SVM - Linear Kernel","SVM - Radial Kernel","Gaussian Process Classifier","MLP Classifier" ]
setup_class = st.session_state.setup_class
if setup_class is not None :
    with st.form(""" # Train models""") :
        models = st.multiselect("Select models to exclude ",options= dic.keys(), 
            default=exclude)
        mod = [dic[i] for i in models]
        col_1,col_2 = st.columns(2)
        with col_1 :
            st.subheader("Metric")
            metric = st.selectbox("Select a metric",
                [ "AUC", "Accuracy","F1", "Recall", "F1","Kappa","MCC","Prec."])
            st.session_state.metric = metric
        with col_2 : 
            st.subheader("Number of models to save")
            num_models = st.slider("Number of models", max_value=(n_mod - len(exclude)), min_value=1, value=int((1*(n_mod - len(exclude)))/4) )
        train_boutton = st.form_submit_button("🏄 Train !")
    if train_boutton :
        with st.spinner("Entrainement en cours..."):
            compare_models_class = compare_models(exclude=mod, sort=metric, n_select=num_models, turbo=False)
        compare_models_pull = pull()
        st.session_state.compare_models_class = compare_models_class
        st.session_state.compare_models_pull = compare_models_pull
        st.success("Training successfull ! ")
        st.dataframe(compare_models_pull.style.highlight_max(axis=0),use_container_width=True)

else:
    st.warning("No setup ! ")