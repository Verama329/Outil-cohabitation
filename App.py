# -*- coding: utf-8 -*-
import streamlit as st
import plotly.graph_objects as go

# 1. CONFIGURATION
st.set_page_config(page_title="Radar Cohabitation", page_icon="🎯", layout="wide")

# CSS pour améliorer la lisibilité du texte long
st.markdown("""
    <style>
    .report-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .action-box {
        background-color: #e8f4f8;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    h3 { color: #2c3e50; }
    h4 { color: #1f77b4; margin-top: 15px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎯 Le Radar de Maturité en Cohabitation")
st.info("Répondez aux questions dans le menu de gauche pour générer votre rapport détaillé.")

# --- DONNÉES DES QUESTIONS ---
questions_data = {
    "Axe A : Gouvernance & Protocoles": {
        "Q1. Protocole de gestion des comportements": ["1 pt - Réactif", "2 pts - Formel", "3 pts - Collaboratif", "4 pts - Systémique"],
        "Q2. Engagements avec le voisinage": ["1 pt - Réactif", "2 pts - Formel", "3 pts - Collaboratif", "4 pts - Systémique"],
        "Q3. Rôles et responsabilités": ["1 pt - Réactif", "2 pts - Formel", "3 pts - Collaboratif", "4 pts - Systémique"],
        "Q4. Mesure d'impact": ["1 pt - Réactif", "2 pts - Formel", "3 pts - Collaboratif", "4 pts - Systémique"]
    },
    "Axe B : Opérations & Terrain": {
        "Q5. Gestion des crises médiatiques": ["1 pt - Réactif", "2 pts - Formel", "3 pts - Collaboratif", "4 pts - Systémique"],
        "Q6. Formation des intervenants": ["1 pt - Réactif", "2 pts - Formel", "3 pts - Collaboratif", "4 pts - Systémique"],
        "Q7. Intervention hors murs": ["1 pt - Réactif", "2 pts - Formel", "3 pts - Collaboratif", "4 pts - Systémique"],
        "Q8. Gestion des exclusions": ["1 pt - Réactif", "2 pts - Formel", "3 pts - Collaboratif", "4 pts - Systémique"]
    },
    "Axe C : Alliances & Partenariats": {
        "Q9. Relation services municipaux": ["1 pt - Réactif", "2 pts - Formel", "3 pts - Collaboratif", "4 pts - Systémique"],
        "Q10. Collaboration organismes": ["1 pt - Réactif", "2 pts - Formel", "3 pts - Collaboratif", "4 pts - Systémique"],
        "Q11. Implication citoyenne": ["1 pt - Réactif", "2 pts - Formel", "3 pts - Collaboratif", "4 pts - Systémique"],
        "Q12. Médiation sociale dédiée": ["1 pt - Réactif", "2 pts - Formel", "3 pts - Collaboratif", "4 pts - Systémique"]
    }
}

# --- SIDEBAR ---
scores = {}
with st.sidebar:
    st.header("📝 Diagnostic")
    for axe, q_dict in questions_data.items():
        with st.expander(axe, expanded=True):
            for q, options in q_dict.items():
                choix = st.radio(q, options, index=0)
                scores[q] = int(choix.split(" ")[0])

# --- CALCULS ---
total = sum(scores.values())
axe_a = sum(list(scores.values())[0:4])
axe_b = sum(list(scores.values())[4:8])
axe_c = sum(list(scores.values())[8:12])

# --- DÉFINITION DU CONTENU TEXTUEL COMPLET ---
# C'est ici que nous intégrons tout votre texte Word
def get_content(score):
    if score <= 24:
        return {
            "titre": "PROFIL 1 : LE POMPIER SOLITAIRE",
            "couleur": "error",
            "intro": "Vous êtes en mode survie. Votre équipe gère au jour le jour, sans protocoles formalisés, avec peu ou pas de collaboration structurée avec le voisinage ou les partenaires externes. Les crises éclatent, vous réagissez, et vous recommencez le lendemain.",
            "forces": """
            - Vous êtes sur le terrain, proche des usagers.
            - Vous faites preuve de résilience et d'adaptation constante.
            - Vous connaissez intimement les réalités de votre clientèle.""",
            "risques": """
            - **Épuisement de l'équipe** : Tout repose sur quelques personnes clés. Le turnover est élevé.
            - **Incohérence** : Chaque intervenant gère les situations à sa façon. Pas de prévisibilité.
            - **Vulnérabilité médiatique** : Une vidéo virale et vous n'avez aucun filet de sécurité.
            - **Isolement** : Vous êtes perçu comme « le problème » par le voisinage et la Ville.""",
            "action_titre": "Créez votre premier protocole d'intervention écrit",
            "action_why": "Parce que c'est le fondement de tout. Tant que vos intervenants n'ont pas un cadre clair et partagé, vous resterez en mode réactif.",
            "action_how": "Allez lire le **Chapitre 3** : Principes d'intervention et gestion quotidienne.",
            "priorites": ["Chapitre 3 (Maintenant)", "Chapitre 1 (3-6 mois)", "Chapitre 6 (3-6 mois)"]
        }
    elif score <= 33:
        return {
            "titre": "PROFIL 2 : LE GESTIONNAIRE STRUCTURÉ",
            "couleur": "warning",
            "intro": "Vous avez posé des bases solides. Vous avez des protocoles écrits et des règles claires. Mais l'application reste inégale, les partenariats sont informels, et vous sentez que votre approche pourrait être plus fluide et collaborative.",
            "forces": """
            - Vous avez des outils et des procédures (règlements, protocoles de base).
            - Votre équipe connaît les attentes minimales.
            - Vous documentez certaines de vos interventions.""",
            "risques": """
            - **Rigidité** : Vos protocoles existent, mais sont appliqués de façon mécanique.
            - **Relations tendues** : Vous gérez les plaintes sans avoir construit de lien de confiance.
            - **Silos** : Vous fonctionnez en vase clos.
            - **Communication défensive** : En cas de crise, vous ne maîtrisez pas la narration.""",
            "action_titre": "Formalisez vos relations avec le voisinage (Pacte de bon voisinage)",
            "action_why": "Parce que vous avez la structure interne, mais il vous manque le pont vers l'externe. Un Pacte transforme les plaintes récurrentes en dialogue structuré.",
            "action_how": "Allez lire le **Chapitre 5** : Outils de structuration des relations.",
            "priorites": ["Chapitre 4 (Maintenant)", "Chapitre 5 (Maintenant)", "Chapitre 7 (3-6 mois)"]
        }
    elif score <= 42:
        return {
            "titre": "PROFIL 3 : LE PARTENAIRE STRATÉGIQUE",
            "couleur": "info",
            "intro": "Vous êtes dans le peloton de tête. Vous avez des protocoles solides et des partenariats actifs. Votre organisme est reconnu comme un acteur de solutions. Mais vous sentez qu'il reste des angles morts à optimiser.",
            "forces": """
            - Protocoles clairs et appliqués de façon cohérente.
            - Partenariats structurés avec la Ville et le voisinage.
            - Capacité à gérer les crises sans panique.""",
            "risques": """
            - **Proactivité vs Réactivité** : Vous gérez bien les crises, mais pourriez-vous les anticiper davantage ?
            - **Mesure d'impact** : Vous collectez des données, mais les exploitez-vous stratégiquement ?
            - **Innovation** : Pourriez-vous tester de nouvelles approches (médiation dédiée) ?""",
            "action_titre": "Structurez votre tableau de bord d'impact",
            "action_why": "Pour démontrer votre valeur ajoutée de manière chiffrée afin de sécuriser du financement et influencer les décisions municipales.",
            "action_how": "Allez lire le **Chapitre 8** : Mesurer votre impact pour durer.",
            "priorites": ["Chapitre 8 (Maintenant)", "Chapitre 7 (Maintenant)", "Chapitre 6 (Pour aller plus loin)"]
        }
    else:
        return {
            "titre": "PROFIL 4 : L'INNOVATEUR SYSTÉMIQUE",
            "couleur": "success",
            "intro": "Vous êtes une référence. Votre organisme fonctionne comme une organisation apprenante. Vous ne gérez pas juste la cohabitation — vous la co-construisez.",
            "forces": """
            - Approche préventive et anticipatrice.
            - Partenariats multi-niveaux (Ville, CIUSSS, Citoyens).
            - Données probantes utilisées stratégiquement.
            - Innovations terrain (zone tampon active, co-construction).""",
            "risques": """
            - **Pérennité** : Comment maintenir l'excellence malgré les changements ?
            - **Essaimage** : Comment transférer vos pratiques sans créer de dépendance ?
            - **Fatigue de l'excellence** : Risque de burnout à force de viser la perfection.""",
            "action_titre": "Documentez vos pratiques exemplaires et partagez-les",
            "action_why": "Votre prochain levier est de multiplier votre impact en inspirant d'autres organismes. Devenez une ressource pour le réseau.",
            "action_how": "Consultez la **Conclusion** : Vers un urbanisme du lien.",
            "priorites": ["Chapitre 8 (Consolider)", "Conclusion (Inspirer)", "Mentorat (Action)"]
        }

