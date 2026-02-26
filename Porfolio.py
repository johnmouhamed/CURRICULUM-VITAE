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
st.sidebar.write("🔗 LinkedIn")

st.sidebar.markdown("---")
st.sidebar.info("Disponible pour opportunités professionnelles")

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
    st.progress(90)

    st.write("🌍 ArcGIS")
    st.progress(85)

    st.write("📐 AutoCAD / Covadis")
    st.progress(80)

with col2:
    st.write("📡 GPS & Stations Totales")
    st.progress(88)

    st.write("🛰️ Télédétection")
    st.progress(82)

    st.write("🐍 Python (Analyse spatiale)")
    st.progress(70)

# ===== EXPÉRIENCE =====
st.markdown('<p class="section">💼 Expérience Professionnelle</p>', unsafe_allow_html=True)

st.markdown("""
### 🏢 Technicien Géomatique – Société XYZ (2023–Présent)
- Réalisation de cartes techniques
- Analyse spatiale sous QGIS
- Collecte de données GPS
- Gestion de bases de données SIG

### 🏢 Stagiaire Géomatique – Bureau d'Études ABC (2022–2023)
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
