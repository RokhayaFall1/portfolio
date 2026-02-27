import streamlit as st
st.set_page_config(page_title="CV Rokhaya Fall", layout="wide")
st.title("Rokhaya Fall, étudiante en géomatique")
with st.sidebar:
    #1.information personnelles
    st.image("image.jpg")
    st.title("Rokhaya FALL")
    st.markdown("Adresse: Keur Mbaye Fall, Dakar")
    st.markdown("Email: fallrokhaya146@gmail.com")
    st.markdown("Tél: +221 70 741 61 13")
    #2.ma page
st.header("Profil")
st.write(""" Etudiante en géomatique passionnée par l'analyse spacial et la cartogrophie numérique. Je posséde des compétence en systéme d'information géographique (SIG) et en programmation, notamment en python pour le codage et la visualisation des données géographiques. Je maitrise des outils comme ArcGIS et QGIS et je m'intéresse au développement d'application géospatiales avec streamlit.""") 
st.header("Compétences Techniques")
st.subheader("SIG")
st.write("""
- ArcGIS: Analyse spatiale, cartographie thématique 
- QGIS: Géotraitement, digitalisation 
- ERDAS Imagine: Classification d'images satéllites
""")
st.subheader("Programmation")
st.write("""
- Python: Analyse de données, automatisation SIG
- Streamlit: Développement d'application interactives
- SQL: Requêtes simples
""")
st.subheader("Analyse")
st.write("""
- Cartographie thématique
- Analyse de données géospatial
- Interprétation d'images satélittes
""")
st.header("Formation")
st.write("""
- BTS géomatique en cours
- Baccalauréat litéraire L2
""")
st.header("Qualité")
st.write("""
- Esprit d'analyse
- Organisation
- Travail en équipe
- Riqueur professionnelle
""")




    
