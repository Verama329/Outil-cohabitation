# -*- coding: utf-8 -*-
import streamlit as st
import plotly.graph_objects as go

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Radar Cohabitation", page_icon="🎯", layout="wide")

# 2. CSS AVANCÉ (FORCER LE FOND BLANC ET TEXTE NOIR)
st.markdown("""
<style>
    /* FORCER LE FOND BLANC PARTOUT */
    .stApp, div[data-testid="stDecoration"], div[data-testid="stSidebar"], section[data-testid="stSidebar"] {
        background-color: #ffffff !important;
        color: #0f172a !important;
    }
    
    /* TYPOGRAPHIE */
    h1, h2, h3, h4, h5, h6 {
        color: #1e293b !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-weight: 700;
    }
    
    p, li, div, span, label, .stMarkdown {
        color: #334155 !important;
        font-size: 1.05rem;
        line-height: 1.6;
    }

    /* EN-TÊTE */
    .header-box {
        background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
        padding: 40px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .header-box h1 { color: #ffffff !important; margin: 0; font-size: 2.5rem; }
    .header-box p { color: #e2e8f0 !important; font-size: 1.2rem; margin-top: 10px; }

    /* BARRE LATÉRALE */
    section[data-testid="stSidebar"] {
        background-color: #f8fafc !important;
        border-right: 1px solid #e2e8f0;
    }
    /* Force la couleur des boutons radio */
    .stRadio label p {
        color: #0f172a !important;
        font-weight: 600;
        font-size: 1rem;
    }
    div[role="radiogroup"] label {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 10px;
        margin-bottom: 5px;
    }
    div[role="radiogroup"] label:hover {
        border-color: #3b82f6;
        background-color: #eff6ff;
    }

    /* CARTES DE RÉSULTATS */
    .profile-card {
        background-color: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        border-left: 10px solid #94a3b8;
    }
    
    /* COULEURS DES PROFILS */
    .border-red { border-left-color: #dc2626 !important; }
    .border-orange { border-left-color: #ea580c !important; }
    .border-blue { border-left-color: #2563eb !important; }
    .border-green { border-left-color: #16a34a !important; }

    /* ACTION PRIORITAIRE */
    .action-container {
        background-color: #eff6ff !important;
        border: 2px solid #bfdbfe;
        border-radius: 12px;
        padding: 30px;
        margin-top: 30px;
    }
    .action-badge {
        background-color: #b91c1c;
        color: white !important;
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: bold;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 15px;
    }
    
    /* CHAPITRES */
    .chapter-box {
        background-color: #f0fdf4 !important;
        border-left: 5px solid #16a34a;
        padding: 20px;
        border-radius: 8px;
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

# 3. EN-TÊTE
st.markdown("""
<div class="header-box">
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

# 5. CONTENU DES PROFILS
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
            "action_why": "Parce que c'est le fondement de tout. Tant que vos équipes d’intervention n'ont pas un cadre clair et partagé, vous resterez en mode réactif. Ce protocole vous permettra de réduire la gestion arbitraire des situations problématiques (et donc les frustrations internes), d'avoir une réponse cohérente à donner aux citoyen.ne.s qui se plaignent et de protéger juridiquement votre organisme en cas de litige.",
            "action_how": "Allez lire le **Chapitre 3** de ce Guide : *Principes d'intervention et gestion quotidienne de la cohabitation sociale*. Vous y trouverez un modèle de protocole de gestion des comportements qui dérangent (vert-jaune-rouge) prêt à adapter.",
            "action_time": "Deux (2) à trois (3) réunions d'équipe pour co-créer le protocole, puis formation de deux (2) heures pour l'implanter.",
            "chap_prio1": "<strong>Chapitre 3</strong> : Principes d'intervention et gestion quotidienne de la cohabitation sociale",
            "chap_prio2": "<strong>Chapitre 1</strong> (Comprendre l'écosystème) et <strong>Chapitre 6</strong> (Gouvernance et concertation)"
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
                "**Rigidité** : Vos protocoles existent, mais ils sont appliqués de façon mécanique. Peu de place pour l'adaptation ou la désescalade créative.",
                "**Relations tendues avec le voisinage** : Vous gérez les plaintes, mais vous n'avez pas vraiment construit de lien de confiance avec les citoyen.ne.s.",
                "**Silos** : Vous fonctionnez en vase clos. Les partenariats sont limités ou ponctuels.",
                "**Communication défensive** : En cas de crise médiatique, vous réagissez, mais vous ne maîtrisez pas le narratif."
            ],
            "action_titre": "Formalisez vos relations avec le voisinage (créez, entre autres, votre premier Pacte de bon voisinage).",
            "action_why": "Parce que vous avez déjà la structure interne. Ce qui vous manque, c'est le pont vers l'externe. Un Pacte de bon voisinage transforme les plaintes récurrentes en dialogue structuré, et les citoyens méfiants en alliés potentiels.",
            "action_how": "Allez lire le **Chapitre 4** de ce Guide : *Le rôle des citoyen.ne.s et du voisinage : de la plainte à la collaboration*. Vous y trouverez un modèle complet de Pacte de bon voisinage (clause par clause) prêt à adapter.",
            "action_time": "Quatre (4) à six (6) semaines (identification des parties prenantes, rédaction collaborative du pacte, signature formelle, première rencontre de suivi).",
            "chap_prio1": "<strong>Chapitre 4</strong> (Le rôle des citoyen.ne.s) et <strong>Chapitre 5</strong> (Outils à développer)",
            "chap_prio2": "<strong>Chapitre 7</strong> (Communication stratégique) et <strong>Chapitre 6</strong> (Gouvernance et concertation)"
        }
    elif score <= 42:
        return {
            "nom": "PROFIL 3 : LE PARTENAIRE STRATÉGIQUE",
            "score_txt": "Score : 34 à 42 points",
            "css_class": "border-blue",
            "intro": "Vous êtes dans le peloton de tête. Vous avez des protocoles solides, des partenariats actifs, et une relation constructive avec le voisinage. Votre organisme est reconnu comme un acteur de solutions, pas comme un « problème ». Cependant, vous sentez qu'il reste des angles morts, et vous voulez optimiser.",
            "forces": [
                "Protocoles clairs et appliqués de façon cohérente",
                "Partenariats structurés avec la Ville, les organismes pairs, et le voisinage",
                "Capacité à gérer les crises sans panique",
                "Certaines mesures d'impact documentées"
            ],
            "risques": [
                "**Proactivité vs Réactivité** : Vous gérez bien les crises, mais pourriez-vous les anticiper davantage ?",
                "**Mesure d'impact** : Vous collectez des données, mais les exploitez-vous stratégiquement pour influencer les politiques ou sécuriser du financement ?",
                "**Innovation** : Pourriez-vous tester de nouvelles approches (médiation sociale dédiée, zone tampon élargie, co-construction avec les personnes qui se prévalent des services) ?"
            ],
            "action_titre": "Structurez votre tableau de bord d'impact et utilisez-le comme levier stratégique.",
            "action_why": "Il vous manque la capacité à démontrer votre valeur ajoutée de manière chiffrée pour obtenir du financement additionnel ou le stabiliser, influencer les décisions municipales et provinciales, inspirer d'autres organismes et protéger votre réputation en cas de crise.",
            "action_how": "Allez lire le **Chapitre 8** de ce Guide : *Mesurer votre impact pour durer — Indicateurs et pérennité*. Vous y trouverez un cadre complet pour bâtir un tableau de bord d'impact adapté à la cohabitation sociale.",
            "action_time": "Quatre (4) à six (6) semaines (identification des indicateurs clés, mise en place d'outils de collecte de données, formation de l'équipe, premier rapport d'impact).",
            "chap_prio1": "<strong>Chapitre 8</strong> (Mesurer votre impact pour durer) et <strong>Chapitre 7</strong> (Communication stratégique)",
            "chap_prio2": "<strong>Chapitre 6</strong> (Gouvernance et concertation) et <strong>Chapitre 2</strong> (L'implantation stratégique)"
        }
    else:
        return {
            "nom": "PROFIL 4 : L'INNOVATEUR SYSTÉMIQUE",
            "score_txt": "Score : 43 à 48 points",
            "css_class": "border-green",
            "intro": "Vous êtes une référence. Votre organisme fonctionne comme une organisation apprenante : protocoles solides, partenariats stratégiques, mesure d'impact rigoureuse, communication proactive, implication citoyenne structurée. Vous ne gérez pas juste la cohabitation — vous la co-construisez.",
            "forces": [
                "Approche préventive et proactive (vous gérez les risques avant qu'ils ne deviennent des crises)",
                "Partenariats intersectoriels (Ville, CIUSSS, organismes pairs, citoyens, commerces)",
                "Innovations terrain (médiation sociale dédiée, zone tampon active, co-construction avec les usagers)",
                "Influence sur les politiques publiques locales"
            ],
            "risques": [
                "**Pérennité** : Comment maintenir ce niveau d'excellence malgré les changements de financement, de personnel, ou de contexte politique ?",
                "**Essaimage** : Comment transférer vos pratiques à d'autres organismes sans créer de dépendance ?",
                "**Fatigue de l'excellence** : Votre équipe est-elle en risque d’épuisement ou fatigue de compassion à force de vouloir tout faire parfaitement ?"
            ],
            "action_titre": "Documentez vos pratiques exemplaires et partagez-les (devenez une ressource pour le réseau).",
            "action_why": "Votre prochain levier est de multiplier votre impact en inspirant et en outillant d'autres organismes. Cela vous permettra de renforcer votre légitimité auprès des bailleurs de fonds, créer des alliances stratégiques, contribuer à l'amélioration systémique du secteur et valoriser votre équipe.",
            "action_how": "Consultez la **Conclusion** et le **Chapitre 8** (Mesurer votre impact) pour structurer votre démarche de transfert de connaissances. Envisagez de publier des études de cas, d'offrir du mentorat, de co-animer des formations ou de participer à des comités consultatifs.",
            "action_time": "Trois (3) à six (6) mois pour structurer une offre de transfert de connaissances (rédaction de cas, création d'outils, partenariats).",
            "chap_prio1": "<strong>Chapitre 8</strong> (Mesurer votre impact) et <strong>Conclusion</strong> (Vers un urbanisme du lien)",
            "chap_prio2": "<strong>Tous les chapitres</strong> (Pas pour vous-même, mais pour aider d'autres organismes à progresser)"
        }

