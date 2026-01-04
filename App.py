# -*- coding: utf-8 -*-
import streamlit as st
import plotly.graph_objects as go

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Radar Cohabitation", page_icon="🎯", layout="wide")

# 2. CSS PERSONNALISÉ
st.markdown("""
    <style>
    .main-header { font-size: 2.2rem; color: #2c3e50; font-weight: 700; margin-bottom: 0.5rem; }
    .sub-header { font-size: 1.2rem; color: #555; margin-bottom: 2rem; }
    .result-box { padding: 20px; border-radius: 10px; margin-bottom: 20px; border: 1px solid #ddd; }
    .profile-header { font-size: 1.5rem; font-weight: bold; margin-bottom: 10px; }
    .p-red { background-color: #ffebee; border-left: 8px solid #ef5350; color: #000; }
    .p-orange { background-color: #fff3e0; border-left: 8px solid #ffa726; color: #000; }
    .p-blue { background-color: #e3f2fd; border-left: 8px solid #29b6f6; color: #000; }
    .p-green { background-color: #e8f5e9; border-left: 8px solid #66bb6a; color: #000; }
    .action-box { background-color: #f4f6f9; padding: 25px; border-radius: 8px; border: 2px solid #34495e; margin-top: 25px; }
    .action-title { color: #c0392b; font-size: 1.4rem; font-weight: bold; }
    p, li { line-height: 1.6; font-size: 1.05rem; }
    </style>
""", unsafe_allow_html=True)

# 3. EN-TÊTE
st.markdown("<div class='main-header'>LE RADAR DE MATURITÉ EN COHABITATION</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Outil d'auto-diagnostic stratégique — 5 minutes pour savoir par où commencer</div>", unsafe_allow_html=True)

with st.expander("📖 MODE D'EMPLOI & CONSIGNES (À LIRE AVANT DE COMMENCER)", expanded=True):
    st.markdown("""
    **Cet outil n'est pas un examen. C'est une boussole.**
    Vous gérez un organisme, une ressource d'hébergement ou un service municipal ? Ce diagnostic vous aide à identifier votre prochain levier d'amélioration.

    * **Temps requis :** 5 minutes
    * **Format :** 12 questions
    * **Résultat :** Votre profil + actions prioritaires

    ---
    **CONSIGNE :** Choisissez la réponse qui reflète **votre réalité actuelle** (pas ce que vous aimeriez avoir).
    """)

