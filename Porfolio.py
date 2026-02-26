import streamlit as st

st.set_page_config(
    page_title="Portfolio Géomaticien 🗺️",
    page_icon="🗺️",
    layout="wide"
)

# ================= STYLE =================
st.markdown("""
<style>
.name {
    font-size: 32px;
    font-weight: bold;
    color: #0B3C5D;
}
.profession {
    font-size: 18px;
    color: gray;
}
.section {
    font-size: 26px;
    font-weight: bold;
    margin-top: 25px;
    color: #0B3C5D;
}
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR (INFOS PERSONNELLES) =================

st.sidebar.markdown("## 👨‍💼 Informations")

st.sidebar.markdown("### Mouhamed Dione")
st.sidebar.markdown("**🗺️ Technicien Supérieur en Géomatique**")

st.sidebar.markdown("---")
st.sidebar.write("📍 Dakar, Sénégal")
st.sidebar.write("📧 johnmouhamed378@gmail.com")
st.sidebar.write("🔗 www.linkedin.com/in/mouhamed-dione-76a08a376")

st.sidebar.markdown("---")


# ================= CONTENU PRINCIPAL =================

# ===== PROFIL =====
st.markdown('<p class="section">👤 Profil Professionnel</p>', unsafe_allow_html=True)

st.write("""
Technicien supérieur en géomatique spécialisé dans la gestion,
l’analyse et la visualisation des données géospatiales.

Expérience en levés terrain, cartographie numérique,
télédétection et production de plans techniques.
et aussi dans la programmation en python

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
### 🏢 Technicien Géomatique – Société XYZ (2023–Présent)
- Réalisation de cartes techniques
- Analyse spatiale sous QGIS
- Collecte de données GPS
- Gestion de bases de données SIG


# ===== PROJETS =====
st.markdown('<p class="section">🌍 Projets Réalisés</p>', unsafe_allow_html=True)

st.write("""
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
🎓 Diplôme de Technicien Supérieur en Géomatique  
📘 Baccalauréat Scientifique -2024  
""")

# ===== LANGUES =====
st.markdown('<p class="section">🌐 Langues</p>', unsafe_allow_html=True)

st.write("🇫🇷 Français : Courant")
st.write("🇬🇧 Anglais : Technique")

# ================= FOOTER =================
st.markdown("---")
st.markdown("© 2026 | Portfolio Géomaticien 🗺️")
