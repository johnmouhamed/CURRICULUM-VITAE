import streamlit as st
st.title("CURRICULUM VITAE")
# ================= CONFIG PAGE =================
st.set_page_config(
    page_title="Portfolio Géomaticien 🗺️",
    page_icon="🗺️",
    layout="wide"
)

# ================= STYLE =================
st.markdown("""
<style>
/* Fond blanc et texte noir pour le contenu principal */
[data-testid="stAppViewContainer"] {
    background-color: white;
    color: black;
}

/* Titres et sections */
.name {
    font-size: 32px;
    font-weight: bold;
    color: black;
}
.profession {
    font-size: 18px;
    color: black;
}
.section {
    font-size: 30px;
    font-weight: bold;
    margin-top: 25px;
    color: black;
}
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: white;
    color: black;
}
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
# Infos personnelles dans sidebar
st.sidebar.markdown("## 👨‍💼 Informations")
st.sidebar.markdown("### Mouhamed Dione")
st.sidebar.markdown("**🗺️ Technicien Supérieur en Géomatique**")
st.sidebar.markdown("---")
st.sidebar.write("📍 Dakar, Sénégal")
st.sidebar.write("📧 johnmouhamed378@gmail.com")
st.sidebar.write("🔗 www.linkedin.com/in/mouhamed-dione-76a08a376")
st.sidebar.markdown("---")


# ================= CONTENU PRINCIPAL =================
# Profil
st.markdown('<p class="section">👤 Profil Professionnel</p>', unsafe_allow_html=True)
st.write("""
Technicien supérieur en géomatique spécialisé dans la gestion,
l’analyse et la visualisation des données géospatiales.

Expérience en levés terrain, cartographie numérique,
télédétection et production de plans techniques,
et aussi dans la programmation en Python.

Rigoureux, précis et orienté résultats.
""")

# Compétences
st.markdown('<p class="section">🛠️ Compétences Techniques</p>', unsafe_allow_html=True)
st.write("""
- 🗺️ QGIS  
- 🌍 ArcGIS  
- 📐 AutoCAD / Covadis  
- 📡 GPS & Stations Totales  
- 🛰️ Télédétection  
- 🐍 Python (Analyse spatiale)  
""")

# Expérience
st.markdown('<p class="section">💼 Expérience Professionnelle</p>', unsafe_allow_html=True)
st.markdown("""

- Réalisation de cartes techniques
- Analyse spatiale sous QGIS
- Collecte de données GPS
- Gestion de bases de données SIG
""")

# Projets
st.markdown('<p class="section">🌍 Projets Réalisés</p>', unsafe_allow_html=True)
st.markdown("""

- Classification d’images satellites
- Analyse multicritère
- Production cartographique
- Structuration SIG
- Intégration données terrain
""")

# Formation
st.markdown('<p class="section">🎓 Formation</p>', unsafe_allow_html=True)
st.write("""
🎓 Diplôme de Technicien Supérieur en Géomatique – 2023  
📘 Baccalauréat Scientifique – 2024  
""")

# Langues
st.markdown('<p class="section">🌐 Langues</p>', unsafe_allow_html=True)
st.write(" Français : Courant")
st.write(" Anglais : Technique")

# Footer
st.markdown("---")
st.markdown("© 2026 | Portfolio Géomaticien 🗺️")
