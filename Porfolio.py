iimport streamlit as st
from PIL import Image
import base64

st.set_page_config(
    page_title="CV - Technicien Supérieur en Géomatique",
    page_icon="🗺️",
    layout="wide"
)

# ================= STYLE =================
st.markdown("""
<style>
.main {
    background-color: #f4f6f7;
}
.title-name {
    font-size: 42px;
    font-weight: bold;
    color: #0B3C5D;
}
.subtitle {
    font-size: 22px;
    color: #1D70A2;
    font-weight: 500;
}
.section-title {
    font-size: 26px;
    font-weight: bold;
    color: #0B3C5D;
    margin-top: 30px;
}
.sidebar .sidebar-content {
    background-color: #0B3C5D;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
with st.sidebar:
    st.title("Informations")
    st.write("📍 Ville, Pays")
    st.write("📞 +XXX XX XX XX XX")
    st.write("📧 email@email.com")
    st.write("🔗 LinkedIn")
    
    st.markdown("---")
    st.subheader("Compétences Clés")
    st.write("• SIG & Cartographie")
    st.write("• Analyse spatiale")
    st.write("• Levés topographiques")
    st.write("• Gestion bases de données SIG")
    st.write("• Télédétection")

    st.markdown("---")
    st.subheader("Langues")
    st.write("Français : Courant")
    st.write("Anglais : Technique")

# ================= HEADER =================
col1, col2 = st.columns([1, 3])

with col1:
    image = Image.open("photo.jpg")  # Remplace par ton image
    st.image(image, width=230)

with col2:
    st.markdown('<p class="title-name">TON NOM</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Technicien Supérieur en Géomatique</p>', unsafe_allow_html=True)

    st.write("""
Technicien supérieur en géomatique spécialisé dans la gestion, 
l’analyse et la visualisation des données géospatiales.
Expérience en levés terrain, cartographie numérique et SIG.
Capacité à transformer les données spatiales en outils d’aide à la décision.
""")

st.markdown("---")

# ================= COMPÉTENCES TECHNIQUES =================
st.markdown('<p class="section-title">🛠 Compétences Techniques</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.write("QGIS")
    st.progress(90)

    st.write("ArcGIS")
    st.progress(85)

    st.write("AutoCAD / Covadis")
    st.progress(80)

with col2:
    st.write("GPS & Stations Totales")
    st.progress(88)

    st.write("Traitement Images Satellites")
    st.progress(82)

    st.write("Python (Analyse spatiale)")
    st.progress(70)

# ================= EXPÉRIENCE =================
st.markdown('<p class="section-title">💼 Expérience Professionnelle</p>', unsafe_allow_html=True)

st.markdown("""
### Technicien Géomatique – Société XYZ  
**2023 – Présent**

- Réalisation de cartes techniques et thématiques
- Analyse spatiale et traitement de données géographiques
- Collecte de données GPS et levés topographiques
- Mise à jour de bases de données SIG
- Production de plans pour projets d’aménagement
""")

st.markdown("""
### Stagiaire Géomatique – Bureau d'Études ABC  
**2022 – 2023**

- Digitalisation et géoréférencement de plans
- Appui aux levés terrain
- Création de bases de données cadastrales
- Production de rapports cartographiques
""")

# ================= PROJETS =================
st.markdown('<p class="section-title">🌍 Projets Réalisés</p>', unsafe_allow_html=True)

st.markdown("""
### 📌 Cartographie d’Occupation des Sols
- Classification d’images satellites
- Analyse multicritère sous QGIS
- Production de cartes thématiques

### 📌 Base de Données Cadastrale
- Structuration SIG
- Intégration données terrain
- Création couches vectorielles
""")

# ================= FORMATION =================
st.markdown('<p class="section-title">🎓 Formation</p>', unsafe_allow_html=True)

st.markdown("""
**Diplôme de Technicien Supérieur en Géomatique**  
Institut / École – 2023  

**Baccalauréat Scientifique**  
2019  
""")

# ================= CERTIFICATIONS =================
st.markdown('<p class="section-title">🏅 Certifications</p>', unsafe_allow_html=True)

st.write("• Certification QGIS Avancé")
st.write("• Formation Télédétection")
st.write("• Formation GPS & Station Totale")

# ================= SOFT SKILLS =================
st.markdown('<p class="section-title">🤝 Compétences Personnelles</p>', unsafe_allow_html=True)

st.write("""
- Rigueur et précision
- Esprit d’analyse
- Travail en équipe
- Adaptabilité terrain
- Sens de l’organisation
""")

# ================= FOOTER =================
st.markdown("---")
st.markdown("© 2026 - TON NOM | Technicien Supérieur en Géomatique")
