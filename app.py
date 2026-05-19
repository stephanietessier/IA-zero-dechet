from pathlib import Path

import streamlit as st

from src.recommender import ZeroWasteRecommender
from src.utils import load_resources, find_resources

BASE_DIR = Path(__file__).resolve().parent
ITEMS_PATH = BASE_DIR / "data" / "items_zero_dechet.csv"
RESOURCES_PATH = BASE_DIR / "data" / "ressources_locales.csv"

st.set_page_config(page_title="IA Zéro Déchet", page_icon="♻️", layout="wide")

st.title("♻️ IA Zéro Déchet")
st.subheader("Assistant personnel de tri, réparation et réutilisation")

st.info(
    "Prototype éducatif. Les recommandations sont indicatives : vérifiez toujours les consignes de votre municipalité."
)

@st.cache_resource
def get_recommender():
    return ZeroWasteRecommender(str(ITEMS_PATH))

@st.cache_data
def get_resources():
    return load_resources(str(RESOURCES_PATH))

recommender = get_recommender()
resources = get_resources()

user_text = st.text_input(
    "Décris ton objet ou ton déchet :",
    placeholder="Ex. vieux téléphone avec écran brisé, pot de yogourt, manteau troué...",
)

if st.button("Trouver la meilleure option") or user_text:
    results = recommender.recommend(user_text, top_k=3)
    if not results:
        st.warning("Écris une courte description pour obtenir une recommandation.")
    else:
        best = results[0]
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f"## Recommandation principale : {best['action_prioritaire']}")
            st.write(f"**Objet le plus proche :** {best['objet']}")
            st.write(f"**Catégorie :** {best['categorie']}")
            st.write(f"**Pourquoi :** {best['explication']}")
            st.write(f"**Réutilisation possible :** {best['reutilisation']}")
            st.write(recommender.ecological_message(best["score_ecologique"]))
        with col2:
            st.metric("Score écologique", f"{int(best['score_ecologique'])}/100")
            st.caption(f"Similarité IA : {best['similarite']}")

        st.markdown("### Autres pistes possibles")
        for alt in results[1:]:
            st.write(
                f"- **{alt['objet']}** → {alt['action_prioritaire']} "
                f"({int(alt['score_ecologique'])}/100)"
            )

        st.markdown("### Ressources locales fictives pertinentes")
        relevant = find_resources(resources, best["categorie"])
        st.dataframe(relevant, use_container_width=True)

st.markdown("---")
st.caption("Projet open source fictif — IA sobre, locale et respectueuse de la vie privée.")