# 6. SIDEBAR : QUESTIONNAIRE (TEXTE 100% IDENTIQUE AU DOCUMENT)

st.sidebar.header("QUESTIONNAIRE")
st.sidebar.info("Veuillez répondre aux 12 questions ci-dessous.")

st.sidebar.markdown("### AXE A : GOUVERNANCE & PROTOCOLES")
st.sidebar.markdown("_« Est-ce que c'est écrit, clair et appliqué ? »_")

opt_q1 = [
    "A. (1 pt) — Réactif : Non, on gère au cas par cas selon l'intervenant.e en poste. Chacun a sa méthode.",
    "B. (2 pts) — Formel : Oui, on a un code de vie interne affiché, mais il est rarement appliqué de façon constante et cohérente (Tout dépend de qui est en poste).",
    "C. (3 pts) — Collaboratif : Oui, on a un protocole écrit et l'équipe le connaît. On fait des ajustements réguliers en réunion clinique.",
    "D. (4 pts) — Systémique : Oui, on a un protocole de gestion des comportements qui dérangent (niveaux vert-jaune-rouge), documenté, appliqué de façon cohérente, et révisé annuellement avec l'équipe."
]
q1_sel = st.sidebar.radio("Q1. Votre organisme dispose-t-il d'un protocole écrit de gestion des comportements qui dérangent (violence, menaces, consommation indiscrète importante, etc.) ?", opt_q1)
s1 = opt_q1.index(q1_sel) + 1

