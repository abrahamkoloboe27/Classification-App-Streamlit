import streamlit as st
import pandas as pd
from pycaret.datasets import get_data


st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded")

@st.cache
@st.cache_data
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


with st.sidebar : 
        st.markdown("""
        ## Auteur
        :blue[Abraham KOLOBOE]
        * Email : <abklb27@gmail.com>
        * WhatsApp : +229 91 83 84 21
        * Linkedin : [Abraham KOLOBOE](https://www.linkedin.com/in/abraham-zacharie-koloboe-data-science-ia-generative-llms-machine-learning)
                    """)

if st.toggle("Importer un fichier") :
  col_1,col_2,col_3 = st.columns([1,1,7])
  with col_1 :
    selected_format = st.radio('Format', formats)

  with col_2 :
    sep = st.radio("Sep",[",",";"])

  with col_3 :
    file = st.file_uploader("Importez vos données ici", type=[selected_format])
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
  st.write("Veuillez choisir un dataset")
  with st.expander("Liste des datasets", True) :
    list_index = st.selectbox("Liste des datasets",["iris","wine","credit"])
    if list_index == "iris" :
       st.markdown("""
        ## Iris Dataset
        Ce jeu de données contient 150 échantillons de 3 classes différentes d'iris (Setosa, Versicolour, et Virginica).
        Les caractéristiques sont la longueur et la largeur des sépales et des pétales en centimètres.
                   """)
    elif list_index == "wine" :
        st.markdown("""
        ## Wine Dataset
        Ce jeu de données contient 178 échantillons de 3 classes différentes de vin (classées en fonction de la variété).
        Les caractéristiques sont les résultats d'une analyse chimique de vins cultivés dans la même région en Italie.
                   """)
    else : 
        st.markdown("""
        ## Credit Dataset
        Ce jeu de données contient 1000 échantillons de 2 classes différentes (bon crédit, mauvais crédit).
        Les caractéristiques sont les informations sur les prêts, les paiements, les soldes, etc.
                   """)
    if st.button("Valider") : 
        data = get_data(list_index)
        data = data.iloc[:500,:]
        st.session_state.data = data    
        st.dataframe(data,use_container_width=True)
        columns_to_use = data.columns          
        st.session_state.df  = data
        st.session_state.columns_to_use = columns_to_use
     

