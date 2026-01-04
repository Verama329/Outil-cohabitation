# -*- coding: utf-8 -*-
import streamlit as st
import plotly.graph_objects as go

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Radar Cohabitation", page_icon="🎯", layout="wide")

# 2. CSS PERSONNALISÉ (DESIGN PROFESSIONNEL)
st.markdown("""
    <style>
    /* TYPOGRAPHIE GLOBALE */
    h1, h2, h3 { font-family: 'Helvetica Neue', sans-serif; color: #2c3e50; }
    p, li { font-size: 1.1rem; line-height: 1.6; color: #444; }
    
    /* EN-TÊTE */
    .main-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .main-header h1 { color: white; margin: 0; font-size: 2.5rem; }
    .main-header p { color: #e0e0e0; font-size: 1.2rem; margin-top: 10px; }

    /* BOITES DE RÉSULTATS (PROFILS) */
    .profile-card {
        padding: 25px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 10px solid #ccc; /* Sera remplacé par la couleur dynamique */
    }
    .profile-title { font-size: 1.8rem; font-weight: bold; margin-bottom: 5px; color: #333; }
    .profile-score { font-size: 1.2rem; font-weight: bold; color: #666; margin-bottom: 20px; }
    
    /* COULEURS DES PROFILS */
    .border-red { border-left-color: #e74c3c !important; }
    .border-orange { border-left-color: #f39c12 !important; }
    .border-blue { border-left-color: #3498db !important; }
    .border-green { border-left-color: #27ae60 !important; }

    /* BOITE ACTION PRIORITAIRE (DESIGN SPÉCIAL) */
    .action-box {
        background-color: #f8f9fa;
        border: 2px solid #2c3e50;
        border-radius: 12px;
        padding: 30px;
        margin-top: 30px;
        position: relative;
    }
    .action-badge {
        background-color: #c0392b;
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.9rem;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 15px;
    }
    .action-main-title {
        color: #c0392b;
        font-size: 1.6rem;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .action-subtitle {
        font-weight: bold;
        color: #2c3e50;
        margin-top: 15px;
        display: block;
    }

    /* CHAPITRES RECOMMANDÉS */
    .chapter-box {
        background-color: #e8f6f3;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1abc9c;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. EN-TÊTE DE L'APPLICATION
st.markdown("""
<div class="main-header">
    <h1>LE RADAR DE MATURITÉ EN COHABITATION</h1>
    <p>Outil d'auto-diagnostic stratégique — 5 minutes pour savoir par où commencer</p>
</div>
""", unsafe_allow_html=True)

# 4. MODE D'EMPLOI
with st.expander("📖 MODE D'EMPLOI & CONSIGNES (CLIQUEZ POUR LIRE)", expanded=True):
    st.markdown("""
    **Cet outil n'est pas un examen. C'est une boussole.**
    
    Vous gérez un organisme, une ressource d'hébergement, une équipe d'intervention de proximité ou un service municipal en contact avec l'itinérance ? Vous faites déjà beaucoup avec peu. Ce diagnostic vous aide simplement à identifier votre prochain levier d'amélioration — celui qui aura le plus d'impact avec le moins d'effort.

    * **Temps requis :** 5 minutes
    * **Format :** 12 questions, 4 choix de réponse par question
    * **Résultat :** Votre profil de maturité + vos actions prioritaires

    ---
    **CONSIGNE :** Pour chaque question, choisissez **la réponse qui reflète le mieux votre réalité actuelle** (pas ce que vous aimeriez avoir, mais ce qui existe vraiment aujourd'hui).
    """)

# 5. BASE DE DONNÉES DU CONTENU (TEXTE EXACT DU WORD)
def get_profile_data(score):
    if score <= 24:
        return {
            "nom": "PROFIL 1 : LE POMPIER SOLITAIRE",
            "score_txt": "Score : 12 à 24 points",
            "css_class": "border-red",
            "intro": "Vous êtes en mode survie. Votre équipe gère au jour le jour, sans protocoles formalisés, avec peu ou pas de collaboration structurée avec le voisinage ou les partenaires externes. Les crises éclatent, vous réagissez, et vous recommencez le lendemain.",
            "forces": [
                "Vous êtes sur le terrain, proche des personnes qui se prévalent des services",
                "Vous faites preuve de résilience et d'adaptation constante",
                "Vous connaissez intimement les réalités de votre clientèle"
            ],
            "risques": [
                "**Épuisement de l'équipe** : Tout repose sur quelques personnes clés. Le taux de roulement est élevé.",
                "**Incohérence** : Chaque intervenant.e gère les situations à sa façon. Pas de prévisibilité.",
                "**Vulnérabilité médiatique** : Une vidéo virale, un article négatif, et vous n'avez aucun filet de sécurité.",
                "**Isolement** : Vous êtes perçu comme « le problème » par le voisinage et la Ville, plutôt que comme un partenaire."
            ],
            "action_titre": "Créez votre premier protocole d'intervention écrit (Gestion des comportements qui dérangent).",
            "action_why": "Parce que c'est le fondement de tout. Tant que vos équipes d’intervention n'ont pas un cadre clair et partagé, vous resterez en mode réactif. Ce protocole vous permettra de réduire la gestion arbitraire, d'avoir une réponse cohérente et de protéger juridiquement votre organisme.",
            "action_how": "Allez lire le **Chapitre 3** de ce Guide : *Principes d'intervention et gestion quotidienne de la cohabitation sociale*. Vous y trouverez un modèle de protocole de gestion des comportements qui dérangent (vert-jaune-rouge) prêt à adapter.",
            "action_time": "Deux (2) à trois (3) réunions d'équipe pour co-créer le protocole, puis formation de deux (2) heures pour l'implanter.",
            "chap_prio1": "<strong>Chapitre 3</strong> : Principes d'intervention et gestion quotidienne",
            "chap_prio2": "<strong>Chapitre 1</strong> (Écosystème) et <strong>Chapitre 6</strong> (Gouvernance)"
        }
    elif score <= 33:
        return {
            "nom": "PROFIL 2 : LE GESTIONNAIRE STRUCTURÉ",
            "score_txt": "Score : 25 à 33 points",
            "css_class": "border-orange",
            "intro": "Vous avez posé des bases solides. Vous avez des protocoles écrits, des règles claires, et une certaine organisation interne. Cependant, l'application reste inégale, les partenariats sont informels, et vous sentez que votre approche pourrait être plus fluide et collaborative.",
            "forces": [
                "Vous avez des outils et des procédures (règlements, protocoles de base)",
                "Votre équipe connaît les attentes minimales",
                "Vous documentez certaines de vos interventions"
            ],
            "risques": [
                "**Rigidité** : Vos protocoles existent, mais ils sont appliqués de façon mécanique. Peu de place pour l'adaptation.",
                "**Relations tendues avec le voisinage** : Vous gérez les plaintes, mais vous n'avez pas vraiment construit de lien de confiance.",
                "**Silos** : Vous fonctionnez en vase clos. Les partenariats sont limités ou ponctuels.",
                "**Communication défensive** : En cas de crise médiatique, vous réagissez, mais vous ne maîtrisez pas le narratif."
            ],
            "action_titre": "Formalisez vos relations avec le voisinage (créez, entre autres, votre premier Pacte de bon voisinage).",
            "action_why": "Parce que vous avez déjà la structure interne. Ce qui vous manque, c'est le pont vers l'externe. Un Pacte de bon voisinage transforme les plaintes récurrentes en dialogue structuré, et les citoyens méfiants en alliés potentiels.",
            "action_how": "Allez lire le **Chapitre 4** de ce Guide : *Le rôle des citoyen.ne.s et du voisinage*. Vous y trouverez un modèle complet de Pacte de bon voisinage (clause par clause) prêt à adapter.",
            "action_time": "Quatre (4) à six (6) semaines (identification, rédaction collaborative, signature).",
            "chap_prio1": "<strong>Chapitre 4</strong> (Rôle des citoyens) et <strong>Chapitre 5</strong> (Outils)",
            "chap_prio2": "<strong>Chapitre 7</strong> (Communication) et <strong>Chapitre 6</strong> (Gouvernance)"
        }
    elif score <= 42:
        return {
            "nom": "PROFIL 3 : LE PARTENAIRE STRATÉGIQUE",
            "score_txt": "Score : 34 à 42 points",
            "css_class": "border-blue",
            "intro": "Vous êtes dans le peloton de tête. Vous avez des protocoles solides, des partenariats actifs, et une relation constructive avec le voisinage. Votre organisme est reconnu comme un acteur de solutions. Cependant, vous sentez qu'il reste des angles morts, et vous voulez optimiser.",
            "forces": [
                "Protocoles clairs et appliqués de façon cohérente",
                "Partenariats structurés avec la Ville, les organismes pairs, et le voisinage",
                "Capacité à gérer les crises sans panique",
                "Certaines mesures d'impact documentées"
            ],
            "risques": [
                "**Proactivité vs Réactivité** : Vous gérez bien les crises, mais pourriez-vous les anticiper davantage ?",
                "**Mesure d'impact** : Vous collectez des données, mais les exploitez-vous stratégiquement pour le financement ?",
                "**Innovation** : Pourriez-vous tester de nouvelles approches (médiation sociale dédiée, zone tampon élargie) ?"
            ],
            "action_titre": "Structurez votre tableau de bord d'impact et utilisez-le comme levier stratégique.",
            "action_why": "Il vous manque la capacité à démontrer votre valeur ajoutée de manière chiffrée pour obtenir du financement additionnel, influencer les décisions municipales et protéger votre réputation.",
            "action_how": "Allez lire le **Chapitre 8** de ce Guide : *Mesurer votre impact pour durer*. Vous y trouverez un cadre complet pour bâtir un tableau de bord.",
            "action_time": "Quatre (4) à six (6) semaines (choix indicateurs, collecte, premier rapport).",
            "chap_prio1": "<strong>Chapitre 8</strong> (Mesure d'impact) et <strong>Chapitre 7</strong> (Communication)",
            "chap_prio2": "<strong>Chapitre 6</strong> (Gouvernance) et <strong>Chapitre 2</strong> (Implantation stratégique)"
        }
    else:
        return {
            "nom": "PROFIL 4 : L'INNOVATEUR SYSTÉMIQUE",
            "score_txt": "Score : 43 à 48 points",
            "css_class": "border-green",
            "intro": "Vous êtes une référence. Votre organisme fonctionne comme une organisation apprenante : protocoles solides, partenariats stratégiques, mesure d'impact rigoureuse. Vous ne gérez pas juste la cohabitation — vous la co-construisez.",
            "forces": [
                "Approche préventive et proactive (gestion des risques)",
                "Partenariats intersectoriels (Ville, CIUSSS, citoyens)",
                "Innovations terrain (médiation sociale, zone tampon)",
                "Influence sur les politiques publiques locales"
            ],
            "risques": [
                "**Pérennité** : Maintenir l'excellence malgré les changements de personnel/financement.",
                "**Essaimage** : Transférer vos pratiques sans créer de dépendance.",
                "**Fatigue de l'excellence** : Risque d’épuisement ou fatigue de compassion de l'équipe."
            ],
            "action_titre": "Documentez vos pratiques exemplaires et partagez-les (devenez une ressource pour le réseau).",
            "action_why": "Votre prochain levier est de multiplier votre impact en inspirant d'autres organismes. Cela renforcera votre légitimité et contribuera à l'amélioration systémique du secteur.",
            "action_how": "Consultez la **Conclusion** et le **Chapitre 8**. Envisagez de publier des études de cas, d'offrir du mentorat ou de co-animer des formations.",
            "action_time": "Trois (3) à six (6) mois pour structurer une offre de transfert de connaissances.",
            "chap_prio1": "<strong>Chapitre 8</strong> (Mesure d'impact) et <strong>Conclusion</strong>",
            "chap_prio2": "<strong>Tous les chapitres</strong> (Lecture en mode mentorat)"
        }

# 6. SIDEBAR : LE QUESTIONNAIRE (LOGIQUE DE CALCUL SANS ERREUR)
# On utilise une liste simple. L'index 0 vaut 1pt, l'index 1 vaut 2pts, etc.

st.sidebar.header("QUESTIONNAIRE")
st.sidebar.info("Veuillez répondre aux 12 questions.")

# -- AXE A --
st.sidebar.markdown("### AXE A : GOUVERNANCE")

opt_q1 = [
    "A. (1 pt) — Réactif : Non, on gère au cas par cas selon l'intervenant.e en poste. Chacun a sa méthode.",
    "B. (2 pts) — Formel : Oui, on a un code de vie interne affiché, mais il est rarement appliqué de façon constante.",
    "C. (3 pts) — Collaboratif : Oui, on a un protocole écrit et l'équipe le connaît. Ajustements réguliers.",
    "D. (4 pts) — Systémique : Oui, protocole documenté (vert-jaune-rouge), appliqué et révisé annuellement."
]
q1_sel = st.sidebar.radio("Q1. Protocole de gestion des comportements qui dérangent ?", opt_q1)
s1 = opt_q1.index(q1_sel) + 1  # Calcul automatique : Index 0 devient 1 point

opt_q2 = [
    "A. (1 pt) — Réactif : Non, on réagit seulement quand il y a une plainte.",
    "B. (2 pts) — Formel : Rencontre à l'ouverture, rien depuis. Les citoyens appellent la Ville.",
    "C. (3 pts) — Collaboratif : Rencontres périodiques (2-4 fois/an) avec un comité, mais non formalisé.",
    "D. (4 pts) — Systémique : Pacte de bon voisinage signé, rencontres trimestrielles et résolution de conflits."
]
q2_sel = st.sidebar.radio("Q2. Engagements avec le voisinage ?", opt_q2)
s2 = opt_q2.index(q2_sel) + 1

opt_q3 = [
    "A. (1 pt) — Réactif : Non, on ne sait pas toujours qui doit faire quoi. Confusion.",
    "B. (2 pts) — Formel : Ententes signées, mais zones grises sur le terrain.",
    "C. (3 pts) — Collaboratif : Rôles relativement clairs, ajustements réguliers.",
    "D. (4 pts) — Systémique : Cadre de gouvernance écrit (qui fait quoi/finance quoi) et coordination active."
]
q3_sel = st.sidebar.radio("Q3. Rôles et responsabilités (Ville/Partenaires) ?", opt_q3)
s3 = opt_q3.index(q3_sel) + 1

opt_q4 = [
    "A. (1 pt) — Réactif : Non, pas de temps. On se fie au « feeling ».",
    "B. (2 pts) — Formel : Collecte de quelques données, mais peu d'analyse.",
    "C. (3 pts) — Collaboratif : Indicateurs de base suivis et présentés en équipe.",
    "D. (4 pts) — Systémique : Tableau de bord clair (sécurité, propreté, etc.) analysé et partagé."
]
q4_sel = st.sidebar.radio("Q4. Mesure d'impact ?", opt_q4)
s4 = opt_q4.index(q4_sel) + 1

# -- AXE B --
st.sidebar.markdown("---")
st.sidebar.markdown("### AXE B : OPÉRATIONS")

opt_q5 = [
    "A. (1 pt) — Réactif : On subit. Souvent on ne dit rien.",
    "B. (2 pts) — Formel : Réaction au cas par cas, tardive, communiqué générique.",
    "C. (3 pts) — Collaboratif : Porte-parole identifié, messages-clés, réponse rapide.",
    "D. (4 pts) — Systémique : Plan de communication de crise documenté et stratégie proactive."
]
q5_sel = st.sidebar.radio("Q5. Gestion des crises médiatiques ?", opt_q5)
s5 = opt_q5.index(q5_sel) + 1

opt_q6 = [
    "A. (1 pt) — Réactif : Non, pas de formation spécifique sur la cohabitation.",
    "B. (2 pts) — Formel : Formation ponctuelle à l'ouverture, rien de continu.",
    "C. (3 pts) — Collaboratif : Formations internes régulières et rétroactions.",
    "D. (4 pts) — Systémique : Formation structurée pour tou.te.s (CPTED, CNV, etc.) et mises à jour."
]
q6_sel = st.sidebar.radio("Q6. Formation des équipes ?", opt_q6)
s6 = opt_q6.index(q6_sel) + 1

opt_q7 = [
    "A. (1 pt) — Réactif : On ne sort pas. L'extérieur n'est « pas notre problème ».",
    "B. (2 pts) — Formel : Sorties ponctuelles sur plainte, sans protocole.",
    "C. (3 pts) — Collaboratif : Rondes régulières aux abords immédiats (10-20m).",
    "D. (4 pts) — Systémique : Gestion active d'une « zone tampon » (50-100m), présence visible."
]
q7_sel = st.sidebar.radio("Q7. Intervention HORS les murs ?", opt_q7)
s7 = opt_q7.index(q7_sel) + 1

opt_q8 = [
    "A. (1 pt) — Réactif : Arbitraire, selon l'humeur. Pas de procédure de retour.",
    "B. (2 pts) — Formel : Variable. Parfois rencontre au retour, parfois non.",
    "C. (3 pts) — Collaboratif : Grille de gradation selon la gravité. Rencontre généralement faite.",
    "D. (4 pts) — Systémique : Protocole (vert-jaune-rouge), durées définies, retour obligatoire, suivi documenté."
]
q8_sel = st.sidebar.radio("Q8. Gestion des pauses de service/exclusions ?", opt_q8)
s8 = opt_q8.index(q8_sel) + 1

# -- AXE C --
st.sidebar.markdown("---")
st.sidebar.markdown("### AXE C : ALLIANCES")

opt_q9 = [
    "A. (1 pt) — Réactif : Presque pas de contact. Relations tendues.",
    "B. (2 pts) — Formel : Courriels administratifs, pas de collaboration terrain.",
    "C. (3 pts) — Collaboratif : Contacts réguliers et constructifs.",
    "D. (4 pts) — Systémique : Table de concertation locale, co-construction de solutions."
]
q9_sel = st.sidebar.radio("Q9. Relations services municipaux ?", opt_q9)
s9 = opt_q9.index(q9_sel) + 1

opt_q10 = [
    "A. (1 pt) — Réactif : Non, chacun gère son coin. Compétition.",
    "B. (2 pts) — Formel : Occasionnel, mais travail en silo.",
    "C. (3 pts) — Collaboratif : Table de concertation, échange sur situations complexes.",
    "D. (4 pts) — Systémique : Réseau structuré, protocoles clairs, stratégies communes."
]
q10_sel = st.sidebar.radio("Q10. Collaboration organismes du secteur ?", opt_q10)
s10 = opt_q10.index(q10_sel) + 1

opt_q11 = [
    "A. (1 pt) — Réactif : Évitement. On subit les reproches.",
    "B. (2 pts) — Formel : Réponses polies aux plaintes, pas de proactivité.",
    "C. (3 pts) — Collaboratif : Rencontres de voisinage 2-3 fois/an.",
    "D. (4 pts) — Systémique : Comité de bon voisinage co-créé, ambassadeurs."
]
q11_sel = st.sidebar.radio("Q11. Implication citoyenne ?", opt_q11)
s11 = opt_q11.index(q11_sel) + 1

opt_q12 = [
    "A. (1 pt) — Réactif : Non, les équipes font tout (clinique + médiation). Débordées.",
    "B. (2 pts) — Formel : On aimerait, mais pas de budget.",
    "C. (3 pts) — Collaboratif : Parfois médiateur externe, mais non systématique.",
    "D. (4 pts) — Systémique : Poste dédié financé (agent de milieu/médiateur)."
]
q12_sel = st.sidebar.radio("Q12. Médiation sociale dédiée ?", opt_q12)
s12 = opt_q12.index(q12_sel) + 1

# 7. CALCULS ET LOGIQUE
total_score = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10 + s11 + s12
score_a = s1 + s2 + s3 + s4
score_b = s5 + s6 + s7 + s8
score_c = s9 + s10 + s11 + s12

data = get_profile_data(total_score)

# 8. AFFICHAGE PRINCIPAL (MAIN AREA)

# Section A: Graphique et Scores
col_stats, col_radar = st.columns([1, 1])

with col_stats:
    st.subheader("📊 VOS RÉSULTATS")
    
    # Affichage en colonnes des scores
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("TOTAL", f"{total_score}/48")
    m2.metric("AXE A", f"{score_a}/16")
    m3.metric("AXE B", f"{score_b}/16")
    m4.metric("AXE C", f"{score_c}/16")

    st.markdown("---")
    st.markdown(f"**Axe A :** Gouvernance & Protocoles")
    st.markdown(f"**Axe B :** Opérations & Terrain")
    st.markdown(f"**Axe C :** Alliances & Partenariats")

with col_radar:
    # Radar Chart
    categories = ['Gouvernance', 'Opérations', 'Alliances']
    values = [score_a, score_b, score_c]
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Votre Score',
        line_color='#2c3e50',
        fillcolor='rgba(44, 62, 80, 0.4)'
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 16])
        ),
        showlegend=False,
        margin=dict(t=20, b=20, l=40, r=40),
        height=250
    )
    st.plotly_chart(fig, use_container_width=True)

# Section B: La Carte Profil (Design soigné)
st.markdown(f"""
<div class="profile-card {data['css_class']}">
    <div class="profile-title">{data['nom']}</div>
    <div class="profile-score">{data['score_txt']}</div>
    <p><strong>🔍 VOTRE RÉALITÉ ACTUELLE</strong><br>{data['intro']}</p>
</div>
""", unsafe_allow_html=True)

# Section C: Forces et Risques (Colonnes)
c1, c2 = st.columns(2)
with c1:
    st.markdown("### ✅ VOS FORCES")
    for force in data['forces']:
        st.markdown(f"- {force}")

with c2:
    st.markdown("### ⚠️ VOS RISQUES")
    for risque in data['risques']:
        st.markdown(f"- {risque}")

# Section D: Action Prioritaire (Boite spéciale)
st.markdown(f"""
<div class="action-box">
    <div class="action-badge">🎯 LOW HANGING FRUIT</div>
    <div class="action-main-title">VOTRE ACTION PRIORITAIRE</div>
    <p><em>Ne tentez pas de tout refaire. Commencez par UNE SEULE CHOSE :</em></p>
    
    <h3 style="color:#c0392b; margin-top:10px;">➜ {data['action_titre']}</h3>
    
    <span class="action-subtitle">POURQUOI ?</span>
    {data['action_why']}
    
    <span class="action-subtitle">COMMENT ?</span>
    {data['action_how']}
    
    <span class="action-subtitle">⏱️ TEMPS REQUIS</span>
    {data['action_time']}
</div>
""", unsafe_allow_html=True)

# Section E: Chapitres
st.markdown("### 📚 CHAPITRES RECOMMANDÉS")
st.markdown(f"""
<div class="chapter-box">
    <p>🔥 <strong>Priorité 1 (À lire maintenant) :</strong><br>{data['chap_prio1']}</p>
    <p>📅 <strong>Priorité 2 (Dans les 3-6 mois) :</strong><br>{data['chap_prio2']}</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("Outil généré pour le Guide de la Cohabitation Sociale.")