opt_q2 = [
    "A. (1 pt) — Réactif : Non, on réagit seulement quand il y a une plainte. On n'a pas de contact proactif avec le voisinage.",
    "B. (2 pts) — Formel : On a eu une rencontre d'information lors de l'ouverture, mais rien de structuré depuis. Les citoyen.ne.s appellent directement la Ville ou l’Arrondissement quand ils.elles sont insatisfait.e.s.",
    "C. (3 pts) — Collaboratif : On organise des rencontres périodiques (2-4 fois par année) avec un comité de citoyen.ne.s. Le dialogue existe, mais ce n'est pas formalisé par écrit.",
    "D. (4 pts) — Systémique : On a signé un Pacte de bon voisinage écrit avec des engagements clairs de part et d'autre, des rencontres trimestrielles, et un mécanisme de résolution de conflits défini."
]
q2_sel = st.sidebar.radio("Q2. Avez-vous formalisé vos engagements avec le voisinage (pacte, entente, rencontres structurées) ?", opt_q2)
s2 = opt_q2.index(q2_sel) + 1

opt_q3 = [
    "A. (1 pt) — Réactif : Non, on ne sait pas toujours qui doit faire quoi. On se renvoie souvent la balle entre organismes.",
    "B. (2 pts) — Formel : On a des ententes de service signées, mais dans les faits, les zones grises créent de la confusion sur le terrain.",
    "C. (3 pts) — Collaboratif : Les rôles sont relativement clairs. On se parle régulièrement pour ajuster. Ça fonctionne bien grâce aux relations interpersonnelles.",
    "D. (4 pts) — Systémique : On a un cadre de gouvernance écrit (qui fait quoi, qui décide quoi, qui finance quoi), partagé avec tous les partenaires, et une instance de coordination active."
]
q3_sel = st.sidebar.radio("Q3. Les rôles et responsabilités entre votre organisme, la Ville, le CIUSSS et les autres partenaires impliqués sont-ils clairs et documentés ?", opt_q3)
s3 = opt_q3.index(q3_sel) + 1

