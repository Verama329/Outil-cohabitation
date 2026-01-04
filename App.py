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
            * **Chapitre 6** : Gouvernance et concertation (pour structurer vos partenariats externes)
            """
        }
    elif score <= 42:
        return {
            "nom": "PROFIL 3 : LE PARTENAIRE STRATÉGIQUE",
            "score_range": "Score : 34 à 42 points",
            "style": "p-blue",
            "realite": """
            **Vous êtes dans le peloton de tête.** Vous avez des protocoles solides, des partenariats actifs, et une relation constructive avec le voisinage. Votre organisme est reconnu comme un acteur de solutions, pas comme un « problème ». Mais vous sentez qu'il reste des angles morts, et vous voulez optimiser.
            """,
            "forces": """
            * Protocoles clairs et appliqués de façon cohérente
            * Partenariats structurés avec la Ville, les organismes pairs, et le voisinage
            * Capacité à gérer les crises sans panique
            * Certaines mesures d'impact documentées
            """,
            "risques": """
            * **Proactivité vs Réactivité** : Vous gérez bien les crises, mais pourriez-vous les anticiper davantage ?
            * **Mesure d'impact** : Vous collectez des données, mais les exploitez-vous stratégiquement pour influencer les politiques ou sécuriser du financement ?
            * **Innovation** : Pourriez-vous tester de nouvelles approches (médiation sociale dédiée, zone tampon élargie, co-construction avec les usagers) ?
            """,
            "action_titre": "→ Structurez votre tableau de bord d'impact et utilisez-le comme levier stratégique.",
            "action_details": """
            **Pourquoi ?**
            Parce que vous avez déjà l'essentiel en place. Ce qui vous manque, c'est la capacité à **démontrer** votre valeur ajoutée de manière chiffrée et à utiliser ces données pour :
            * Obtenir du financement additionnel
            * Influencer les décisions municipales
            * Inspirer d'autres organismes
            * Protéger votre réputation en cas de crise

            **Comment ?**
            → Allez lire le **Chapitre 8** de ce Guide : *Mesurer votre impact pour durer — Indicateurs et pérennité*.
            Vous y trouverez un cadre complet pour bâtir un tableau de bord d'impact adapté à la cohabitation sociale.

            **Temps requis :**
            4-6 semaines (identification des indicateurs clés, mise en place d'outils de collecte, formation de l'équipe, premier rapport d'impact).
            """,
            "chapitres": """
            **Priorité 1 (À lire maintenant) :**
            * **Chapitre 8** : Mesurer votre impact pour durer — Indicateurs de performance et pérennité des financements
            * **Chapitre 7** : Communication stratégique et gestion de crise

            **Priorité 2 (Pour aller encore plus loin) :**
            * **Chapitre 6** : Gouvernance et concertation
            * **Chapitre 2** : L'implantation stratégique et l'acceptabilité sociale
            """
        }
    else:
        return {
            "nom": "PROFIL 4 : L'INNOVATEUR SYSTÉMIQUE",
            "score_range": "Score : 43 à 48 points",
            "style": "p-green",
            "realite": """
            **Vous êtes une référence.** Votre organisme fonctionne comme une organisation apprenante : protocoles solides, partenariats stratégiques, mesure d'impact rigoureuse, communication proactive, implication citoyenne structurée. Vous ne gérez pas juste la cohabitation — vous la co-construisez.
            """,
            "forces": """
            * Approche préventive et anticipatrice (vous gérez les risques avant qu'ils ne deviennent des crises)
            * Partenariats multi-niveaux (Ville, CIUSSS, organismes pairs, citoyens, commerces)
            * Données probantes utilisées stratégiquement
            * Innovations terrain (médiation sociale dédiée, zone tampon active, co-construction avec les usagers)
            * Influence sur les politiques publiques locales
            """,
            "risques": """
            * **Pérennité** : Comment maintenir ce niveau d'excellence malgré les changements de financement, de personnel, ou de contexte politique ?
            * **Essaimage** : Comment transférer vos pratiques à d'autres organismes sans créer de dépendance ?
            * **Fatigue de l'excellence** : Votre équipe est-elle en risque de burnout à force de vouloir tout faire parfaitement ?
            """,
            "action_titre": "→ Documentez vos pratiques exemplaires et partagez-les (devenez une ressource pour le réseau).",
            "action_details": """
            **Pourquoi ?**
            Parce que vous avez atteint un niveau de maturité rare. Votre prochain levier n'est pas d'améliorer VOS pratiques, mais de **multiplier leur impact** en inspirant et en outillant d'autres organismes. Cela vous permettra de :
            * Renforcer votre légitimité auprès des bailleurs de fonds
            * Créer des alliances stratégiques avec d'autres acteurs
            * Contribuer à l'amélioration systémique du secteur
            * Valoriser votre équipe (reconnaissance externe)

            **Comment ?**
            → Allez lire le **Chapitre 8** (Mesurer votre impact) et la **Conclusion** de ce Guide pour structurer votre démarche de transfert de connaissances.
            Envisagez de publier des études de cas, d'offrir du mentorat ou de co-animer des formations.

            **Temps requis :**
            3-6 mois pour structurer une offre de transfert de connaissances.
            """,
            "chapitres": """
            **Priorité 1 (À lire pour consolider) :**
            * **Chapitre 8** : Mesurer votre impact pour durer
            * **Conclusion** : Vers un urbanisme du lien

            **Priorité 2 (Pour aller encore plus loin) :**
            * **Tous les chapitres** — Mais pas pour vous-même. Lisez-les en vous demandant : « Comment pourrais-je aider d'autres organismes à progresser sur ces dimensions ? »
            """
        }

# 5. SIDEBAR : LE QUESTIONNAIRE COMPLET (AVEC TEXTE INTÉGRAL)
scores = {}

with st.sidebar:
    st.header("QUESTIONNAIRE")
    st.info("Répondez aux 12 questions ci-dessous.")
    
    # AXE A
    st.markdown("### AXE A : GOUVERNANCE & PROTOCOLES")
    st.caption("« Est-ce que c'est écrit, clair et appliqué ? »")
    
    q1 = st.radio(
        "Q1. Votre organisme dispose-t-il d'un protocole écrit de gestion des comportements problématiques (violence, menaces, consommation ostentatoire) ?",
        [
            "A. (1 pt) — Réactif : Non, on gère au cas par cas selon l'intervenant de garde. Chacun a sa méthode.",
            "B. (2 pts) — Formel : Oui, on a un règlement interne affiché, mais il est rarement appliqué de façon cohérente (dépend de qui est de service).",
            "C. (3 pts) — Collaboratif : Oui, on a un protocole écrit et l'équipe le connaît. On fait des ajustements réguliers en réunion clinique.",
            "D. (4 pts) — Systémique : Oui, on a un protocole d'intervention graduée (niveaux vert-jaune-rouge), documenté, appliqué de façon cohérente, et révisé annuellement avec l'équipe."
        ]
    )
    scores["Q1"] = int(q1.split("pt")[0][-1])

    q2 = st.radio(
        "Q2. Avez-vous formalisé vos engagements avec le voisinage (pacte, entente, rencontres structurées) ?",
        [
            "A. (1 pt) — Réactif : Non, on réagit seulement quand il y a une plainte. On n'a pas de contact proactif avec les voisins.",
            "B. (2 pts) — Formel : On a eu une rencontre d'information lors de l'ouverture, mais rien de structuré depuis. Les citoyens appellent directement la Ville.",
            "C. (3 pts) — Collaboratif : On organise des rencontres périodiques (2-4 fois par année) avec un comité de citoyens. Le dialogue existe, mais ce n'est pas formalisé par écrit.",
            "D. (4 pts) — Systémique : On a signé un Pacte de bon voisinage écrit avec des engagements clairs de part et d'autre, des rencontres trimestrielles, et un mécanisme de résolution de conflits défini."
        ]
    )
    scores["Q2"] = int(q2.split("pt")[0][-1])

    q3 = st.radio(
        "Q3. Les rôles et responsabilités entre votre organisme, la Ville, le CIUSSS et les partenaires sont-ils clairs et documentés ?",
        [
            "A. (1 pt) — Réactif : Non, on ne sait pas toujours qui doit faire quoi. On se renvoie souvent la balle entre organismes.",
            "B. (2 pts) — Formel : On a des ententes de service signées, mais dans les faits, les zones grises créent de la confusion sur le terrain.",
            "C. (3 pts) — Collaboratif : Les rôles sont relativement clairs. On se parle régulièrement pour ajuster. Ça fonctionne bien grâce aux relations interpersonnelles.",
            "D. (4 pts) — Systémique : On a un cadre de gouvernance écrit (qui fait quoi, qui décide quoi, qui finance quoi), partagé avec tous les partenaires, et une instance de coordination active."
        ]
    )
    scores["Q3"] = int(q3.split("pt")[0][-1])

    q4 = st.radio(
        "Q4. Mesurez-vous l'impact de vos interventions de cohabitation (données, indicateurs, rapports) ?",
        [
            "A. (1 pt) — Réactif : Non, on n'a pas le temps de compiler des données. On se fie à notre « feeling » terrain.",
            "B. (2 pts) — Formel : On collecte quelques données (nombre de refus, incidents), mais on ne les analyse pas vraiment ni ne les partage.",
            "C. (3 pts) — Collaboratif : On suit des indicateurs de base (taux d'occupation, incidents, plaintes du voisinage) et on les présente en réunion d'équipe ou au CA.",
            "D. (4 pts) — Systémique : On a un tableau de bord avec des indicateurs clairs (sécurité, propreté, satisfaction voisinage, taux de réintégration), analysés mensuellement, et partagés avec nos bailleurs de fonds."
        ]
    )
    scores["Q4"] = int(q4.split("pt")[0][-1])

    st.markdown("---")
    # AXE B
    st.markdown("### AXE B : OPÉRATIONS & TERRAIN")
    st.caption("« Comment on réagit concrètement aux situations de crise ? »")

    q5 = st.radio(
        "Q5. Comment gérez-vous les crises médiatiques (vidéo virale, article négatif, pression des citoyens sur les réseaux sociaux) ?",
        [
            "A. (1 pt) — Réactif : On subit. On ne sait jamais quoi dire. Souvent, on ne dit rien et on espère que ça passe.",
            "B. (2 pts) — Formel : On réagit au cas par cas, souvent avec retard. On publie un communiqué générique qui satisfait rarement les gens.",
            "C. (3 pts) — Collaboratif : On a identifié un porte-parole interne. On prépare des messages-clés adaptés à la situation et on répond rapidement (dans les 24-48h).",
            "D. (4 pts) — Systémique : On a un plan de communication de crise documenté, avec des messages pré-approuvés, un protocole de gestion des médias sociaux, et une stratégie proactive."
        ]
    )
    scores["Q5"] = int(q5.split("pt")[0][-1])

    q6 = st.radio(
        "Q6. Vos intervenants sont-ils formés spécifiquement à la gestion de la cohabitation sociale (pas juste à l'intervention clinique) ?",
        [
            "A. (1 pt) — Réactif : Non, on embauche des gens avec de l'expérience en intervention, mais on n'offre pas de formation spécifique sur la cohabitation avec le voisinage.",
            "B. (2 pts) — Formel : On a fait une formation ponctuelle lors de l'ouverture, mais rien de continu. Les nouvelles recrues apprennent « sur le tas ».",
            "C. (3 pts) — Collaboratif : On organise des formations internes régulières (désescalade, médiation, gestion des plaintes) et on fait des débriefs d'incidents en équipe.",
            "D. (4 pts) — Systémique : Tous les intervenants reçoivent une formation structurée en cohabitation sociale (CPTED, réduction des méfaits, communication non-violente), avec des mises à jour annuelles."
        ]
    )
    scores["Q6"] = int(q6.split("pt")[0][-1])

    q7 = st.radio(
        "Q7. Quelle est votre capacité à intervenir HORS de votre bâtiment (parvis, ruelle adjacente, parc à proximité) ?",
        [
            "A. (1 pt) — Réactif : On ne sort pas. On gère seulement ce qui se passe à l'intérieur. L'extérieur, c'est « pas notre problème ».",
            "B. (2 pts) — Formel : On sort parfois si un citoyen se plaint, mais on n'a pas de protocole clair ni de ressources dédiées.",
            "C. (3 pts) — Collaboratif : On a des intervenants qui font des rondes régulières sur le parvis et aux abords immédiats (rayon de 10-20m). On nettoie quotidiennement.",
            "D. (4 pts) — Systémique : On gère activement une « zone tampon » de 50-100m autour de notre établissement : nettoyage structuré, présence visible, médiation proactive."
        ]
    )
    scores["Q7"] = int(q7.split("pt")[0][-1])

    q8 = st.radio(
        "Q8. Avez-vous un processus clair pour gérer les exclusions (barring) et les retours après exclusion ?",
        [
            "A. (1 pt) — Réactif : Non, les exclusions sont décidées de façon arbitraire selon l'humeur de l'intervenant. Pas de procédure de retour.",
            "B. (2 pts) — Formel : On exclut quand c'est grave, mais les durées varient beaucoup. Parfois les gens reviennent sans rencontre, parfois non.",
            "C. (3 pts) — Collaboratif : On a une grille d'exclusion selon la gravité (violence = X jours). Les retours nécessitent généralement une rencontre avec un intervenant.",
            "D. (4 pts) — Systémique : On a un protocole d'intervention graduée (vert-jaune-rouge) avec des durées d'exclusion proportionnées, des rencontres de retour obligatoires, et un suivi documenté."
        ]
    )
    scores["Q8"] = int(q8.split("pt")[0][-1])

    st.markdown("---")
    # AXE C
    st.markdown("### AXE C : ALLIANCES & PARTENARIATS")
    st.caption("« Travaille-t-on seul ou en réseau ? »")

    q9 = st.radio(
        "Q9. Quelle est la qualité de votre relation avec les services municipaux (police, 311, propreté, urbanisme) ?",
        [
            "A. (1 pt) — Réactif : On n'a presque pas de contact. Quand on se parle, c'est souvent tendu (ils nous voient comme « le problème »).",
            "B. (2 pts) — Formel : On se connaît de nom, on s'échange des courriels administratifs, mais il n'y a pas vraiment de collaboration terrain.",
            "C. (3 pts) — Collaboratif : On a des contacts réguliers et constructifs. On peut appeler le poste de quartier ou le responsable municipal quand il y a un enjeu.",
            "D. (4 pts) — Systémique : On siège à une table de concertation locale avec la Ville, la police communautaire, et d'autres partenaires. On co-construit des solutions."
        ]
    )
    scores["Q9"] = int(q9.split("pt")[0][-1])

    q10 = st.radio(
        "Q10. Collaborez-vous avec d'autres organismes du secteur (refuges, haltes, centres de jour, santé) pour gérer collectivement la cohabitation ?",
        [
            "A. (1 pt) — Réactif : Non, chacun gère son coin. On se voit comme des compétiteurs (pour le financement, pour les usagers).",
            "B. (2 pts) — Formel : On se parle occasionnellement, mais chacun reste dans son silo. On ne partage pas vraiment d'information ni de stratégie.",
            "C. (3 pts) — Collaboratif : On participe à une table de concertation locale. On échange sur les cas complexes et on se réfère mutuellement des usagers.",
            "D. (4 pts) — Systémique : On fait partie d'un réseau structuré avec des protocoles de collaboration clairs (partage d'info, stratégies communes de cohabitation)."
        ]
    )
    scores["Q10"] = int(q10.split("pt")[0][-1])

    q11 = st.radio(
        "Q11. Impliquez-vous les citoyens/voisins de manière constructive (au-delà de « gérer les plaintes ») ?",
        [
            "A. (1 pt) — Réactif : Non, on évite les citoyens. Quand ils appellent, on subit leurs reproches. On n'a pas de stratégie d'engagement.",
            "B. (2 pts) — Formel : On répond poliment aux plaintes, mais on ne cherche pas à créer une relation proactive avec le voisinage.",
            "C. (3 pts) — Collaboratif : On organise des rencontres de voisinage 2-3 fois par année. Les citoyens peuvent nous poser des questions et on explique notre mission.",
            "D. (4 pts) — Systémique : On a co-créé un Comité de bon voisinage avec des résidents volontaires. Ils participent à des activités et deviennent des « ambassadeurs »."
        ]
    )
    scores["Q11"] = int(q11.split("pt")[0][-1])

    q12 = st.radio(
        "Q12. Avez-vous accès à des ressources de médiation sociale ou de travail de proximité dédiées à la cohabitation ?",
        [
            "A. (1 pt) — Réactif : Non, nos intervenants font tout : clinique + gestion des plaintes + médiation. Ils sont débordés.",
            "B. (2 pts) — Formel : On aimerait avoir de la médiation, mais on n'a pas le budget. On se débrouille avec nos ressources internes.",
            "C. (3 pts) — Collaboratif : On a parfois accès à un médiateur externe (via la Ville ou un partenaire), mais ce n'est pas systématique ni financé de façon stable.",
            "D. (4 pts) — Systémique : On a un poste dédié (agent de milieu, médiateur social) financé spécifiquement pour gérer la zone tampon et les relations avec le voisinage."
        ]
    )
    scores["Q12"] = int(q12.split("pt")[0][-1])


# 6. CALCULS
total = sum(scores.values())
axe_a = scores["Q1"] + scores["Q2"] + scores["Q3"] + scores["Q4"]
axe_b = scores["Q5"] + scores["Q6"] + scores["Q7"] + scores["Q8"]
axe_c = scores["Q9"] + scores["Q10"] + scores["Q11"] + scores["Q12"]

content = get_profile_content(total)

# 7. AFFICHAGE DES RÉSULTATS

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📊 VOS RÉSULTATS")
    
    # Métriques
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("SCORE TOTAL", f"{total}/48")
    m2.metric("A. Gouvernance", f"{axe_a}/16")
    m3.metric("B. Terrain", f"{axe_b}/16")
    m4.metric("C. Alliances", f"{axe_c}/16")
    
    st.markdown("---")

    # BOITE PROFIL (Visuel fidèle)
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
    # Radar Chart
    categories = ['Gouvernance & Protocoles', 'Opérations & Terrain', 'Alliances & Partenariats']
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

# 8. ANALYSE DÉTAILLÉE (Sous le radar)
st.markdown("---")

c_forces, c_risques = st.columns(2)
with c_forces:
    st.markdown("#### ✅ VOS FORCES")
    st.markdown(content['forces'])

with c_risques:
    st.markdown("#### ⚠️ VOS RISQUES")
    st.markdown(content['risques'])

# 9. ACTION PRIORITAIRE (Boite spéciale)
st.markdown(f"""
<div class="action-box">
    <div class="action-title">🎯 VOTRE ACTION PRIORITAIRE (Low Hanging Fruit)</div>
    <div style="margin-top:10px;"><em>Ne tentez pas de tout refaire. Commencez par :</em></div>
    <h2 style="color:#c0392b; margin-top:5px;">{content['action_titre']}</h2>
    {content['action_details']}
</div>
""", unsafe_allow_html=True)

# 10. CHAPITRES RECOMMANDÉS
st.markdown("### 📖 CHAPITRES RECOMMANDÉS POUR VOUS")
st.markdown(content['chapitres'])

st.markdown("---")
st.caption("Outil généré pour le Guide de la Cohabitation Sociale.")
