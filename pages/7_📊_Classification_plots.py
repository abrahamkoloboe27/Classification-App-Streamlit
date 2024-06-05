import streamlit as st
from pycaret.classification import plot_model
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded")

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

dic = {
    "Learning Curve" : "learning",          "Confusion Matrix" :"confusion_matrix" ,
    "AUC Curve" : "auc",                    "Classification Report" : "class_report" ,
    "Feature Importance" : "feature",       "Validation Curve" : "vc",
    "Manifold Learning" : "manifold",       "Feature Importance (All)" : "feature_all",
    "Pipeline plot" : "pipeline",           "Discrimination Threshold" : "threshold" ,
    "Precision Recall Curve" : "pr",        "Class Prediction Error": "error",
    "Decision Boundary" : "boundary" ,      "Recursive Feature Selection" : "rfe" ,
    "Calibration Curve" : "calibration",    "Dimension Learning" : "dimension" ,
    "Model Hyperparameter" : "parameter" ,  "Lift Curve" : "lift",
    "Gain Chart" : "gain",                  "Decision Tree" : "tree",      
    "KS Statistic Plot" : "ks"}

st.header("Classifcation plots",divider='rainbow')
model = st.session_state.compare_models_class
if model is not None:
    mod = st.selectbox("Select a model", model)
    plot_ = st.sidebar.multiselect("Select a plot", options=dic.keys(),
        default=["Class Prediction Error","Confusion Matrix","Learning Curve","Validation Curve","AUC Curve","Classification Report","Precision Recall Curve"])
    col_1,col_2 = st.columns(2)
    i=1
    for plt in plot_ : 
        if plt != "Feature Importance" : 
            if i == 1 :
                with col_1 : 
                    st.subheader(plt)
                    try :
                        plot_model(estimator=mod, plot=dic[plt], display_format='streamlit')
                    except: 
                        st.warning("Impossible d'afficher ce graphique")
                    i = 2
            else : 
                with col_2 :
                    st.subheader(plt)
                    try:
                        plot_model(estimator=mod, plot=dic[plt], display_format='streamlit')
                    except: 
                        st.warning("Impossible d'afficher ce graphique")
                    i = 1
        else : 
            if i == 1 :
                with col_1 : 
                    st.subheader(plt)
                    try: 
                        plot_model(estimator=mod, plot=dic[plt], display_format='streamlit', save= True)
                        st.image("Feature Importance.png")
                    except: 
                        st.warning("Impossible d'afficher ce graphique")
                    i = 2
            else : 
                with col_2 :
                    st.subheader(plt)
                    try: 
                        plot_model(estimator=mod, plot=dic[plt], display_format='streamlit', save=True)
                        st.image("Feature Importance.png")
                    except: 
                        st.warning("Impossible d'afficher ce graphique")
                    i = 1
else:
    st.warning("No model trained ! ")