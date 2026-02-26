import streamlit as st

st.set_page_config(
    page_title="Portfolio Géomaticien 🗺️",
    page_icon="🗺️",
    layout="wide"
)

# ================= STYLE =================
st.markdown("""
<style>
/* Fond blanc et texte noir pour toute la page */
body {
    background-color: white;
    color: black;
}

/* Sidebar style */
.stSidebar {
    background-color: #f5f5f5;  /* gris clair pour distinguer la sidebar */
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
    font-size: 26px;
    font-weight: bold;
    margin-top: 25px;
    color: black;
}
</style>
""", unsafe_allow_html=True)


# ================= SIDEBAR (INFOS PERSONNELLES) =================
st.sidebar.markdown("## 👨‍💼 Informations")

st.sidebar.markdown("### TON NOM")
st.sidebar.markdown("**🗺️ Technicien Supérieur en Géomatique**")

st.sidebar.markdown("---")
st.sidebar.write("📍 Ville, Pays")
st.sidebar.write("📧 johnmouhamed378@gmail.com")


st.sidebar.markdown("---")


# ================= CONTENU PRINCIPAL =================

# ===== PROFIL =====
st.markdown('<p class="section">👤 Profil Professionnel</p>', unsafe_allow_html=True)

st.write("""
Technicien supérieur en géomatique spécialisé dans la gestion,
l’analyse et la visualisation des données géospatiales.

Expérience en levés terrain, cartographie numérique,
télédétection et production de plans techniques.

Rigoureux, précis et orienté résultats.
""")

# ===== COMPÉTENCES =====
st.markdown('<p class="section">🛠️ Compétences Techniques</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.write("🗺️ QGIS")
    

    st.write("🌍 ArcGIS")
   

    st.write("📐 AutoCAD / Covadis")
    

with col2:
    st.write("📡 GPS & Stations Totales")


    st.write("🛰️ Télédétection")


    st.write("🐍 Python (Analyse spatiale)")
   

# ===== EXPÉRIENCE =====
st.markdown('<p class="section">💼 Expérience Professionnelle</p>', unsafe_allow_html=True)

st.markdown("""

- Réalisation de cartes techniques
- Analyse spatiale sous QGIS
- Collecte de données GPS
- Gestion de bases de données SIG


- Levés topographiques
- Digitalisation de plans
- Production cartographique
""")

# ===== PROJETS =====
st.markdown('<p class="section">🌍 Projets Réalisés</p>', unsafe_allow_html=True)

st.markdown("""
### 🛰️ Cartographie d’Occupation des Sols
- Classification d’images satellites
- Analyse multicritère
- Production cartographique

### 🏘️ Base de Données Cadastrale
- Structuration SIG
- Intégration données terrain
""")

# ===== FORMATION =====
st.markdown('<p class="section">🎓 Formation</p>', unsafe_allow_html=True)

st.write("""
🎓 Diplôme de Technicien Supérieur en Géomatique – 2026  
📘 Baccalauréat Scientifique – 2024  
""")

# ===== LANGUES =====
st.markdown('<p class="section">🌐 Langues</p>', unsafe_allow_html=True)

st.write("🇫🇷 Français : Courant")
st.write("🇬🇧 Anglais : Technique")

# ================= FOOTER =================
st.markdown("---")
st.markdown("© 2026 | Portfolio Géomaticien 🗺️")
