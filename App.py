# -*- coding: utf-8 -*-
import streamlit as st
import plotly.graph_objects as go

# 1. CONFIGURATION
st.set_page_config(page_title="Radar Cohabitation", page_icon="🎯", layout="wide")

# 2. CSS CORRECTIF (Haute Lisibilité)
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 1rem;
    }
    .metric-box {
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
    }
    /* Style spécifique pour la boite d'action - Force le texte foncé */
    .action-box {
        background-color: #e3f2fd; /* Bleu très clair */
        padding: 25px;
        border-radius: 10px;
        border: 1px solid #90caf9;
        margin-top: 20px;
        margin-bottom: 20px;
        color: #0d47a1; /* Bleu très foncé pour le texte */
    }
    .action-box h2 {
        color: #c62828 !important; /* Rouge foncé pour le titre */
        margin-top: 0;
    }
    .action-box h3 {
        color: #1565c0 !important;
        font-size: 1.2rem;
        margin-top: 15px;
    }
    .action-box p, .action-box li {
        color: #1a237e !important; /* Texte quasi noir */
        font-size: 1.05rem;
        line-height: 1.6;
    }
    /* Style pour les boîtes de profil */
    .profile-box-error { background-color: #ffebee; padding: 15px; border-radius: 8px; border-left: 5px solid #ef5350; color: #000000; }
    .profile-box-warning { background-color: #fff3e0; padding: 15px; border-radius: 8px; border-left: 5px solid #ffa726; color: #000000; }
    .profile-box-info { background-color: #e1f5fe; padding: 15px; border-radius: 8px; border-left: 5px solid #29b6f6; color: #000000; }
    .profile-box-success { background-color: #e8f5e9; padding: 15px; border-radius: 8px; border-left: 5px solid #66bb6a; color: #000000; }
    </style>
    """, unsafe_allow_html=True)

# 3. CONTENU (Base de données complète du document Word)
def get_full_content(score):
    if score <= 24:
        return {
            "profil_nom": "LE POMPIER SOLITAIRE",
            "style": "profile-box-error",
            "intro": """Vous êtes en mode survie. Votre équipe gère au jour le jour, sans protocoles formalisés. Les crises éclatent, vous réagissez, et vous recommencez le lendemain.""",
            "forces": [
                "Vous êtes sur le terrain, proche des usagers.",
                "Vous faites preuve de résilience et d'adaptation constante.",
                "Vous connaissez intimement les réalités de votre clientèle."
            ],
            "risques": [
                "**Épuisement de l'équipe** : Tout repose sur quelques personnes clés.",
                "**Incohérence** : Chaque intervenant gère à sa façon.",
                "**Vulnérabilité médiatique** : Pas de filet de sécurité en cas de crise.",
                "**Isolement** : Perçu comme « le problème » par le voisinage."
            ],
            "action": {
                "titre": "Créez votre premier protocole d'intervention écrit",
                "sous_titre": "Comportements problématiques",
                "pourquoi": """Parce que c'est le fondement de tout. Tant que vos intervenants n'ont pas un cadre clair et partagé, vous resterez en mode réactif. Ce protocole permettra de réduire l'arbitraire, d'avoir une réponse cohérente pour les citoyens et de protéger juridiquement votre organisme.""",
                "comment": """Allez lire le **Chapitre 3** du Guide. Vous y trouverez un modèle de protocole d'intervention graduée (vert-jaune-rouge) prêt à adapter.""",
                "temps": "2-3 réunions d'équipe pour co-créer + 2h de formation."
            },
            "lectures": {
                "prio1": ["**Chapitre 3** : Principes d'intervention et gestion quotidienne."],
                "prio2": ["**Chapitre 1** : Comprendre l'écosystème.", "**Chapitre 6** : Gouvernance et concertation."]
            }
        }
    elif score <= 33:
        return {
            "profil_nom": "LE GESTIONNAIRE STRUCTURÉ",
            "style": "profile-box-warning",
            "intro": """Vous avez posé des bases solides (règlements, organisation), mais l'application reste inégale et les partenariats sont informels.""",
            "forces": [
                "Vous avez des outils et des procédures de base.",
                "Votre équipe connaît les attentes minimales.",
                "Vous documentez certaines interventions."
            ],
            "risques": [
                "**Rigidité** : Protocoles appliqués de façon mécanique.",
                "**Relations tendues** : Gestion de plaintes sans lien de confiance avec le voisinage.",
                "**Silos** : Vous fonctionnez en vase clos.",
                "**Communication défensive** : Réaction subie en cas de crise."
            ],
            "action": {
                "titre": "Formalisez vos relations avec le voisinage",
                "sous_titre": "Pacte de bon voisinage",
                "pourquoi": """Vous avez la structure interne, mais il manque le pont vers l'externe. Un Pacte transforme les plaintes récurrentes en dialogue structuré et les citoyens méfiants en alliés potentiels.""",
                "comment": """Allez lire le **Chapitre 5** du Guide. Vous y trouverez un modèle complet de Pacte de bon voisinage (clause par clause) prêt à adapter.""",
                "temps": "4-6 semaines (rédaction collaborative et signature)."
            },
            "lectures": {
                "prio1": ["**Chapitre 4** : Le rôle du citoyen.", "**Chapitre 5** : Outils de structuration des relations."],
                "prio2": ["**Chapitre 7** : Communication stratégique.", "**Chapitre 6** : Gouvernance et concertation."]
            }
        }
    elif score <= 42:
        return {
            "profil_nom": "LE PARTENAIRE STRATÉGIQUE",
            "style": "profile-box-info",
            "intro": """Vous êtes dans le peloton de tête. Vous avez des protocoles solides et des partenariats actifs. Vous êtes reconnu comme un acteur de solutions.""",
            "forces": [
                "Protocoles clairs et appliqués de façon cohérente.",
                "Partenariats structurés avec la Ville et le voisinage.",
                "Capacité à gérer les crises sans panique."
            ],
            "risques": [
                "**Proactivité vs Réactivité** : Pourriez-vous anticiper davantage ?",
                "**Mesure d'impact** : Exploitez-vous vos données stratégiquement ?",
                "**Innovation** : Pourriez-vous tester de nouvelles approches (zone tampon, médiation) ?"
            ],
            "action": {
                "titre": "Structurez votre tableau de bord d'impact",
                "sous_titre": "Indicateurs et Pérennité",
                "pourquoi": """Il vous manque la capacité à DÉMONTRER votre valeur ajoutée de manière chiffrée pour obtenir du financement additionnel et influencer les décisions municipales.""",
                "comment": """Allez lire le **Chapitre 8** du Guide. Vous y trouverez un cadre pour bâtir un tableau de bord adapté à la cohabitation.""",
                "temps": "4-6 semaines (choix des indicateurs et mise en place)."
            },
            "lectures": {
                "prio1": ["**Chapitre 8** : Mesurer votre impact pour durer.", "**Chapitre 7** : Communication stratégique."],
                "prio2": ["**Chapitre 6** : Gouvernance (Optimisation).", "**Chapitre 2** : Implantation stratégique (Expansion)."]
            }
        }
    else:
        return {
            "profil_nom": "L'INNOVATEUR SYSTÉMIQUE",
            "style": "profile-box-success",
            "intro": """Vous êtes une référence. Votre organisme fonctionne comme une organisation apprenante qui co-construit la cohabitation.""",
            "forces": [
                "Approche préventive et anticipatrice.",
                "Partenariats multi-niveaux (Ville, CIUSSS, Citoyens).",
                "Innovations terrain (zone tampon active, co-construction)."
            ],
            "risques": [
                "**Pérennité** : Maintenir l'excellence malgré les changements de personnel.",
                "**Essaimage** : Transférer vos pratiques sans créer de dépendance.",
                "**Fatigue** : Risque de burnout à force de viser la perfection."
            ],
            "action": {
                "titre": "Documentez et partagez vos pratiques exemplaires",
                "sous_titre": "Transfert de connaissances",
                "pourquoi": """Votre prochain levier est de multiplier votre impact en inspirant d'autres organismes. Cela renforce votre légitimité et contribue à l'amélioration systémique.""",
                "comment": """Consultez la **Conclusion** et le **Chapitre 8**. Envisagez de publier des études de cas ou d'offrir du mentorat.""",
                "temps": "3-6 mois pour structurer une offre de transfert."
            },
            "lectures": {
                "prio1": ["**Chapitre 8** : Consolider la mesure d'impact.", "**Conclusion** : Vers un urbanisme du lien."],
                "prio2": ["**Tous les chapitres** : À relire sous l'angle du mentorat pour autrui."]
            }
        }

# --- INTERFACE UTILISATEUR ---

st.markdown("<div class='main-header'>🎯 Le Radar de Maturité</div>", unsafe_allow_html=True)
st.info("👋 Bienvenue. Répondez aux 12 questions dans le menu de gauche pour générer votre plan d'action détaillé.")

# --- SIDEBAR (Questions) ---
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

scores = {}
with st.sidebar:
    st.markdown("### 📝 Questionnaire")
    for axe, q_dict in questions_data.items():
        with st.expander(axe, expanded=False):
            for q, options in q_dict.items():
                choix = st.radio(q, options, index=0)
                scores[q] = int(choix.split(" ")[0])

# --- CALCULS ---
total = sum(scores.values())
axe_a = sum(list(scores.values())[0:4])
axe_b = sum(list(scores.values())[4:8])
axe_c = sum(list(scores.values())[8:12])

content = get_full_content(total)

# --- AFFICHAGE PRINCIPAL ---

# 1. SCORES & RADAR
c1, c2 = st.columns([1, 1])

with c1:
    st.markdown("### 📊 Vos Résultats")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("GLOBAL", f"{total}/48")
    m2.metric("Gouv.", f"{axe_a}/16")
    m3.metric("Terrain", f"{axe_b}/16")
    m4.metric("Alliance", f"{axe_c}/16")
    
    # Affichage du Profil avec style CSS personnalisé
    st.markdown(f"""
    <div class="{content['style']}">
        <h3 style="margin-top:0; color:#000;">📍 {content['profil_nom']} (Score {total})</h3>
        <p style="margin-bottom:0;">{content['intro']}</p>
    </div>
    """, unsafe_allow_html=True)

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

st.divider()

# 2. ANALYSE DÉTAILLÉE (FORCES / RISQUES)
col_f, col_r = st.columns(2)
with col_f:
    st.markdown("#### ✅ Vos Forces")
    for item in content['forces']:
        st.markdown(f"- {item}")

with col_r:
    st.markdown("#### ⚠️ Vos Risques")
    for item in content['risques']:
        st.markdown(f"- {item}")

# 3. ACTION PRIORITAIRE (ENCADRÉ HAUTE LISIBILITÉ)
act = content['action']
st.markdown(f"""
<div class="action-box">
    <h2>🎯 VOTRE ACTION PRIORITAIRE (Low Hanging Fruit)</h2>
    <h3>👉 {act['titre']} <br><small>({act['sous_titre']})</small></h3>
    <p><strong>POURQUOI ?</strong><br>{act['pourquoi']}</p>
    <p><strong>COMMENT ?</strong><br>{act['comment']}</p>
    <p><strong>⏱️ TEMPS REQUIS :</strong> {act['temps']}</p>
</div>
""", unsafe_allow_html=True)

# 4. BIBLIOTHÈQUE
st.markdown("### 📚 Chapitres Recommandés")
c_prio1, c_prio2 = st.columns(2)

with c_prio1:
    st.info("🔥 **Priorité 1 (À lire maintenant)**")
    for book in content['lectures']['prio1']:
        st.markdown(f"- {book}")

with c_prio2:
    st.success("📅 **Priorité 2 (Dans les 3-6 mois)**")
    for book in content['lectures']['prio2']:
        st.markdown(f"- {book}")
