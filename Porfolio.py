import streamlit as st

# ================= CONFIG PAGE =================
st.set_page_config(
    page_title="Portfolio Géomaticien 🗺️",
    page_icon="🗺️",
    layout="wide"
)

# ================= STYLE =================
st.markdown("""
<style>
/* Fond blanc et texte noir pour toute la page et sidebar */
[data-testid="stAppViewContainer"] {
    background-color:gray;
    color: black;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: gray;
    color: black;
}

/* Titre centré en haut */
.title {
    font-size:60px;
    font-weight: bold;
    color: black;
    text-align: center;
    margin-bottom: 20px;
}

/* Sections */
.section {
    font-size: 26px;
    font-weight: bold;
    margin-top: 25px;
    color: black;
}
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
st.image("photo.jpeg")
st.sidebar.markdown("## 👨‍💼 Informations")
st.sidebar.markdown("### Mouhamed Dione")
st.sidebar.markdown("**🗺️ Technicien Supérieur en Géomatique**")
st.sidebar.markdown("---")
st.sidebar.write("📍 Dakar, Sénégal")
st.sidebar.write("📧 johnmouhamed378@gmail.com")
st.sidebar.write("🔗 www.linkedin.com/in/mouhamed-dione-76a08a376")
st.sidebar.markdown("---")
st.sidebar.info("Disponible pour opportunités professionnelles")

# ================= CONTENU PRINCIPAL =================

# ===== TITRE CENTRÉ =====
st.markdown('<p class="title">Curriculum Vitae</p>', unsafe_allow_html=True)

# ===== PROFIL =====
st.markdown('<p class="section">👤 Profil Professionnel</p>', unsafe_allow_html=True)
st.write("""
Technicien supérieur en géomatique spécialisé dans la gestion,
l’analyse et la visualisation des données géospatiales.

Expérience en levés terrain, cartographie numérique,
télédétection et production de plans techniques,
et aussi dans la programmation en Python.

Rigoureux, précis et orienté résultats.
""")

# ===== COMPÉTENCES =====
st.markdown('<p class="section">🛠️ Compétences Techniques</p>', unsafe_allow_html=True)
st.write("""
- 🗺️ QGIS  
- 🌍 ArcGIS  
- 📐 AutoCAD / Covadis  
- 📡 GPS & Stations Totales  
- 🛰️ Télédétection  
- 🐍 Python (Analyse spatiale)  
""")

# ===== EXPÉRIENCE =====
st.markdown('<p class="section">💼 Expérience Professionnelle</p>', unsafe_allow_html=True)
st.markdown("""

- Réalisation de cartes techniques
- Analyse spatiale sous QGIS
- Collecte de données GPS
- Gestion de bases de données SIG
""")

# ===== PROJETS =====
st.markdown('<p class="section">🌍 Projets Réalisés</p>', unsafe_allow_html=True)
st.markdown("""
- Classification d’images satellites
- Analyse multicritère
- Production cartographique
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
st.write(" Français : Courant")
st.write(" Anglais : Technique")

# ===== FOOTER =====
st.markdown("---")
st.markdown("© 2026 | Portfolio Géomaticien 🗺️")