# 4. FONCTION DE CONTENU (BASE DE DONNÉES TEXTE)
def get_profile_content(score):
    if score <= 24:
        return {
            "nom": "PROFIL 1 : LE POMPIER SOLITAIRE",
            "score_range": "Score : 12 à 24 points",
            "style": "p-red",
            "realite": """**Vous êtes en mode survie.** Votre équipe gère au jour le jour, sans protocoles formalisés. Les crises éclatent, vous réagissez, et vous recommencez le lendemain.""",
            "forces": """
            * Vous êtes sur le terrain, proche des usagers
            * Vous faites preuve de résilience et d'adaptation constante
            * Vous connaissez intimement les réalités de votre clientèle
            """,
            "risques": """
            * **Épuisement de l'équipe** : Tout repose sur quelques personnes clés.
            * **Incohérence** : Chaque intervenant gère à sa façon.
            * **Vulnérabilité médiatique** : Pas de filet de sécurité en cas de crise.
            * **Isolement** : Perçu comme « le problème » par le voisinage.
            """,
            "action_titre": "→ Créez votre premier protocole d'intervention écrit (comportements qui dérangent).",
            "action_details": """
            **Pourquoi ?** Parce que c'est le fondement de tout. Tant que vos intervenants n'ont pas un cadre clair, vous resterez en mode réactif.
            **Comment ?** Allez lire le **Chapitre 3** du Guide : *Principes d'intervention et gestion quotidienne*.
            **Temps requis :** 2-3 réunions d'équipe + 2h de formation.
            """,
            "chapitres": """
            **Priorité 1 :** Chapitre 3 (Principes d'intervention)
            **Priorité 2 :** Chapitre 1 (Écosystème) et Chapitre 6 (Gouvernance)
            """
        }
    elif score <= 33:
        return {
            "nom": "PROFIL 2 : LE GESTIONNAIRE STRUCTURÉ",
            "score_range": "Score : 25 à 33 points",
            "style": "p-orange",
            "realite": """**Vous avez posé des bases solides.** Vous avez des règles claires, mais l'application reste inégale et les partenariats sont informels.""",
            "forces": """
            * Vous avez des outils et procédures de base
            * Votre équipe connaît les attentes minimales
            * Vous documentez certaines interventions
            """,
            "risques": """
            * **Rigidité** : Protocoles appliqués de façon mécanique.
            * **Relations tendues** : Gestion de plaintes sans lien de confiance.
            * **Silos** : Fonctionnement en vase clos.
            * **Communication défensive** : Réaction subie en cas de crise.
            """,
            "action_titre": "→ Formalisez vos relations avec le voisinage (Pacte de bon voisinage).",
            "action_details": """
            **Pourquoi ?** Il vous manque le pont vers l'externe. Un Pacte transforme les plaintes en dialogue structuré.
            **Comment ?** Allez lire le **Chapitre 4** du Guide : *Le rôle des citoyen.ne.s*.
            **Temps requis :** 4-6 semaines.
            """,
            "chapitres": """
            **Priorité 1 :** Chapitre 4 (Voisinage) et Chapitre 5 (Outils)
            **Priorité 2 :** Chapitre 7 (Comms) et Chapitre 6 (Gouvernance)
            """
        }
    elif score <= 42:
        return {
            "nom": "PROFIL 3 : LE PARTENAIRE STRATÉGIQUE",
            "score_range": "Score : 34 à 42 points",
            "style": "p-blue",
            "realite": """**Vous êtes dans le peloton de tête.** Protocoles solides, partenariats actifs. Vous êtes reconnu comme un acteur de solutions.""",
            "forces": """
            * Protocoles clairs et cohérents
            * Partenariats structurés avec la Ville
            * Capacité à gérer les crises sans panique
            """,
            "risques": """
            * **Proactivité vs Réactivité** : Pourriez-vous anticiper davantage ?
            * **Mesure d'impact** : Exploitez-vous vos données stratégiquement ?
            * **Innovation** : Pourriez-vous tester la médiation sociale dédiée ?
            """,
            "action_titre": "→ Structurez votre tableau de bord d'impact.",
            "action_details": """
            **Pourquoi ?** Pour démontrer votre valeur ajoutée de manière chiffrée et influencer les décisions.
            **Comment ?** Allez lire le **Chapitre 8** du Guide : *Mesurer votre impact*.
            **Temps requis :** 4-6 semaines.
            """,
            "chapitres": """
            **Priorité 1 :** Chapitre 8 (Impact) et Chapitre 7 (Comms)
            **Priorité 2 :** Chapitre 6 (Gouvernance) et Chapitre 2 (Implantation)
            """
        }
    else:
        return {
            "nom": "PROFIL 4 : L'INNOVATEUR SYSTÉMIQUE",
            "score_range": "Score : 43 à 48 points",
            "style": "p-green",
            "realite": """**Vous êtes une référence.** Organisation apprenante qui co-construit la cohabitation.""",
            "forces": """
            * Approche préventive et anticipatrice
            * Partenariats multi-niveaux
            * Innovations terrain (zone tampon, médiation)
            """,
            "risques": """
            * **Pérennité** : Maintenir l'excellence malgré les changements.
            * **Essaimage** : Transférer sans créer de dépendance.
            * **Fatigue** : Risque de burnout de l'équipe.
            """,
            "action_titre": "→ Documentez et partagez vos pratiques exemplaires.",
            "action_details": """
            **Pourquoi ?** Votre levier est de multiplier votre impact en inspirant d'autres organismes.
            **Comment ?** Consultez la **Conclusion** et le **Chapitre 8**.
            **Temps requis :** 3-6 mois (transfert de connaissances).
            """,
            "chapitres": """
            **Priorité 1 :** Chapitre 8 et Conclusion
            **Priorité 2 :** Tous les chapitres (en mode mentorat)
            """
        }

# 5. SIDEBAR : LE QUESTIONNAIRE
scores = {}

