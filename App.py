# -*- coding: utf-8 -*-
import streamlit as st
import plotly.graph_objects as go

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Radar Cohabitation", page_icon="🎯", layout="wide")

# 2. CSS PERSONNALISÉ (Pour le look "Document Officiel")
st.markdown("""
    <style>
    .main-header { font-size: 2.2rem; color: #2c3e50; font-weight: 700; margin-bottom: 0.5rem; }
    .sub-header { font-size: 1.2rem; color: #555; margin-bottom: 2rem; }
    
    /* Boites de résultats */
    .result-box { padding: 20px; border-radius: 10px; margin-bottom: 20px; border: 1px solid #ddd; }
    .profile-header { font-size: 1.5rem; font-weight: bold; margin-bottom: 10px; }
    
    /* Couleurs des profils */
    .p-red { background-color: #ffebee; border-left: 8px solid #ef5350; color: #000; }
    .p-orange { background-color: #fff3e0; border-left: 8px solid #ffa726; color: #000; }
    .p-blue { background-color: #e3f2fd; border-left: 8px solid #29b6f6; color: #000; }
    .p-green { background-color: #e8f5e9; border-left: 8px solid #66bb6a; color: #000; }

    /* Action Prioritaire */
    .action-box {
        background-color: #f4f6f9;
        padding: 25px;
        border-radius: 8px;
        border: 2px solid #34495e;
        margin-top: 25px;
    }
    .action-title { color: #c0392b; font-size: 1.4rem; font-weight: bold; }
    
    /* Texte général */
    p, li { line-height: 1.6; font-size: 1.05rem; }
    </style>
""", unsafe_allow_html=True)

# 3. EN-TÊTE & MODE D'EMPLOI (Visible avant de commencer)
st.markdown("<div class='main-header'>LE RADAR DE MATURITÉ EN COHABITATION</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Outil d'auto-diagnostic stratégique — 5 minutes pour savoir par où commencer</div>", unsafe_allow_html=True)

with st.expander("📖 MODE D'EMPLOI & CONSIGNES (À LIRE AVANT DE COMMENCER)", expanded=True):
    st.markdown("""
    **Cet outil n'est pas un examen. C'est une boussole.**
    
    Vous gérez un organisme, une ressource d'hébergement, une équipe d'intervention de proximité ou un service municipal en contact avec l'itinérance ? Vous faites déjà beaucoup avec peu. Ce diagnostic vous aide simplement à identifier votre prochain levier d'amélioration — celui qui aura le plus d'impact avec le moins d'effort.

    * **Temps requis :** 5 minutes
    * **Format :** 12 questions, 4 choix de réponse par question
    * **Résultat :** Votre profil de maturité + vos actions prioritaires

    ---
    **CONSIGNE :** Pour chaque question, choisissez **la réponse qui reflète le mieux votre réalité actuelle** (pas ce que vous aimeriez avoir, mais ce qui existe vraiment aujourd'hui).
    """)

# 4. CONTENU INTÉGRAL DU DOCUMENT (Base de données)
# J'utilise des triples guillemets pour éviter les erreurs de syntaxe