opt_q4 = [
    "A. (1 pt) — Réactif : Non, on n'a pas le temps de compiler des données. On se fie à notre « feeling » terrain.",
    "B. (2 pts) — Formel : On collecte quelques données (nombre de refus, incidents), mais on ne les analyse pas vraiment ni ne les partage.",
    "C. (3 pts) — Collaboratif : On suit des indicateurs de base (taux d'occupation, incidents, plaintes du voisinage) et on les présente en réunion d'équipe ou aux directions.",
    "D. (4 pts) — Systémique : On a un tableau de bord avec des indicateurs clairs (sécurité, propreté, satisfaction voisinage, taux de réintégration), analysés mensuellement, et partagés avec nos bailleurs de fonds/partenaires stratégiques."
]
q4_sel = st.sidebar.radio("Q4. Mesurez-vous l'impact de vos interventions de cohabitation (données, indicateurs, rapports) ?", opt_q4)
s4 = opt_q4.index(q4_sel) + 1

st.sidebar.markdown("---")
st.sidebar.markdown("### AXE B : OPÉRATIONS & TERRAIN")
st.sidebar.markdown("_« Comment on réagit concrètement aux situations de crise ? »_")

opt_q5 = [
    "A. (1 pt) — Réactif : On subit. On ne sait jamais quoi dire. Souvent, on ne dit rien et on espère que ça passe.",
    "B. (2 pts) — Formel : On réagit au cas par cas, souvent avec retard. On publie un communiqué générique qui satisfait rarement les gens.",
    "C. (3 pts) — Collaboratif : On a identifié un porte-parole interne. On prépare des messages-clés adaptés à la situation et on répond rapidement (dans les 24-48h).",
    "D. (4 pts) — Systémique : On a un plan de communication de crise documenté, avec des messages pré-approuvés, un protocole de gestion des médias sociaux, et une stratégie proactive (on communique AVANT que les problèmes n'explosent)."
]
q5_sel = st.sidebar.radio("Q5. Comment gérez-vous les crises médiatiques (vidéo virale, article négatif, pression des citoyen.ne.s sur les réseaux sociaux) ?", opt_q5)
s5 = opt_q5.index(q5_sel) + 1

opt_q6 = [
    "A. (1 pt) — Réactif : Non, on embauche des gens avec de l'expérience en intervention, mais on n'offre pas de formation spécifique sur la cohabitation avec le voisinage.",
    "B. (2 pts) — Formel : On a fait une formation ponctuelle lors de l'ouverture, mais rien de continu. Les nouvelles recrues apprennent « sur le tas ».",
    "C. (3 pts) — Collaboratif : On organise des formations internes régulières (désescalade, médiation, gestion des plaintes) et on fait des rétroactions d'incidents en équipe.",
    "D. (4 pts) — Systémique : Tou.te.s les intervenant.e.s reçoivent une formation structurée en cohabitation sociale (CPTED, réduction des risques, communication non-violente, gestion des comportements qui dérangent), avec des mises à jour annuelles et des supervisions cliniques régulières."
]
q6_sel = st.sidebar.radio("Q6. Vos équipes d’intervention sont-elles formées spécifiquement à la prévention et gestion de la cohabitation sociale (pas juste à l'intervention clinique) ?", opt_q6)
s6 = opt_q6.index(q6_sel) + 1

opt_q7 = [
    "A. (1 pt) — Réactif : On ne sort pas. On gère seulement ce qui se passe à l'intérieur. L'extérieur, ce n’est « pas notre problème ».",
    "B. (2 pts) — Formel : On sort parfois si un.e citoyen.ne se plaint, mais on n'a pas de protocole clair ni de ressources dédiées.",
    "C. (3 pts) — Collaboratif : On a des intervenant.e.s qui font des rondes régulières sur le parvis et aux abords immédiats (rayon de 10-20m). On nettoie quotidiennement.",
    "D. (4 pts) — Systémique : On gère activement une « zone tampon » de 50-100m autour de notre établissement : nettoyage structuré, présence visible, médiation proactive avec les personnes en situation d’itinérance et le voisinage."
]
q7_sel = st.sidebar.radio("Q7. Quelle est votre capacité à intervenir HORS de votre bâtiment (parvis, ruelle adjacente, parc à proximité, campement, etc.) ?", opt_q7)
s7 = opt_q7.index(q7_sel) + 1

opt_q8 = [
    "A. (1 pt) — Réactif : Non, les pauses de service sont décidées de façon arbitraire