with st.sidebar:
    st.header("QUESTIONNAIRE")
    st.info("Répondez aux 12 questions ci-dessous.")
    
    st.markdown("### AXE A : GOUVERNANCE")
    
    q1 = st.radio("Q1. Protocole de gestion des comportements ?", 
        ["A. (1 pt) — Réactif : Non, cas par cas.", 
         "B. (2 pts) — Formel : Règlement affiché mais application inégale.", 
         "C. (3 pts) — Collaboratif : Protocole écrit connu de l'équipe.", 
         "D. (4 pts) — Systémique : Protocole gradué (vert-jaune-rouge) documenté."])
    # CORRECTION ICI : On prend le caractère à l'index 0 après la parenthèse ouvrante
    scores["Q1"] = int(q1.split("(")[1][0])

    q2 = st.radio("Q2. Engagements avec le voisinage ?", 
        ["A. (1 pt) — Réactif : Non, réaction aux plaintes seulement.", 
         "B. (2 pts) — Formel : Rencontre à l'ouverture, rien depuis.", 
         "C. (3 pts) — Collaboratif : Rencontres périodiques (comité de citoyens).", 
         "D. (4 pts) — Systémique : Pacte de bon voisinage signé et actif."])
    scores["Q2"] = int(q2.split("(")[1][0])

    q3 = st.radio("Q3. Rôles et responsabilités (Ville/Partenaires) ?", 
        ["A. (1 pt) — Réactif : Confusion, on se renvoie la balle.", 
         "B. (2 pts) — Formel : Ententes signées mais zones grises terrain.", 
         "C. (3 pts) — Collaboratif : Rôles clairs, ajustements réguliers.", 
         "D. (4 pts) — Systémique : Cadre de gouvernance écrit et partagé."])
    scores["Q3"] = int(q3.split("(")[1][0])

    q4 = st.radio("Q4. Mesure d'impact ?", 
        ["A. (1 pt) — Réactif : Pas de données, gestion au feeling.", 
         "B. (2 pts) — Formel : Données collectées mais peu analysées.", 
         "C. (3 pts) — Collaboratif : Indicateurs de base suivis en équipe.", 
         "D. (4 pts) — Systémique : Tableau de bord complet partagé."])
    scores["Q4"] = int(q4.split("(")[1][0])

    st.markdown("---")
    st.markdown("### AXE B : OPÉRATIONS")

    q5 = st.radio("Q5. Gestion des crises médiatiques ?", 
        ["A. (1 pt) — Réactif : On subit, silence radio.", 
         "B. (2 pts) — Formel : Réaction tardive, communiqué générique.", 
         "C. (3 pts) — Collaboratif : Porte-parole identifié, réponse rapide.", 
         "D. (4 pts) — Systémique : Plan de comm. de crise proactif."])
    scores["Q5"] = int(q5.split("(")[1][0])

    q6 = st.radio("Q6. Formation des intervenants ?", 
        ["A. (1 pt) — Réactif : Pas de formation spécifique cohabitation.", 
         "B. (2 pts) — Formel : Formation ponctuelle à l'embauche.", 
         "C. (3 pts) — Collaboratif : Formations régulières et débriefs.", 
         "D. (4 pts) — Systémique : Cursus structuré (CPTED, CNV) annuel."])
    scores["Q6"] = int(q6.split("(")[1][0])

    q7 = st.radio("Q7. Intervention hors murs (Zone tampon) ?", 
        ["A. (1 pt) — Réactif : On ne sort pas.", 
         "B. (2 pts) — Formel : Sorties ponctuelles sur plainte.", 
         "C. (3 pts) — Collaboratif : Rondes régulières (10-20m).", 
         "D. (4 pts) — Systémique : Gestion active zone tampon (50-100m)."])
    scores["Q7"] = int(q7.split("(")[1][0])

    q8 = st.radio("Q8. Gestion des exclusions ?", 
        ["A. (1 pt) — Réactif : Arbitraire, pas de procédure.", 
         "B. (2 pts) — Formel : Variable, parfois sans rencontre.", 
         "C. (3 pts) — Collaboratif : Grille claire, retour avec rencontre.", 
         "D. (4 pts) — Systémique : Protocole gradué et suivi documenté."])
    scores["Q8"] = int(q8.split("(")[1][0])

    st.markdown("---")
    st.markdown("### AXE C : ALLIANCES")

    q9 = st.radio("Q9. Relation services municipaux ?", 
        ["A. (1 pt) — Réactif : Peu de contact, relations tendues.", 
         "B. (2 pts) — Formel : Courriels administratifs seulement.", 
         "C. (3 pts) — Collaboratif : Contacts réguliers et constructifs.", 
         "D. (4 pts) — Systémique : Table de concertation, solutions communes."])
    scores["Q9"] = int(q9.split("(")[1][0])

    q10 = st.radio("Q10. Collaboration organismes du secteur ?", 
        ["A. (1 pt) — Réactif : Silos, compétition.", 
         "B. (2 pts) — Formel : Echanges occasionnels.", 
         "C. (3 pts) — Collaboratif : Concertation sur cas complexes.", 
         "D. (4 pts) — Systémique : Réseau structuré, stratégies communes."])
    scores["Q10"] = int(q10.split("(")[1][0])

    q11 = st.radio("Q11. Implication citoyenne ?", 
        ["A. (1 pt) — Réactif : Évitement, on subit les reproches.", 
         "B. (2 pts) — Formel : Réponses polies aux plaintes.", 
         "C. (3 pts) — Collaboratif : Rencontres 2-3 fois par an.", 
         "D. (4 pts) — Systémique : Comité de bon voisinage co-créé."])
    scores["Q11"] = int(q11.split("(")[1][0])

    q12 = st.radio("Q12. Médiation sociale dédiée ?", 
        ["A. (1 pt) — Réactif : Intervenants débordés font tout.", 
         "B. (2 pts) — Formel : Pas de budget, débrouillardise.", 
         "C. (3 pts) — Collaboratif : Médiateur externe ponctuel.", 
         "D. (4 pts) — Systémique : Poste dédié financé (agent de milieu)."])
    scores["Q12"] = int(q12.split("(")[1][0])