def get_profile_content(score):
    if score <= 24:
        return {
            "nom": "PROFIL 1 : LE POMPIER SOLITAIRE",
            "score_range": "Score : 12 à 24 points",
            "style": "p-red",
            "realite": """
            **Vous êtes en mode survie.** Votre équipe gère au jour le jour, sans protocoles formalisés, avec peu ou pas de collaboration structurée avec le voisinage ou les partenaires externes. Les crises éclatent, vous réagissez, et vous recommencez le lendemain.
            """,
            "forces": """
            * Vous êtes sur le terrain, proche des usagers
            * Vous faites preuve de résilience et d'adaptation constante
            * Vous connaissez intimement les réalités de votre clientèle
            """,
            "risques": """
            * **Épuisement de l'équipe** : Tout repose sur quelques personnes clés. Le turnover est élevé.
            * **Incohérence** : Chaque intervenant gère les situations à sa façon. Pas de prévisibilité.
            * **Vulnérabilité médiatique** : Une vidéo virale, un article négatif, et vous n'avez aucun filet de sécurité.
            * **Isolement** : Vous êtes perçu comme « le problème » par le voisinage et la Ville, plutôt que comme un partenaire.
            """,
            "action_titre": "→ Créez votre premier protocole d'intervention écrit (comportements qui dérangent).",
            "action_details": """
            **Ne tentez pas de tout refaire. Commencez par UNE SEULE CHOSE.**

            **Pourquoi ?**
            Parce que c'est le fondement de tout. Tant que vos intervenants n'ont pas un cadre clair et partagé, vous resterez en mode réactif. Ce protocole vous permettra de :
            * Réduire l'arbitraire (et donc les frustrations internes)
            * Avoir une réponse cohérente à donner aux citoyens qui se plaignent
            * Protéger juridiquement votre organisme en cas de litige

            **Comment ?**
            → Allez lire le **Chapitre 3** de ce Guide : *Principes d'intervention et gestion quotidienne de la cohabitation sociale*.
            Vous y trouverez un modèle de protocole de gestion des comportements qui dérangent (vert-jaune-rouge) prêt à adapter.

            **Temps requis :**
            2-3 réunions d'équipe pour co-créer le protocole, puis formation de 2 heures pour l'implanter.
            """,
            "chapitres": """
            **Priorité 1 (À lire maintenant) :**
            * **Chapitre 3** : Principes d'intervention et gestion quotidienne de la cohabitation sociale

            **Priorité 2 (Dans les 3-6 prochains mois) :**
            * **Chapitre 1** : Comprendre l'écosystème et la gouvernance (pour clarifier qui fait quoi)
            * **Chapitre 6** : Gouvernance et concertation (pour structurer vos partenariats de base)
            """
        }
    elif score <= 33:
        return {
            "nom": "PROFIL 2 : LE GESTIONNAIRE STRUCTURÉ",
            "score_range": "Score : 25 à 33 points",
            "style": "p-orange",
            "realite": """
            **Vous avez posé des bases solides.** Vous avez des protocoles écrits, des règles claires, et une certaine organisation interne. Mais l'application reste inégale, les partenariats sont informels, et vous sentez que votre approche pourrait être plus fluide et collaborative.
            """,
            "forces": """
            * Vous avez des outils et des procédures (règlements, protocoles de base)
            * Votre équipe connaît les attentes minimales
            * Vous documentez certaines de vos interventions
            """,
            "risques": """
            * **Rigidité** : Vos protocoles existent, mais ils sont appliqués de façon mécanique. Peu de place pour l'adaptation ou la désescalade créative.
            * **Relations tendues avec le voisinage** : Vous gérez les plaintes, mais vous n'avez pas vraiment construit de lien de confiance avec les citoyens.
            * **Silos** : Vous fonctionnez en vase clos. Les partenariats sont limités ou ponctuels.
            * **Communication défensive** : En cas de crise médiatique, vous réagissez, mais vous ne maîtrisez pas la narration.
            """,
            "action_titre": "→ Formalisez vos relations avec le voisinage (créez votre premier Pacte de bon voisinage).",
            "action_details": """
            **Pourquoi ?**
            Parce que vous avez déjà la structure interne. Ce qui vous manque, c'est le pont vers l'externe. Un Pacte de bon voisinage transforme les plaintes récurrentes en dialogue structuré, et les citoyens méfiants en alliés potentiels.

            **Comment ?**
            → Allez lire le **Chapitre 4** de ce Guide : *Le rôle des citoyen.ne.s et du voisinage : de la plainte à la collaboration*.
            Vous y trouverez un modèle complet de Pacte de bon voisinage (clause par clause) prêt à adapter.

            **Temps requis :**
            4-6 semaines (identification des parties prenantes, rédaction collaborative du pacte, signature formelle, première rencontre de suivi).
            """,
            "chapitres": """
            **Priorité 1 (À lire maintenant) :**
            * **Chapitre 4** : Le rôle du citoyen et du voisinage — De la plainte à la collaboration
            * **Chapitre 4 et 5** : Outils à développer (Pacte de bon voisinage, aide-mémoire Qui appeler et quand ?)

            **Priorité 2 (Dans les 3-6 prochains mois) :**
            * **Chapitre 7** : Communication stratégique et gestion de crise (pour sortir du mode défensif)
            * **Chapitre 6**
