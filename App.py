# -*- coding: utf-8 -*-
import streamlit as st
import plotly.graph_objects as go
import base64
from datetime import datetime

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Radar Cohabitation", page_icon="🎯", layout="wide")

# 2. CSS AVANCÉ (DESIGN PROPRE & LISIBILITÉ)
st.markdown("""
<style>
    /* FORCER LE FOND BLANC ET TEXTE NOIR */
    .stApp, .stAppViewContainer {
        background-color: #ffffff !important;
        color: #0f172a !important;
    }
    
    /* TYPOGRAPHIE */
    h1, h2, h3 {
        color: #1e293b !important;
        font-family: 'Helvetica Neue', sans-serif;
    }
    p, div, label, li, span {
        color: #334155 !important;
        font-size: 1.05rem;
        line-height: 1.6;
    }

    /* HEADER */
    .header-box {
        background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
        color: white !important;
    }
    .header-box h1 { color: white !important; margin: 0; }
    .header-box p { color: #e2e8f0 !important; }

    /* ONGLETS DE NAVIGATION (QUESTIONS) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f1f5f9;
        border-radius: 5px;
        color: #0f172a;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: #e0f2fe;
        color: #0284c7;
        border-bottom-color: #0284c7;
    }

    /* CARTES RÉSULTATS */
    .result-card {
        padding: 25px;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        background-color: #f8fafc;
        margin-bottom: 20px;
        border-left: 8px solid #cbd5e1;
    }
    .border-red { border-left-color: #dc2626 !important; background-color: #fef2f2 !important; }
    .border-orange { border-left-color: #ea580c !important; background-color: #fff7ed !important; }
    .border-blue { border-left-color: #2563eb !important; background-color: #eff6ff !important; }
    .border-green { border-left-color: #16a34a !important; background-color: #f0fdf4 !important; }

    /* ACTION PRIORITAIRE (ÉPURÉE SANS BADGE) */
    .action-box {
        background-color: #ffffff;
        border: 2px solid #cbd5e1;
        border-radius: 10px;
        padding: 25px;
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .action-title {
        color: #b91c1c !important;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 15px;
        border-bottom: 1px solid #eee;
        padding-bottom: 10px;
    }

    /* CACHER L'ICON GITHUB/MENU STREAMLIT */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 3. EN-TÊTE PRINCIPAL
st.markdown("""
<div class="header-box">
    <h1>LE RADAR DE MATURITÉ EN COHABITATION</h1>
    <p>Outil d'auto-diagnostic stratégique — Répondez aux questions ci-dessous pour obtenir votre profil.</p>
</div>
""", unsafe_allow_html=True)

# 4. FONCTION POUR GÉNÉRER LE RAPPORT (HTML/PDF)
def create_download_link(content_dict, total_score):
    # Sécurisation des textes pour le HTML
    forces_html = "".join([f"<li>{f}</li>" for f in content_dict['forces']])
    risques_html = "".join([f"<li>{r}</li>" for r in content_dict['risques']])
    
    html_content = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Helvetica, Arial, sans-serif; padding: 40px; color: #333; }}
            h1 {{ color: #1e3a8a; border-bottom: 2px solid #1e3a8a; padding-bottom: 10px; }}
            h2 {{ color: #b91c1c; margin-top: 30px; }}
            h3 {{ color: #1e293b; background-color: #f1f5f9; padding: 10px; }}
            .score-box {{ font-size: 24px; font-weight: bold; margin: 20px 0; }}
            .section {{ margin-bottom: 20px; line-height: 1.5; }}
            .footer {{ margin-top: 50px; font-size: 12px; color: #666; border-top: 1px solid #ccc; padding-top: 10px; }}
        </style>
    </head>
    <body>
        <h1>Rapport de Diagnostic : Cohabitation Sociale</h1>
        <p>Date : {datetime.now().strftime("%d/%m/%Y")}</p>
        
        <div class="score-box">
            Votre Score Global : {total_score} / 48<br>
            Profil : {content_dict['nom'].replace('PROFIL : ', '')}
        </div>

        <div class="section">
            <h3>🔍 VOTRE RÉALITÉ ACTUELLE</h3>
            <p>{content_dict['intro']}</p>
        </div>

        <div class="section">
            <h3>✅ VOS FORCES</h3>
            <ul>{forces_html}</ul>
        </div>

        <div class="section">
            <h3>⚠️ VOS RISQUES</h3>
            <ul>{risques_html}</ul>
        </div>

        <div class="section">
            <h2>🎯 ACTION PRIORITAIRE</h2>
            <p><strong>{content_dict['action_titre']}</strong></p>
            <p><strong>POURQUOI ?</strong><br>{content_dict['action_why']}</p>
            <p><strong>COMMENT ?</strong><br>{content_dict['action_how']}</p>
            <p><strong>TEMPS REQUIS :</strong> {content_dict['action_time']}</p>
        </div>

        <div class="section">
            <h3>📚 LECTURES RECOMMANDÉES</h3>
            <p>{content_dict['chap_prio1']}</p>
            <p>{content_dict['chap_prio2']}</p>
        </div>

        <div class="footer">
            Généré par Le Radar de Maturité en Cohabitation.
        </div>
    </body>
    </html>
    """
    b64 = base64.b64encode(html_content.encode()).decode()
    return f'<a href="data:text/html;base64,{b64}" download="Rapport_Cohabitation.html" style="background-color:#2563eb; color:white; padding:12px 25px; text-decoration:none; border-radius:5px; font-weight:bold; display:inline-block; margin-top:10px;">📥 TÉLÉCHARGER VOS RÉSULTATS (PDF/Impression)</a>'

# 5. BASE DE DONNÉES TEXTUELLE (SÉCURISÉE AVEC TRIPLES GUILLEMETS)
def get_profile_data(score):
    if score <= 24:
        return {
            "nom": "PROFIL 1 : LE POMPIER SOLITAIRE",
            "score_txt": "Score : 12 à 24 points",
            "css_class": "border-red",
            "intro": """Vous êtes en mode survie. Votre équipe gère au jour le jour, sans protocoles formalisés, avec peu ou pas de collaboration structurée avec le voisinage ou les partenaires externes. Les crises éclatent, vous réagissez, et vous recommencez le lendemain.""",
            "forces": [
                """Vous êtes sur le terrain, proche des personnes qui se prévalent des services""",
                """Vous faites preuve de résilience et d'adaptation constante""",
                """Vous connaissez intimement les réalités de votre clientèle"""
            ],
            "risques": [
                """**Épuisement de l'équipe** : Tout repose sur quelques personnes clés. Le taux de roulement est élevé.""",
                """**Incohérence** : Chaque intervenant.e gère les situations à sa façon. Pas de prévisibilité.""",
                """**Vulnérabilité médiatique** : Une vidéo virale, un article négatif, et vous n'avez aucun filet de sécurité.""",
                """**Isolement** : Vous êtes perçu comme « le problème » par le voisinage et la Ville, plutôt que comme un partenaire."""
            ],
            "action_titre": """Créez votre premier protocole d'intervention écrit (Gestion des comportements qui dérangent).""",
            "action_why": """Parce que c'est le fondement de tout. Tant que vos équipes d’intervention n'ont pas un cadre clair et partagé, vous resterez en mode réactif. Ce protocole vous permettra de réduire la gestion arbitraire des situations problématiques (et donc les frustrations internes), d'avoir une réponse cohérente à donner aux citoyen.ne.s qui se plaignent et de protéger juridiquement votre organisme en cas de litige.""",
            "action_how": """Allez lire le **Chapitre 3** de ce Guide : *Principes d'intervention et gestion quotidienne de la cohabitation sociale*. Vous y trouverez un modèle de protocole de gestion des comportements qui dérangent (vert-jaune-rouge) prêt à adapter.""",
            "action_time": """Deux (2) à trois (3) réunions d'équipe pour co-créer le protocole, puis formation de deux (2) heures pour l'implanter.""",
            "chap_prio1": """<strong>Priorité 1 :</strong> Chapitre 3 (Principes d'intervention et gestion quotidienne)""",
            "chap_prio2": """<strong>Priorité 2 :</strong> Chapitre 1 (Écosystème) et Chapitre 6 (Gouvernance)"""
        }
    elif score <= 33:
        return {
            "nom": "PROFIL 2 : LE GESTIONNAIRE STRUCTURÉ",
            "score_txt": "Score : 25 à 33 points",
            "css_class": "border-orange",
            "intro": """Vous avez posé des bases solides. Vous avez des protocoles écrits, des règles claires, et une certaine organisation interne. Cependant, l'application reste inégale, les partenariats sont informels, et vous sentez que votre approche pourrait être plus fluide et collaborative.""",
            "forces": [
                """Vous avez des outils et des procédures (règlements, protocoles de base)""",
                """Votre équipe connaît les attentes minimales""",
                """Vous documentez certaines de vos interventions"""
            ],
            "risques": [
                """**Rigidité** : Vos protocoles existent, mais ils sont appliqués de façon mécanique. Peu de place pour l'adaptation ou la désescalade créative.""",
                """**Relations tendues avec le voisinage** : Vous gérez les plaintes, mais vous n'avez pas vraiment construit de lien de confiance avec les citoyen.ne.s.""",
                """**Silos** : Vous fonctionnez en vase clos. Les partenariats sont limités ou ponctuels.""",
                """**Communication défensive** : En cas de crise médiatique, vous réagissez, mais vous ne maîtrisez pas le narratif."""
            ],
            "action_titre": """Formalisez vos relations avec le voisinage (créez, entre autres, votre premier Pacte de bon voisinage).""",
            "action_why": """Parce que vous avez déjà la structure interne. Ce qui vous manque, c'est le pont vers l'externe. Un Pacte de bon voisinage transforme les plaintes récurrentes en dialogue structuré, et les citoyens méfiants en alliés potentiels.""",
            "action_how": """Allez lire le **Chapitre 4** de ce Guide : *Le rôle des citoyen.ne.s et du voisinage : de la plainte à la collaboration*. Vous y trouverez un modèle complet de Pacte de bon voisinage (clause par clause) prêt à adapter.""",
            "action_time": """Quatre (4) à six (6) semaines (identification des parties prenantes, rédaction collaborative du pacte, signature formelle, première rencontre de suivi).""",
            "chap_prio1": """<strong>Priorité 1 :</strong> Chapitre 4 (Le rôle des citoyen.ne.s) et Chapitre 5 (Outils)""",
            "chap_prio2": """<strong>Priorité 2 :</strong> Chapitre 7 (Communication) et Chapitre 6 (Gouvernance)"""
        }
    elif score <= 42:
        return {
            "nom": "PROFIL 3 : LE PARTENAIRE STRATÉGIQUE",
            "score_txt": "Score : 34 à 42 points",
            "css_class": "border-blue",
            "intro": """Vous êtes dans le peloton de tête. Vous avez des protocoles solides, des partenariats actifs, et une relation constructive avec le voisinage. Votre organisme est reconnu comme un acteur de solutions, pas comme un « problème ». Cependant, vous sentez qu'il reste des angles morts, et vous voulez optimiser.""",
            "forces": [
                """Protocoles clairs et appliqués de façon cohérente""",
                """Partenariats structurés avec la Ville, les organismes pairs, et le voisinage""",
                """Capacité à gérer les crises sans panique""",
                """Certaines mesures d'impact documentées"""
            ],
            "risques": [
                """**Proactivité vs Réactivité** : Vous gérez bien les crises, mais pourriez-vous les anticiper davantage ?""",
                """**Mesure d'impact** : Vous collectez des données, mais les exploitez-vous stratégiquement pour influencer les politiques ou sécuriser du financement ?""",
                """**Innovation** : Pourriez-vous tester de nouvelles approches (médiation sociale dédiée, zone tampon élargie, co-construction avec les personnes qui se prévalent des services) ?"""
            ],
            "action_titre": """Structurez votre tableau de bord d'impact et utilisez-le comme levier stratégique.""",
            "action_why": """Il vous manque la capacité à démontrer votre valeur ajoutée de manière chiffrée pour obtenir du financement additionnel ou le stabiliser, influencer les décisions municipales et provinciales, inspirer d'autres organismes et protéger votre réputation en cas de crise.""",
            "action_how": """Allez lire le **Chapitre 8** de ce Guide : *Mesurer votre impact pour durer — Indicateurs et pérennité*. Vous y trouverez un cadre complet pour bâtir un tableau de bord d'impact adapté à la cohabitation sociale.""",
            "action_time": """Quatre (4) à six (6) semaines (identification des indicateurs clés, mise en place d'outils de collecte de données, formation de l'équipe, premier rapport d'impact).""",
            "chap_prio1": """<strong>Priorité 1 :</strong> Chapitre 8 (Mesurer votre impact) et Chapitre 7 (Communication)""",
            "chap_prio2": """<strong>Priorité 2 :</strong> Chapitre 6 (Gouvernance) et Chapitre 2 (Implantation)"""
        }
    else:
        return {
            "nom": "PROFIL 4 : L'INNOVATEUR SYSTÉMIQUE",
            "score_txt": "Score : 43 à 48 points",
            "css_class": "border-green",
            "intro": """Vous êtes une référence. Votre organisme fonctionne comme une organisation apprenante : protocoles solides, partenariats stratégiques, mesure d'impact rigoureuse, communication proactive, implication citoyenne structurée. Vous ne gérez pas juste la cohabitation — vous la co-construisez.""",
            "forces": [
                """Approche préventive et proactive (vous gérez les risques avant qu'ils ne deviennent des crises)""",
                """Partenariats intersectoriels (Ville, CIUSSS, organismes pairs, citoyens, commerces)""",
                """Innovations terrain (médiation sociale dédiée, zone tampon active, co-construction avec les usagers)""",
                """Influence sur les politiques publiques locales"""
            ],
            "risques": [
                """**Pérennité** : Comment maintenir ce niveau d'excellence malgré les changements de financement, de personnel, ou de contexte politique ?""",
                """**Essaimage** : Comment transférer vos pratiques à d'autres organismes sans créer de dépendance ?""",
                """**Fatigue de l'excellence** : Votre équipe est-elle en risque d’épuisement ou fatigue de compassion à force de vouloir tout faire parfaitement ?"""
            ],
            "action_titre": """Documentez vos pratiques exemplaires et partagez-les (devenez une ressource pour le réseau).""",
            "action_why": """Votre prochain levier est de multiplier votre impact en inspirant et en outillant d'autres organismes. Cela vous permettra de renforcer votre légitimité auprès des bailleurs de fonds, créer des alliances stratégiques, contribuer à l'amélioration systémique du secteur et valoriser votre équipe.""",
            "action_how": """Consultez la **Conclusion** et le **Chapitre 8** (Mesurer votre impact) pour structurer votre démarche de transfert de connaissances. Envisagez de publier des études de cas, d'offrir du mentorat, de co-animer des formations ou de participer à des comités consultatifs.""",
            "action_time": """Trois (3) à six (6) mois pour structurer une offre de transfert de connaissances (rédaction de cas, création d'outils, partenariats).""",
            "chap_prio1": """<strong>Priorité 1 :</strong> Chapitre 8 (Impact) et Conclusion""",
            "chap_prio2": """<strong>Priorité 2 :</strong> Tous les chapitres (Lecture en mode mentorat)"""
        }

# 6. NAVIGATION ET QUESTIONS (CENTRALISÉES PAR ONGLETS)

tab1, tab2, tab3, tab4 = st.tabs(["1. GOUVERNANCE", "2. OPÉRATIONS", "3. ALLIANCES", "📊 RÉSULTATS"])

scores = {}

with tab1:
    st.markdown("### AXE A : GOUVERNANCE & PROTOCOLES")
    st.info("« Est-ce que c'est écrit, clair et appliqué ? »")
    
    # QUESTION 1
    q1_opts = [
        """A. (1 pt) — Réactif : Non, on gère au cas par cas selon l'intervenant.e en poste. Chacun a sa méthode.""",
        """B. (2 pts) — Formel : Oui, on a un code de vie interne affiché, mais il est rarement appliqué de façon constante et cohérente (Tout dépend de qui est en poste).""",
        """C. (3 pts) — Collaboratif : Oui, on a un protocole écrit et l'équipe le connaît. On fait des ajustements réguliers en réunion clinique.""",
        """D. (4 pts) — Systémique : Oui, on a un protocole de gestion des comportements qui dérangent (niveaux vert-jaune-rouge), documenté, appliqué de façon cohérente, et révisé annuellement avec l'équipe."""
    ]
    q1 = st.radio("Q1. Votre organisme dispose-t-il d'un protocole écrit de gestion des comportements qui dérangent (violence, menaces, consommation indiscrète importante, etc.) ?", q1_opts)
    scores["Q1"] = q1_opts.index(q1) + 1
    st.markdown("---")

    # QUESTION 2
    q2_opts = [
        """A. (1 pt) — Réactif : Non, on réagit seulement quand il y a une plainte. On n'a pas de contact proactif avec le voisinage.""",
        """B. (2 pts) — Formel : On a eu une rencontre d'information lors de l'ouverture, mais rien de structuré depuis. Les citoyen.ne.s appellent directement la Ville ou l’Arrondissement quand ils.elles sont insatisfait.e.s.""",
        """C. (3 pts) — Collaboratif : On organise des rencontres périodiques (2-4 fois par année) avec un comité de citoyen.ne.s. Le dialogue existe, mais ce n'est pas formalisé par écrit.""",
        """D. (4 pts) — Systémique : On a signé un Pacte de bon voisinage écrit avec des engagements clairs de part et d'autre, des rencontres trimestrielles, et un mécanisme de résolution de conflits défini."""
    ]
    q2 = st.radio("Q2. Avez-vous formalisé vos engagements avec le voisinage (pacte, entente, rencontres structurées) ?", q2_opts)
    scores["Q2"] = q2_opts.index(q2) + 1
    st.markdown("---")

    # QUESTION 3
    q3_opts = [
        """A. (1 pt) — Réactif : Non, on ne sait pas toujours qui doit faire quoi. On se renvoie souvent la balle entre organismes.""",
        """B. (2 pts) — Formel : On a des ententes de service signées, mais dans les faits, les zones grises créent de la confusion sur le terrain.""",
        """C. (3 pts) — Collaboratif : Les rôles sont relativement clairs. On se parle régulièrement pour ajuster. Ça fonctionne bien grâce aux relations interpersonnelles.""",
        """D. (4 pts) — Systémique : On a un cadre de gouvernance écrit (qui fait quoi, qui décide quoi, qui finance quoi), partagé avec tous les partenaires, et une instance de coordination active."""
    ]
    q3 = st.radio("Q3. Les rôles et responsabilités entre votre organisme, la Ville, le CIUSSS et les autres partenaires impliqués sont-ils clairs et documentés ?", q3_opts)
    scores["Q3"] = q3_opts.index(q3) + 1
    st.markdown("---")

    # QUESTION 4
    q4_opts = [
        """A. (1 pt) — Réactif : Non, on n'a pas le temps de compiler des données. On se fie à notre « feeling » terrain.""",
        """B. (2 pts) — Formel : On collecte quelques données (nombre de refus, incidents), mais on ne les analyse pas vraiment ni ne les partage.""",
        """C. (3 pts) — Collaboratif : On suit des indicateurs de base (taux d'occupation, incidents, plaintes du voisinage) et on les présente en réunion d'équipe ou aux directions.""",
        """D. (4 pts) — Systémique : On a un tableau de bord avec des indicateurs clairs (sécurité, propreté, satisfaction voisinage, taux de réintégration), analysés mensuellement, et partagés avec nos bailleurs de fonds/partenaires stratégiques."""
    ]
    q4 = st.radio("Q4. Mesurez-vous l'impact de vos interventions de cohabitation (données, indicateurs, rapports) ?", q4_opts)
    scores["Q4"] = q4_opts.index(q4) + 1

with tab2:
    st.markdown("### AXE B : OPÉRATIONS & TERRAIN")
    st.info("« Comment on réagit concrètement aux situations de crise ? »")

    # QUESTION 5
    q5_opts = [
        """A. (1 pt) — Réactif : On subit. On ne sait jamais quoi dire. Souvent, on ne dit rien et on espère que ça passe.""",
        """B. (2 pts) — Formel : On réagit au cas par cas, souvent avec retard. On publie un communiqué générique qui satisfait rarement les gens.""",
        """C. (3 pts) — Collaboratif : On a identifié un porte-parole interne. On prépare des messages-clés adaptés à la situation et on répond rapidement (dans les 24-48h).""",
        """D. (4 pts) — Systémique : On a un plan de communication de crise documenté, avec des messages pré-approuvés, un protocole de gestion des médias sociaux, et une stratégie proactive (on communique AVANT que les problèmes n'explosent)."""
    ]
    q5 = st.radio("Q5. Comment gérez-vous les crises médiatiques (vidéo virale, article négatif, pression des citoyen.ne.s sur les réseaux sociaux) ?", q5_opts)
    scores["Q5"] = q5_opts.index(q5) + 1
    st.markdown("---")

    # QUESTION 6
    q6_opts = [
        """A. (1 pt) — Réactif : Non, on embauche des gens avec de l'expérience en intervention, mais on n'offre pas de formation spécifique sur la cohabitation avec le voisinage.""",
        """B. (2 pts) — Formel : On a fait une formation ponctuelle lors de l'ouverture, mais rien de continu. Les nouvelles recrues apprennent « sur le tas ».""",
        """C. (3 pts) — Collaboratif : On organise des formations internes régulières (désescalade, médiation, gestion des plaintes) et on fait des rétroactions d'incidents en équipe.""",
        """D. (4 pts) — Systémique : Tou.te.s les intervenant.e.s reçoivent une formation structurée en cohabitation sociale (CPTED, réduction des risques, communication non-violente, gestion des comportements qui dérangent), avec des mises à jour annuelles et des supervisions cliniques régulières."""
    ]
    q6 = st.radio("Q6. Vos équipes d’intervention sont-elles formées spécifiquement à la prévention et gestion de la cohabitation sociale (pas juste à l'intervention clinique) ?", q6_opts)
    scores["Q6"] = q6_opts.index(q6) + 1
    st.markdown("---")

    # QUESTION 7
    q7_opts = [
        """A. (1 pt) — Réactif : On ne sort pas. On gère seulement ce qui se passe à l'intérieur. L'extérieur, ce n’est « pas notre problème ».""",
        """B. (2 pts) — Formel : On sort parfois si un.e citoyen.ne se plaint, mais on n'a pas de protocole clair ni de ressources dédiées.""",
        """C. (3 pts) — Collaboratif : On a des intervenant.e.s qui font des rondes régulières sur le parvis et aux abords immédiats (rayon de 10-20m). On nettoie quotidiennement.""",
        """D. (4 pts) — Systémique : On gère activement une « zone tampon » de 50-100m autour de notre établissement : nettoyage structuré, présence visible, médiation proactive avec les personnes en situation d’itinérance et le voisinage."""
    ]
    q7 = st.radio("Q7. Quelle est votre capacité à intervenir HORS de votre bâtiment (parvis, ruelle adjacente, parc à proximité, campement, etc.) ?", q7_opts)
    scores["Q7"] = q7_opts.index(q7) + 1
    st.markdown("---")

    # QUESTION 8
    q8_opts = [
        """A. (1 pt) — Réactif : Non, les pauses de service sont décidées de façon arbitraire selon l'humeur de l'équipe d’intervention. Nous n’avons pas de procédure de retour.""",
        """B. (2 pts) — Formel : On exclut quand c'est grave, mais les durées varient beaucoup. Parfois les gens reviennent sans rencontre, parfois il y a une rencontre de réalisée.""",
        """C. (3 pts) — Collaboratif : On a une grille de gradation des conséquences selon la gravité de la situation (violence = X jours). Les retours nécessitent généralement une rencontre avec un.e intervenant.e.""",
        """D. (4 pts) — Systémique : On a un protocole de gestion des comportements qui dérangent (vert-jaune-rouge) avec des durées de pauses de service/conséquences définies selon la gravité de la situation, des rencontres de retour obligatoires, et un suivi documenté dans le dossier clinique."""
    ]
    q8 = st.radio("Q8. Avez-vous un processus clair pour gérer les pauses de service au sein de votre organisme et les retours après les pauses de service ?", q8_opts)
    scores["Q8"] = q8_opts.index(q8) + 1

with tab3:
    st.markdown("### AXE C : ALLIANCES & PARTENARIATS")
    st.info("« Travaille-t-on seul ou en réseau ? »")

    # QUESTION 9
    q9_opts = [
        """A. (1 pt) — Réactif : On n'a presque pas de contact. Quand on se parle, c'est souvent tendu (ils nous voient comme « le problème ») ou nous les percevons comme des menaces.""",
        """B. (2 pts) — Formel : On se connaît de nom, on s'échange des courriels administratifs, mais il n'y a pas vraiment de collaboration terrain.""",
        """C. (3 pts) — Collaboratif : On a des contacts réguliers et constructifs. On peut appeler le poste de quartier et/ou le responsable municipal quand il y a un enjeu.""",
        """D. (4 pts) — Systémique : On siège à une table de concertation locale avec la Ville, la police communautaire, et d'autres partenaires. On co-construit des solutions et on partage des données."""
    ]
    q9 = st.radio("Q9. Quelle est la qualité de votre relation avec les services municipaux (police, 311, propreté, urbanisme) ?", q9_opts)
    scores["Q9"] = q9_opts.index(q9) + 1
    st.markdown("---")

    # QUESTION 10
    q10_opts = [
        """A. (1 pt) — Réactif : Non, chacun gère son coin. On se voit comme des compétiteurs (pour le financement, pour les personnes qui se prévalent des services, etc.).""",
        """B. (2 pts) — Formel : On se parle occasionnellement, mais chacun travaille en silo. On ne partage pas vraiment d'information ni de stratégie.""",
        """C. (3 pts) — Collaboratif : On participe à une table de concertation locale. On échange sur les situations complexes et on se réfère mutuellement des personnes en situation d’itinérance requérant du soutien.""",
        """D. (4 pts) — Systémique : On fait partie d'un réseau structuré avec des protocoles de collaboration clairs (partage d'informations stratégiques et opérationnelles, gestion des comportements qui dérangent, stratégies communes de cohabitation, financement partagé pour médiation sociale, etc.)."""
    ]
    q10 = st.radio("Q10. Collaborez-vous avec d'autres organismes du secteur (refuges, haltes, centres de jour, réseau de la santé) pour gérer collectivement la cohabitation ?", q10_opts)
    scores["Q10"] = q10_opts.index(q10) + 1
    st.markdown("---")

    # QUESTION 11
    q11_opts = [
        """A. (1 pt) — Réactif : Non, on évite les citoyen.ne.s. Quand ils appellent, on subit leurs reproches. On n'a pas de stratégie d'engagement.""",
        """B. (2 pts) — Formel : On répond poliment aux plaintes, mais on ne cherche pas à créer une relation proactive avec le voisinage.""",
        """C. (3 pts) — Collaboratif : On organise des rencontres de voisinage 2-3 fois par année. Les citoyen.ne.s peuvent nous poser des questions et on explique notre mission.""",
        """D. (4 pts) — Systémique : On a co-créé un Comité de bon voisinage avec des résident.e.s volontaires. Ils participent à des activités (nettoyage collectif, 5 à 7, portes ouvertes) et deviennent des « ambassadeur.drice.s » de la cohabitation."""
    ]
    q11 = st.radio("Q11. Impliquez-vous les citoyen.ne.s/voisinage de manière constructive (au-delà de « gérer les plaintes ») ?", q11_opts)
    scores["Q11"] = q11_opts.index(q11) + 1
    st.markdown("---")

    # QUESTION 12
    q12_opts = [
        """A. (1 pt) — Réactif : Non, nos équipes d’intervention de proximité font tout : clinique + gestion des plaintes + médiation. Elles sont débordées.""",
        """B. (2 pts) — Formel : On aimerait avoir une équipe dédiée à la médiation, mais on n'a pas le budget. On se débrouille avec nos ressources internes.""",
        """C. (3 pts) — Collaboratif : On a parfois accès à un médiateur externe (via la Ville ou un partenaire), mais ce n'est pas systématique ni financé de façon stable.""",
        """D. (4 pts) — Systémique : On a un poste dédié (agent de milieu, médiateur social, intervenant.e de proximité) financé spécifiquement pour gérer la zone tampon et les relations avec le voisinage. C'est distinct et complémentaire de l'intervention clinique."""
    ]
    q12 = st.radio("Q12. Avez-vous accès à des ressources de médiation sociale ou de travail de proximité dédiées à la cohabitation (pas juste à l'intervention clinique) ?", q12_opts)
    scores["Q12"] = q12_opts.index(q12) + 1

# 7. CALCULS ET RÉSULTATS
with tab4:
    total_score = sum(scores.values())
    score_a = scores["Q1"] + scores["Q2"] + scores["Q3"] + scores["Q4"]
    score_b = scores["Q5"] + scores["Q6"] + scores["Q7"] + scores["Q8"]
    score_c = scores["Q9"] + scores["Q10"] + scores["Q11"] + scores["Q12"]
    
    data = get_profile_data(total_score)

    st.success("✅ Cliquez ci-dessous pour voir votre profil complet.")
    
    col_metrics, col_radar = st.columns([1, 1])
    
    with col_metrics:
        st.markdown("### 📊 VOS SCORES")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("GLOBAL", f"{total_score}/48")
        m2.metric("AXE A", f"{score_a}/16")
        m3.metric("AXE B", f"{score_b}/16")
        m4.metric("AXE C", f"{score_c}/16")
        
        # BOUTON TÉLÉCHARGEMENT PDF
        st.markdown(create_download_link(data, total_score), unsafe_allow_html=True)

    with col_radar:
        categories = ['Gouvernance', 'Opérations', 'Alliances']
        values = [score_a, score_b, score_c]
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Votre Score',
            line_color='#1e3a8a',
            fillcolor='rgba(30, 58, 138, 0.2)'
        ))
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 16], showticklabels=False)),
            showlegend=False,
            margin=dict(t=20, b=20, l=40, r=40),
            height=250
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # AFFICHAGE PROFIL
    st.markdown(f"""
    <div class="result-card {data['css_class']}">
        <h2 style="margin-top:0;">{data['nom']}</h2>
        <p><strong>{data['score_txt']}</strong></p>
        <p>{data['intro']}</p>
    </div>
    """, unsafe_allow_html=True)

    c_forces, c_risques = st.columns(2)
    with c_forces:
        st.markdown("#### ✅ VOS FORCES")
        for force in data['forces']:
            st.markdown(f"- {force}")

    with c_risques:
        st.markdown("#### ⚠️ VOS RISQUES")
        for risque in data['risques']:
            st.markdown(f"- {risque}")

    # ACTION PRIORITAIRE
    st.markdown(f"""
    <div class="action-box">
        <div class="action-title">➡️ ACTION PRIORITAIRE</div>
        <p><em>Ne tentez pas de tout refaire. Commencez par UNE SEULE CHOSE :</em></p>
        <h3>{data['action_titre']}</h3>
        <p><strong>POURQUOI ?</strong><br>{data['action_why']}</p>
        <p><strong>COMMENT ?</strong><br>{data['action_how']}</p>
        <p><strong>TEMPS REQUIS :</strong> {data['action_time']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.info(f"📚 **LECTURES RECOMMANDÉES**\n\n{data['chap_prio1']}\n\n{data['chap_prio2']}")