content = get_content(total)

# --- AFFICHAGE ---

# 1. HAUT DE PAGE : MÉTRIQUES & RADAR
c1, c2 = st.columns([1, 1])

with c1:
    st.markdown("### 📊 Vos Scores")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("GLOBAL", f"{total}/48")
    m2.metric("Gouv.", f"{axe_a}/16")
    m3.metric("Terrain", f"{axe_b}/16")
    m4.metric("Alliance", f"{axe_c}/16")
    
    # Message coloré simple
    if content["couleur"] == "error": st.error(f"📍 {content['titre']}")
    elif content["couleur"] == "warning": st.warning(f"📍 {content['titre']}")
    elif content["couleur"] == "info": st.info(f"📍 {content['titre']}")
    else: st.success(f"📍 {content['titre']}")

with c2:
    # Radar Chart
    categories = ['Gouvernance', 'Opérations', 'Alliances']
    values = [axe_a, axe_b, axe_c]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values, theta=categories, fill='toself', name='Score',
        line_color='#1f77b4', fillcolor='rgba(31, 119, 180, 0.2)'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 16])),
        showlegend=False, height=250, margin=dict(l=40, r=40, t=20, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)

# 2. BAS DE PAGE : ANALYSE DÉTAILLÉE (C'est ici que tout le texte apparaît)
st.divider()

st.markdown(f"### 🔍 Analyse de votre réalité")
st.markdown(f"_{content['intro']}_")

col_f, col_r = st.columns(2)
with col_f:
    st.markdown("#### ✅ Vos Forces")
    st.markdown(content['forces'])

with col_r:
    st.markdown("#### ⚠️ Vos Risques")
    st.markdown(content['risques'])

# BOITE D'ACTION (Mise en valeur)
st.markdown(f"""
<div class="action-box">
    <h3>🎯 VOTRE ACTION PRIORITAIRE (Low Hanging Fruit)</h3>
    <p><strong>Ne tentez pas de tout refaire. Commencez par :</strong></p>
    <h2 style="color:#d9534f;">{content['action_titre']}</h2>
    <p><strong>Pourquoi ?</strong> {content['action_why']}</p>
    <p><strong>Comment ?</strong> {content['action_how']}</p>
</div>
""", unsafe_allow_html=True)

st.markdown("#### 📖 Chapitres Recommandés")
for chap in content["priorites"]:
    st.markdown(f"- 📘 {chap}")
