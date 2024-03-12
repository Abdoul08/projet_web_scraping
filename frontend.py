
import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

st.write('''
         # reporting du nombre d'appel 
         ''')

# Faire une requête à l'API backend pour récupérer les données
req = requests.get("http://127.0.0.1:5000/index_front")

# Vérifier si la requête a réussi
if req.status_code == 200:
    # Convertir les données JSON en DataFrame Pandas
    data = pd.DataFrame(req.json())
    st.dataframe(data)
    
    # Widget de sélection pour le type de graphique
    graph_type = st.selectbox("Choisir le type de graphique", ["Histogramme", "Camembert"])
    
    if graph_type == "Histogramme":
        # Créer un histogramme empilé pour chaque catégorie avec Seaborn
        fig, ax = plt.subplots()
        n_bins = st.number_input(
            label="Choisir un nombre de bins",
            min_value=10,
            value=20
        )
        for column in data.columns:
            sns.histplot(data[column], bins=n_bins, alpha=0.5, label=column, ax=ax)
        
        ax.legend()
        title = st.text_input(label="Saisir le titre du graphe")
        st.title(title)
        st.pyplot(fig)
        
    elif graph_type == "Camembert":
        # Créer un camembert pour chaque catégorie avec Seaborn
        for column in data.columns:
            plt.figure()
            sns.countplot(data[column])
            plt.title(f"Répartition de {column}")
            st.pyplot()

else:
    st.error("Erreur lors de la récupération des données depuis l'API.")