import streamlit as st
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded")
st.header("Classification Application",divider='rainbow')    
if st.sidebar.toggle("A propos de l'auteur", True):
    with st.expander("Auteur", True) : 
        c1, c2 = st.columns([1,2])
        with c1 :
            st.image("img/About the author.png")
        with c2 : 
            st.header(""" **S. Abraham Z. KOLOBOE**""")
            st.markdown("""
                
                *:blue[Data Scientist | Ingénieur en Mathématiques et Modélisation]*

                Bonjour,

                Je suis Abraham, un Data Scientist et Ingénieur en Mathématiques et Modélisation. 
                Mon expertise se situe dans les domaines des sciences de données et de l'intelligence artificielle. 
                Avec une approche technique et concise, je m'engage à fournir des solutions efficaces et précises dans mes projets.
                        
                * Email : <abklb27@gmail.com>
                * WhatsApp : +229 91 83 84 21
                * Linkedin : [Abraham KOLOBOE](https://www.linkedin.com/in/abraham-zacharie-koloboe-data-science-ia-generative-llms-machine-learning)
                    
                                    """)
with st.sidebar : 
        st.markdown("""
        ## Auteur
        :blue[Abraham KOLOBOE]
        * Email : <abklb27@gmail.com>
        * WhatsApp : +229 91 83 84 21
        * Linkedin : [Abraham KOLOBOE](https://www.linkedin.com/in/abraham-zacharie-koloboe-data-science-ia-generative-llms-machine-learning)
                    """)
st.markdown("""

### **:blue[Description de l'Application Streamlit pour la Création et l'Entraînement de Modèles de Classification avec PyCaret]**

L'application Streamlit que j'ai créée offre une interface conviviale pour l'importation, le profilage, la configuration, l'entraînement, l'évaluation, le réglage fin, et la sauvegarde des modèles de classification en utilisant PyCaret. Voici un aperçu des fonctionnalités de chaque page :

**Page 1 : Importez vos données**
- Permet aux utilisateurs d'importer leurs données au format CSV ou Excel.
- Affiche un aperçu des données avec la possibilité de sélectionner les colonnes à utiliser pour la classification.
- Offre des options de prétraitement telles que la sélection du séparateur CSV.

**Page 2 : Profil du jeu de données**
- Profil détaillé du jeu de données à l'aide de pandas-profiling.
- Affiche les statistiques, les graphiques et les informations sur les variables.

**Page 3 : Configuration**
- Permet aux utilisateurs de configurer les paramètres de l'entraînement, y compris la variable cible, la taille d'entraînement, les méthodes d'imputation, la normalisation, et la validation croisée.

**Page 4 : Entraînez le modèle**
- Entraîne plusieurs modèles de classification en utilisant PyCaret.
- Permet de personnaliser le choix des modèles et la métrique d'évaluation.
- Affiche les performances comparatives des modèles entraînés.

**Page 5 : Rapport d'Entraînement**
- Présente un rapport détaillé sur les performances des modèles entraînés.
- Permet de visualiser les graphiques comparatifs basés sur différentes métriques sélectionnées par l'utilisateur.

**Page 6 : Graphiques de Classification**
- Affiche des graphiques spécifiques au modèle sélectionné, tels que la courbe d'apprentissage, la matrice de confusion, le rapport de classification, etc.

**Page 7 : Ajustement Fin**
- Permet aux utilisateurs de régler finement les hyperparamètres des modèles pour améliorer les performances.
- Utilise différentes bibliothèques d'optimisation telles que scikit-learn, scikit-optimize, tune-sklearn, optuna, etc.

**Page 8 : Finalisation et Sauvegarde**
- Finalise le meilleur modèle sélectionné après ajustement fin.
- Permet aux utilisateurs de nommer et de sauvegarder leur modèle entraîné.
- Offre la possibilité de télécharger le modèle sauvegardé.

Cette application simplifie le processus de création et d'entraînement de modèles de classification, offrant aux utilisateurs une plateforme interactive pour explorer et optimiser leurs modèles de machine learning.
            """)

