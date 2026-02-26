import streamlit as st

st.set_page_config(
    page_title="CV - Technicien Supérieur en Géomatique 🗺️",
    page_icon="🗺️",
    layout="wide"
)

# ================= STYLE =================
st.markdown("""
<style>
.title {
    font-size: 42px;
    font-weight: bold;
    color: #0B3C5D;
}
.subtitle {
    font-size: 22px;
    color: #1D70A2;
}
.section {
    font-size: 26px;
    font-weight: bold;
    margin-top: 30px;
    color: #0B3C5D;
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
def header():
    st.markdown('<p class="title">👨‍💼 TON NOM</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">🗺️ Technicien Supérieur en Géomatique</p>', unsafe_allow_html=True)
    st.write("📍 Ville, Pays")
    
    st.write("📧 johnmouhadione378@email.com")
    st.write("🔗 LinkedIn | Portfolio")
    st.markdown("---")

# ================= PROFIL =================
def profil():
    st.markdown('<p class="section">👤 Profil Professionnel</p>', unsafe_allow_html=True)
    st.write("""
🎯 Technicien supérieur en géomatique spécialisé dans la gestion,
l’analyse et la visualisation des données géospatiales.

🛰️ Expérience en levés terrain, cartographie numérique,
traitement d’images satellites et production de plans techniques.

📊 Capacité à transformer les données spatiales
en outils d’aide à la décision.
""")

# ================= COMPETENCES =================
def competences():
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

        st.write("🛰️ Traitement d’images satellites")
        st.progress(82)

        st.write("🐍 Python (analyse spatiale)")
        st.progress(70)

# ================= EXPERIENCE =================
def experience():
    st.markdown('<p class="section">💼 Expérience Professionnelle</p>', unsafe_allow_html=True)

    st.markdown("""
### 🏢 Technicien Géomatique – Société XYZ  
📅 2023 – Présent

- 🗺️ Réalisation de cartes techniques  
- 📊 Analyse spatiale sous QGIS et ArcGIS  
- 📡 Collecte de données GPS  
- 🗃️ Gestion de bases de données géographiques  
""")

    st.markdown("""
### 🏢 Stagiaire Géomatique – Bureau d'Études ABC  
📅 2022 – 2023

- 📍 Levés topographiques  
- ✏️ Digitalisation de plans  
- 🗂️ Création de bases de données cadastrales  
""")

# ================= PROJETS =================
def projets():
    st.markdown('<p class="section">🌍 Projets Réalisés</p>', unsafe_allow_html=True)

    st.markdown("""
### 🛰️ Cartographie d’Occupation des Sols
- Classification d’images satellites  
- Production de cartes thématiques  

### 🏘️ Base de Données Cadastrale
- Structuration SIG  
- Intégration données terrain  
""")

# ================= FORMATION =================
def formation():
    st.markdown('<p class="section">🎓 Formation</p>', unsafe_allow_html=True)

    st.markdown("""
🎓 Diplôme de Technicien Supérieur en Géomatique – 2023  
📘 Baccalauréat Scientifique – 2019  
""")

# ================= LANGUES =================
def langues():
    st.markdown('<p class="section">🌐 Langues</p>', unsafe_allow_html=True)
    st.write("🇫🇷 Français : Courant")
    st.write("🇬🇧 Anglais : Technique")

# ================= EXECUTION =================
header()
profil()
competences()
experience()
projets()
formation()
langues()

st.markdown("---")
st.markdown("© 2026 🗺️ TON NOM | Technicien Supérieur en Géomatique")
