# -*- coding: utf-8 -*-
import streamlit as st
import plotly.graph_objects as go

# 1. CONFIGURATION DE LA PAGE (Doit être la première commande)
st.set_page_config(
    page_title="Radar Cohabitation",
    page_icon="🎯",
    layout="wide"  # Utilise toute la largeur de l'écran
)

# 2. CSS PERSONNALISÉ (Pour un look plus "Pro" et moins "Streamlit")
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    h1 {
        color: #2c3e50;
    }
    .stRadio > label {
        font-weight: bold;
        background-color: #eef2f3;
        padding: 10px;
        border-radius: 5px;
        display: block;
        margin-bottom: 5px;
    }
    div[data-testid="stMetricValue"] {
        font-size: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. EN-TÊTE
st.title("🎯 Le Radar de Maturité en Cohabitation")
st.markdown("### Outil d'auto-diagnostic stratégique pour OBNL et Gestionnaires")
st.info("👋 Bienvenue. Cet outil vous permet d'évaluer vos pratiques actuelles. Sélectionnez l'énoncé qui correspond le mieux à votre réalité dans la colonne de gauche.")

# --- DÉFINITION DES DONNÉES (QUESTIONS) ---
# Structure : "Question": [Choix 1, Choix 2, Choix 3, Choix 4]
questions_data = {
    "Axe A : Gouvernance & Protocoles": {
        "Q1. Protocole de gestion des comportements": [
            "1 pt - Réactif : Au cas par cas, selon l'intervenant de garde.",
            "2 pts - Formel : Règlement affiché mais application inégale.",
            "3 pts - Collaboratif : Protocole écrit, connu et ajusté en équipe.",
            "4 pts - Systémique : Intervention graduée (vert-jaune-rouge) révisée annuellement."
        ],
        "Q2. Engagements avec le voisinage": [
            "1 pt - Réactif : On réagit seulement aux plaintes.",
            "2 pts - Formel : Rencontre à l'ouverture, rien depuis.",
            "3 pts - Collaboratif : Rencontres périodiques non formalisées.",
            "4 pts - Systémique : Pacte de bon voisinage signé et actif."
        ],
        "Q3. Rôles et responsabilités": [
            "1 pt - Réactif : Confusion, on se renvoie la balle.",
            "2 pts - Formel : Ententes signées mais zones grises sur le terrain.",
            "3 pts - Collaboratif : Rôles clairs grâce aux bonnes relations.",
            "4 pts - Systémique : Cadre de gouvernance écrit et partagé."
        ],
        "Q4. Mesure d'impact": [
            "1 pt - Réactif : Pas de données, gestion au feeling.",
            "2 pts - Formel : Données collectées mais peu analysées.",
            "3 pts - Collaboratif : Indicateurs de base suivis en équipe.",
            "4 pts - Systémique : Tableau de bord complet partagé aux bailleurs."
        ]
    },
    "Axe B : Opérations & Terrain": {
        "Q5. Gestion des crises médiatiques": [
            "1 pt - Réactif : On subit, silence radio.",
            "2 pts - Formel : Réaction tardive, communiqué générique.",
            "3 pts - Collaboratif : Porte-parole identifié, réponse rapide.",
            "4 pts - Systémique : Plan de comm. de crise et stratégie proactive."
        ],
        "Q6. Formation des intervenants": [
            "1 pt - Réactif : Pas de formation spécifique cohabitation.",
            "2 pts - Formel : Formation ponctuelle à l'embauche.",
            "3 pts - Collaboratif : Formations régulières et débriefs.",
            "4 pts - Systémique : Cursus structuré (CPTED, CNV) et supervision."
        ],
        "Q7. Intervention hors murs (Zone tampon)": [
            "1 pt - Réactif : On ne sort pas.",
            "2 pts - Formel : Sorties ponctuelles sur plainte.",
            "3 pts - Collaboratif : Rondes régulières (10-20m).",
            "4 pts - Systémique : Gestion active de la zone tampon (50-100m)."
        ],
        "Q8. Gestion des exclusions": [
            "1 pt - Réactif : Arbitraire, pas de procédure.",
            "2 pts - Formel : Variable selon la gravité.",
            "3 pts - Collaboratif : Grille claire, retour avec rencontre.",
            "4 pts - Systémique : Protocole gradué et suivi documenté."
        ]
    },
    "Axe C : Alliances & Partenariats": {
        "Q9. Relation services municipaux": [
            "1 pt - Réactif : Peu de contact, relations tendues.",
            "2 pts - Formel : Courriels administratifs, pas de terrain.",
            "3 pts - Collaboratif : Contacts réguliers et constructifs.",
            "4 pts - Systémique : Table de concertation et solutions communes."
        ],
        "Q10. Collaboration organismes du secteur": [
            "1 pt - Réactif : Silos, compétition.",
            "2 pts - Formel : Echanges occasionnels.",
            "3 pts - Collaboratif : Concertation sur cas complexes.",
            "4 pts - Systémique : Réseau structuré, stratégies communes."
        ],
        "Q11. Implication citoyenne": [
            "1 pt - Réactif : Évitement, on subit les reproches.",
            "2 pts - Formel : Réponses polies aux plaintes.",
            "3 pts - Collaboratif : Rencontres 2-3 fois par an.",
            "4 pts - Systémique : Comité de bon voisinage co-créé."
        ],
        "Q12. Médiation sociale dédiée": [
            "1 pt - Réactif : Intervenants débordés font tout.",
            "2 pts - Formel : On aimerait, mais pas de budget.",
            "3 pts - Collaboratif : Médiateur externe ponctuel.",
            "4 pts - Systémique : Poste dédié financé (Agent de milieu)."
        ]
    }
}

# --- INTERFACE UTILISATEUR (COLONNES) ---
# On utilise une Sidebar pour les questions pour laisser la place aux résultats
scores = {}

with st.sidebar:
    st.header("📝 Votre Diagnostic")
    st.markdown("---")
    
    # On boucle sur les axes et les questions
    for axe, q_dict in questions_data.items():
        with st.expander(axe, expanded=True): # Utilise des menus déroulants pour être plus propre
            for q, options in q_dict.items():
                choix = st.radio(q, options, index=0)
                # Extraction du score (le premier caractère est le chiffre)
                scores[q] = int(choix.split(" ")[0])

# --- CALCULS ---
total_score = sum(scores.values())
axe_a_score = sum(list(scores.values())[0:4])
axe_b_score = sum(list(scores.values())[4:8])
axe_c_score = sum(list(scores.values())[8:12])

# --- AFFICHAGE DES RÉSULTATS (MAIN PAGE) ---

col_gauche, col_droite = st.columns([1, 1])

with col_gauche:
    st.markdown("### 📊 Vos Résultats")
    
    # Affichage des métriques
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("GLOBAL", f"{total_score}/48")
    c2.metric("A. Gouvernance", f"{axe_a_score}/16")
    c3.metric("B. Terrain", f"{axe_b_score}/16")
    c4.metric("C. Alliances", f"{axe_c_score}/16")

    # Logique du Profil
    if total_score <= 24:
        profil = "Le Pompier Solitaire"
        msg_couleur = "error" # Rouge
        desc = "Vous êtes en mode survie. Votre équipe gère au jour le jour."
        action = "Créer un protocole d'intervention écrit."
        chapitre = "Chapitre 3"
    elif total_score <= 33:
        profil = "Le Gestionnaire Structuré"
        msg_couleur = "warning" # Orange
        desc = "Vous avez des bases, mais l'application est inégale."
        action = "Formaliser un Pacte de bon voisinage."
        chapitre = "Chapitre 5"
    elif total_score <= 42:
        profil = "Le Partenaire Stratégique"
        msg_couleur = "info" # Bleu
        desc = "Vous avez des protocoles solides et de bons partenariats."
        action = "Structurer le tableau de bord d'impact."
        chapitre = "Chapitre 8"
    else:
        profil = "L'Innovateur Systémique"
        msg_couleur = "success" # Vert
        desc = "Vous êtes une référence et co-construisez la cohabitation."
        action = "Documenter et partager vos pratiques."
        chapitre = "Conclusion"

    # Affichage Profil
    if msg_couleur == "error":
        st.error(f"📍 Votre Profil : **{profil}**")
    elif msg_couleur == "warning":
        st.warning(f"📍 Votre Profil : **{profil}**")
    elif msg_couleur == "info":
        st.info(f"📍 Votre Profil : **{profil}**")
    else:
        st.success(f"📍 Votre Profil : **{profil}**")

    st.markdown(f"_{desc}_")
    
    st.divider()
    st.markdown(f"#### 🚀 Action Prioritaire :")
    st.markdown(f"**{action}**")
    st.markdown(f"👉 *Pour savoir comment faire, consultez le **{chapitre}** du Guide.*")

with col_droite:
    st.markdown("### 🕸️ Radar de Maturité")
    
    # Graphique Radar amélioré
    categories = ['Gouvernance', 'Opérations', 'Alliances']
    values = [axe_a_score, axe_b_score, axe_c_score]
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Organisation',
        line_color='#1f77b4',
        fillcolor='rgba(31, 119, 180, 0.3)'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 16], # Échelle fixe pour bien voir la progression
                tickfont=dict(size=10)
            ),
        ),
        showlegend=False,
        margin=dict(l=50, r=50, t=30, b=30), # Marges ajustées pour éviter que ça coupe
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Footer discret
st.markdown("---")
st.caption("Outil généré pour le *Guide de la Cohabitation Sociale*.")