# 6. CALCULS
total = sum(scores.values())
axe_a = scores["Q1"] + scores["Q2"] + scores["Q3"] + scores["Q4"]
axe_b = scores["Q5"] + scores["Q6"] + scores["Q7"] + scores["Q8"]
axe_c = scores["Q9"] + scores["Q10"] + scores["Q11"] + scores["Q12"]

content = get_profile_content(total)

# 7. AFFICHAGE RÉSULTATS
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📊 VOS RÉSULTATS")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("TOTAL", f"{total}/48")
    m2.metric("A. Gouv.", f"{axe_a}/16")
    m3.metric("B. Terrain", f"{axe_b}/16")
    m4.metric("C. Alliance", f"{axe_c}/16")
    
    st.markdown(f"""
    <div class="result-box {content['style']}">
        <div class="profile-header">{content['nom']}</div>
        <div style="font-weight:bold; margin-bottom:15px;">{content['score_range']}</div>
        <div><strong>🔍 VOTRE RÉALITÉ ACTUELLE</strong></div>
        {content['realite']}
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### 🕸️ RADAR")
    categories = ['Gouvernance', 'Opérations', 'Alliances']
    values = [axe_a, axe_b, axe_c]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values, theta=categories, fill='toself', name='Score',
        line_color='#34495e', fillcolor='rgba(52, 73, 94, 0.2)'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 16])),
        showlegend=False, height=300, margin=dict(l=40, r=40, t=20, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
c_forces, c_risques = st.columns(2)
with c_forces:
    st.markdown("#### ✅ VOS FORCES")
    st.markdown(content['forces'])
with c_risques:
    st.markdown("#### ⚠️ VOS RISQUES")
    st.markdown(content['risques'])

st.markdown(f"""
<div class="action-box">
    <div class="action-title">🎯 VOTRE ACTION PRIORITAIRE (Low Hanging Fruit)</div>
    <div style="margin-top:10px;"><em>Ne tentez pas de tout refaire. Commencez par :</em></div>
    <h2 style="color:#c0392b; margin-top:5px;">{content['action_titre']}</h2>
    {content['action_details']}
</div>
""", unsafe_allow_html=True)

st.markdown("### 📖 CHAPITRES RECOMMANDÉS")
st.markdown(content['chapitres'])
st.markdown("---")
st.caption("Outil généré pour le Guide de la Cohabitation Sociale.")
