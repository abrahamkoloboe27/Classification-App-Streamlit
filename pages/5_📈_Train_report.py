import streamlit as st
import pandas as pd
import plotly.express as px
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

def top_models_by_metric(pull_report, metric, m):
      # Trier le DataFrame pull_report par la métrique spécifiée (dans l'ordre décroissant)
  pull_report_sorted = pull_report.sort_values(by=metric, ascending=False)
    
  # Sélectionner les m premières lignes (c'est-à-dire les m modèles les plus performants)
  top_m_models = pull_report_sorted.head(m)
    
  return top_m_models

st.header("Train Report",divider='rainbow')
pull_report = st.session_state.compare_models_pull
best_model = st.session_state.compare_models_class
if best_model is not None :
    num_compare = st.sidebar.slider("Nombre de models a comparer", min_value = 2, max_value =len(pull_report), value=int((len(pull_report)*3)/4))
    metric = st.sidebar.multiselect("Métrique",pull_report.drop("Model",axis=1).columns, default = ["AUC","Accuracy","Prec.","F1","Recall"])
        
    for metrics in metric :
        to_plot = top_models_by_metric(pull_report,metrics,num_compare)
        fig = px.bar(to_plot, x=to_plot.index, y = metrics, color = "Model", title = f"Model comparaison by {metrics}")
        st.plotly_chart(fig,use_container_width=True)
else:
    st.warning("No model trained ! ")