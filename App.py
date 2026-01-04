# app.py
# Streamlit web app Ñ Le Radar de MaturitŽ en Cohabitation
# Run: streamlit run app.py
#
# Dependencies:
#   pip install streamlit plotly reportlab

from __future__ import annotations

from dataclasses import dataclass
from io import BytesIO
from typing import Dict, List, Tuple

import plotly.graph_objects as go
import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas


# -----------------------------
# DonnŽes (questionnaire + profils)
# -----------------------------
@dataclass(frozen=True)
class Option:
    code: str  # "A".."D"
    points: int  # 1..4
    niveau: str  # "RŽactif".."SystŽmique"
    texte: str   # texte descriptif complet

@dataclass(frozen=True)
class Question:
    id: str      # "Q1".."Q12"
    axe: str     # "A", "B", "C"
    titre_axe: str
    question: str
    options: List[Option]

@dataclass(frozen=True)
class Profil:
    min_score: int
    max_score: int
    nom: str
    realite: str
    action: str
    chapitres: str


AXE_META = {
    "A": ("Gouvernance & Protocoles", "Ç Est-ce que c'est Žcrit, clair et appliquŽ ? È"),
    "B": ("OpŽrations & Terrain", "Ç Comment on rŽagit concrtement aux situations de crise ? È"),
    "C": ("Alliances & Partenariats", "Ç Travaille-t-on seul ou en rŽseau ? È"),
}

QUESTIONS: List[Question] = [
    Question(
        id="Q1",
        axe="A",
        titre_axe=AXE_META["A"][0],
        question="Votre organisme dispose-t-il d'un protocole Žcrit de gestion des comportements problŽmatiques (violence, menaces, consommation ostentatoire) ?",
        options=[
            Option("A", 1, "RŽactif", "Non, on gre au cas par cas selon l'intervenant de garde. Chacun a sa mŽthode."),
            Option("B", 2, "Formel", "Oui, on a un rglement interne affichŽ, mais il est rarement appliquŽ de faon cohŽrente (dŽpend de qui est de service)."),
            Option("C", 3, "Collaboratif", "Oui, on a un protocole Žcrit et l'Žquipe le conna”t. On fait des ajustements rŽguliers en rŽunion clinique."),
            Option("D", 4, "SystŽmique", "Oui, on a un protocole d'intervention graduŽe (niveaux vert-jaune-rouge), documentŽ, appliquŽ de faon cohŽrente, et rŽvisŽ annuellement avec l'Žquipe."),
        ],
    ),
    Question(
        id="Q2",
        axe="A",
        titre_axe=AXE_META["A"][0],
        question="Avez-vous formalisŽ vos engagements avec le voisinage (pacte, entente, rencontres structurŽes) ?",
        options=[
            Option("A", 1, "RŽactif", "Non, on rŽagit seulement quand il y a une plainte. On n'a pas de contact proactif avec les voisins."),
            Option("B", 2, "Formel", "On a eu une rencontre d'information lors de l'ouverture, mais rien de structurŽ depuis. Les citoyens appellent directement la Ville quand ils sont insatisfaits."),
            Option("C", 3, "Collaboratif", "On organise des rencontres pŽriodiques (2-4 fois par annŽe) avec un comitŽ de citoyens. Le dialogue existe, mais ce n'est pas formalisŽ par Žcrit."),
            Option("D", 4, "SystŽmique", "On a signŽ un Pacte de bon voisinage Žcrit avec des engagements clairs de part et d'autre, des rencontres trimestrielles, et un mŽcanisme de rŽsolution de conflits dŽfini."),
        ],
    ),
    Question(
        id="Q3",
        axe="A",
        titre_axe=AXE_META["A"][0],
        question="Les r™les et responsabilitŽs entre votre organisme, la Ville, le CIUSSS et les partenaires sont-ils clairs et documentŽs ?",
        options=[
            Option("A", 1, "RŽactif", "Non, on ne sait pas toujours qui doit faire quoi. On se renvoie souvent la balle entre organismes."),
            Option("B", 2, "Formel", "On a des ententes de service signŽes, mais dans les faits, les zones grises crŽent de la confusion sur le terrain."),
            Option("C", 3, "Collaboratif", "Les r™les sont relativement clairs. On se parle rŽgulirement pour ajuster. ‚a fonctionne bien gr‰ce aux relations interpersonnelles."),
            Option("D", 4, "SystŽmique", "On a un cadre de gouvernance Žcrit (qui fait quoi, qui dŽcide quoi, qui finance quoi), partagŽ avec tous les partenaires, et une instance de coordination active."),
        ],
    ),
    Question(
        id="Q4",
        axe="A",
        titre_axe=AXE_META["A"][0],
        question="Mesurez-vous l'impact de vos interventions de cohabitation (donnŽes, indicateurs, rapports) ?",
        options=[
            Option("A", 1, "RŽactif", "Non, on n'a pas le temps de compiler des donnŽes. On se fie ˆ notre Ç feeling È terrain."),
            Option("B", 2, "Formel", "On collecte quelques donnŽes (nombre de refus, incidents), mais on ne les analyse pas vraiment ni ne les partage."),
            Option("C", 3, "Collaboratif", "On suit des indicateurs de base (taux d'occupation, incidents, plaintes du voisinage) et on les prŽsente en rŽunion d'Žquipe ou au CA."),
            Option("D", 4, "SystŽmique", "On a un tableau de bord avec des indicateurs clairs (sŽcuritŽ, propretŽ, satisfaction voisinage, taux de rŽintŽgration), analysŽs mensuellement, et partagŽs avec nos bailleurs de fonds."),
        ],
    ),
    Question(
        id="Q5",
        axe="B",
        titre_axe=AXE_META["B"][0],
        question="Comment gŽrez-vous les crises mŽdiatiques (vidŽo virale, article nŽgatif, pression des citoyens sur les rŽseaux sociaux) ?",
        options=[
            Option("A", 1, "RŽactif", "On subit. On ne sait jamais quoi dire. Souvent, on ne dit rien et on espre que a passe."),
            Option("B", 2, "Formel", "On rŽagit au cas par cas, souvent avec retard. On publie un communiquŽ gŽnŽrique qui satisfait rarement les gens."),
            Option("C", 3, "Collaboratif", "On a identifiŽ un porte-parole interne. On prŽpare des messages-clŽs adaptŽs ˆ la situation et on rŽpond rapidement (dans les 24-48h)."),
            Option("D", 4, "SystŽmique", "On a un plan de communication de crise documentŽ, avec des messages prŽ-approuvŽs, un protocole de gestion des mŽdias sociaux, et une stratŽgie proactive (on communique AVANT que les problmes n'explosent)."),
        ],
    ),
    Question(
        id="Q6",
        axe="B",
        titre_axe=AXE_META["B"][0],
        question="Vos intervenants sont-ils formŽs spŽcifiquement ˆ la gestion de la cohabitation sociale (pas juste ˆ l'intervention clinique) ?",
        options=[
            Option("A", 1, "RŽactif", "Non, on embauche des gens avec de l'expŽrience en intervention, mais on n'offre pas de formation spŽcifique sur la cohabitation avec le voisinage."),
            Option("B", 2, "Formel", "On a fait une formation ponctuelle lors de l'ouverture, mais rien de continu. Les nouvelles recrues apprennent Ç sur le tas È."),
            Option("C", 3, "Collaboratif", "On organise des formations internes rŽgulires (dŽsescalade, mŽdiation, gestion des plaintes) et on fait des dŽbriefs d'incidents en Žquipe."),
            Option("D", 4, "SystŽmique", "Tous les intervenants reoivent une formation structurŽe en cohabitation sociale (CPTED, rŽduction des mŽfaits, communication non-violente), avec des mises ˆ jour annuelles et des supervisions cliniques rŽgulires."),
        ],
    ),
    Question(
        id="Q7",
        axe="B",
        titre_axe=AXE_META["B"][0],
        question="Quelle est votre capacitŽ ˆ intervenir HORS de votre b‰timent (parvis, ruelle adjacente, parc ˆ proximitŽ) ?",
        options=[
            Option("A", 1, "RŽactif", "On ne sort pas. On gre seulement ce qui se passe ˆ l'intŽrieur. L'extŽrieur, c'est Ç pas notre problme È."),
            Option("B", 2, "Formel", "On sort parfois si un citoyen se plaint, mais on n'a pas de protocole clair ni de ressources dŽdiŽes."),
            Option("C", 3, "Collaboratif", "On a des intervenants qui font des rondes rŽgulires sur le parvis et aux abords immŽdiats (rayon de 10-20m). On nettoie quotidiennement."),
            Option("D", 4, "SystŽmique", "On gre activement une Ç zone tampon È de 50-100m autour de notre Žtablissement : nettoyage structurŽ, prŽsence visible, mŽdiation proactive avec les usagers et le voisinage."),
        ],
    ),
    Question(
        id="Q8",
        axe="B",
        titre_axe=AXE_META["B"][0],
        question="Avez-vous un processus clair pour gŽrer les exclusions (barring) et les retours aprs exclusion ?",
        options=[
            Option("A", 1, "RŽactif", "Non, les exclusions sont dŽcidŽes de faon arbitraire selon l'humeur de l'intervenant. Pas de procŽdure de retour."),
            Option("B", 2, "Formel", "On exclut quand c'est grave, mais les durŽes varient beaucoup. Parfois les gens reviennent sans rencontre, parfois non."),
            Option("C", 3, "Collaboratif", "On a une grille d'exclusion selon la gravitŽ (violence = X jours). Les retours nŽcessitent gŽnŽralement une rencontre avec un intervenant."),
            Option("D", 4, "SystŽmique", "On a un protocole d'intervention graduŽe (vert-jaune-rouge) avec des durŽes d'exclusion proportionnŽes, des rencontres de retour obligatoires, et un suivi documentŽ dans le dossier clinique."),
        ],
    ),
    Question(
        id="Q9",
        axe="C",
        titre_axe=AXE_META["C"][0],
        question="Quelle est la qualitŽ de votre relation avec les services municipaux (police, 311, propretŽ, urbanisme) ?",
        options=[
            Option("A", 1, "RŽactif", "On n'a presque pas de contact. Quand on se parle, c'est souvent tendu (ils nous voient comme Ç le problme È)."),
            Option("B", 2, "Formel", "On se conna”t de nom, on s'Žchange des courriels administratifs, mais il n'y a pas vraiment de collaboration terrain."),
            Option("C", 3, "Collaboratif", "On a des contacts rŽguliers et constructifs. On peut appeler le poste de quartier ou le responsable municipal quand il y a un enjeu."),
            Option("D", 4, "SystŽmique", "On sige ˆ une table de concertation locale avec la Ville, la police communautaire, et d'autres partenaires. On co-construit des solutions et on partage des donnŽes."),
        ],
    ),
    Question(
        id="Q10",
        axe="C",
        titre_axe=AXE_META["C"][0],
        question="Collaborez-vous avec d'autres organismes du secteur (refuges, haltes, centres de jour, santŽ) pour gŽrer collectivement la cohabitation ?",
        options=[
            Option("A", 1, "RŽactif", "Non, chacun gre son coin. On se voit comme des compŽtiteurs (pour le financement, pour les usagers)."),
            Option("B", 2, "Formel", "On se parle occasionnellement, mais chacun reste dans son silo. On ne partage pas vraiment d'information ni de stratŽgie."),
            Option("C", 3, "Collaboratif", "On participe ˆ une table de concertation locale. On Žchange sur les cas complexes et on se rŽfre mutuellement des usagers."),
            Option("D", 4, "SystŽmique", "On fait partie d'un rŽseau structurŽ avec des protocoles de collaboration clairs (partage d'info, gestion des exclusions croisŽes, stratŽgies communes de cohabitation, financement partagŽ pour mŽdiation sociale)."),
        ],
    ),
    Question(
        id="Q11",
        axe="C",
        titre_axe=AXE_META["C"][0],
        question="Impliquez-vous les citoyens/voisins de manire constructive (au-delˆ de Ç gŽrer les plaintes È) ?",
        options=[
            Option("A", 1, "RŽactif", "Non, on Žvite les citoyens. Quand ils appellent, on subit leurs reproches. On n'a pas de stratŽgie d'engagement."),
            Option("B", 2, "Formel", "On rŽpond poliment aux plaintes, mais on ne cherche pas ˆ crŽer une relation proactive avec le voisinage."),
            Option("C", 3, "Collaboratif", "On organise des rencontres de voisinage 2-3 fois par annŽe. Les citoyens peuvent nous poser des questions et on explique notre mission."),
            Option("D", 4, "SystŽmique", "On a co-crŽŽ un ComitŽ de bon voisinage avec des rŽsidents volontaires. Ils participent ˆ des activitŽs (nettoyage collectif, 5 ˆ 7, portes ouvertes) et deviennent des Ç ambassadeurs È de la cohabitation."),
        ],
    ),
    Question(
        id="Q12",
        axe="C",
        titre_axe=AXE_META["C"][0],
        question="Avez-vous accs ˆ des ressources de mŽdiation sociale ou de travail de proximitŽ dŽdiŽes ˆ la cohabitation (pas juste ˆ l'intervention clinique) ?",
        options=[
            Option("A", 1, "RŽactif", "Non, nos intervenants font tout : clinique + gestion des plaintes + mŽdiation. Ils sont dŽbordŽs."),
            Option("B", 2, "Formel", "On aimerait avoir de la mŽdiation, mais on n'a pas le budget. On se dŽbrouille avec nos ressources internes."),
            Option("C", 3, "Collaboratif", "On a parfois accs ˆ un mŽdiateur externe (via la Ville ou un partenaire), mais ce n'est pas systŽmatique ni financŽ de faon stable."),
            Option("D", 4, "SystŽmique", "On a un poste dŽdiŽ (agent de milieu, mŽdiateur social, intervenant de proximitŽ) financŽ spŽcifiquement pour gŽrer la zone tampon et les relations avec le voisinage. C'est distinct de l'intervention clinique."),
        ],
    ),
]

PROFILS: List[Profil] = [
    Profil(
        12, 24, "Le Pompier Solitaire",
        "Vous tes en mode survie. Votre Žquipe gre au jour le jour, sans protocoles formalisŽs, avec peu ou pas de collaboration structurŽe avec le voisinage ou les partenaires externes. Les crises Žclatent, vous rŽagissez, et vous recommencez le lendemain.\n\n"
        "Forces : proximitŽ terrain, rŽsilience, connaissance fine des usagers.\n"
        "Risques : Žpuisement, incohŽrence, vulnŽrabilitŽ mŽdiatique, isolement institutionnel.",
        "Commencez par UNE chose : crŽer votre premier protocole d'intervention Žcrit (comportements problŽmatiques). "
        "Objectif : rŽduire l'arbitraire, amŽliorer la cohŽrence, protŽger l'organisme et faciliter la rŽponse aux plaintes.",
        "PrioritŽ 1 : Chapitre 3.\nPrioritŽ 2 : Chapitre 1 et Chapitre 6."
    ),
    Profil(
        25, 33, "Le Gestionnaire StructurŽ",
        "Vous avez des bases solides (protocoles, rgles, organisation), mais l'application varie et les partenariats demeurent informels. "
        "Vous gŽrez les plaintes plus que vous ne construisez une relation de confiance.",
        "Formalisez vos relations avec le voisinage : crŽez un Pacte de bon voisinage (engagements, mŽcanisme de rŽsolution, rencontres).",
        "PrioritŽ 1 : Chapitre 4 et Chapitre 5.\nPrioritŽ 2 : Chapitre 7 et Chapitre 6."
    ),
    Profil(
        34, 42, "Le Partenaire StratŽgique",
        "Vous avez des protocoles solides, des partenariats actifs et une relation constructive avec le voisinage. "
        "Vous tes reconnu comme un acteur de solutions, mais souhaitez optimiser (proactivitŽ, mesure dÕimpact, innovation).",
        "Structurez un tableau de bord d'impact et utilisez-le comme levier (financement, influence, rŽputation, apprentissage).",
        "PrioritŽ 1 : Chapitre 8 et Chapitre 7.\nPrioritŽ 2 : Chapitre 6 et Chapitre 2."
    ),
    Profil(
        43, 48, "LÕInnovateur SystŽmique",
        "Vous tes une rŽfŽrence : protocoles, partenariats stratŽgiques, mesure dÕimpact, communication proactive, implication citoyenne structurŽe. "
        "Vous co-construisez la cohabitation ˆ lÕŽchelle du systme.",
        "Documentez vos pratiques et partagez-les (essaimage, mentorat, outils, Žtudes de cas). Votre levier : multiplier lÕimpact.",
        "PrioritŽ 1 : Chapitre 8 et Conclusion.\nPrioritŽ 2 : lecture transversale orientŽe transfert de pratiques."
    ),
]


# -----------------------------
# Fonctions mŽtier
# -----------------------------
def option_label(opt: Option) -> str:
    # Ultra explicite : on affiche A/B/C/D + points + niveau + description
    return f"{opt.code}. ({opt.points} pt) Ñ {opt.niveau}\n? {opt.texte}"

def compute_scores(answers: Dict[str, str]) -> Tuple[int, Dict[str, int]]:
    # answers: {"Q1": "A", ...}
    per_axis = {"A": 0, "B": 0, "C": 0}
    total = 0
    for q in QUESTIONS:
        code = answers.get(q.id, "")
        if not code:
            continue
        opt = next(o for o in q.options if o.code == code)
        total += opt.points
        per_axis[q.axe] += opt.points
    return total, per_axis

def resolve_profile(total_score: int) -> Profil | None:
    if total_score <= 0:
        return None
    for p in PROFILS:
        if p.min_score <= total_score <= p.max_score:
            return p
    # sŽcuritŽ (si jamais score partiel en dessous de 12)
    return None

def make_radar(per_axis: Dict[str, int]) -> go.Figure:
    labels = [
        "Gouvernance & Protocoles",
        "OpŽrations & Terrain",
        "Alliances & Partenariats",
    ]
    values = [per_axis["A"], per_axis["B"], per_axis["C"]]
    # fermer la boucle
    labels_closed = labels + [labels[0]]
    values_closed = values + [values[0]]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values_closed,
        theta=labels_closed,
        fill="toself",
        name="Score par axe",
        hovertemplate="%{theta}<br>Score: %{r}/16<extra></extra>",
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 16], tick0=0, dtick=4)
        ),
        showlegend=False,
        margin=dict(l=30, r=30, t=30, b=30),
        height=420,
    )
    return fig

def pdf_report_bytes(
    answers: Dict[str, str],
    total: int,
    per_axis: Dict[str, int],
    profile: Profil | None,
) -> bytes:
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    width, height = A4

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(2*cm, height - 2.2*cm, "Le Radar de MaturitŽ en Cohabitation Ñ Rapport")
    c.setFont("Helvetica", 10)
    c.drawString(2*cm, height - 2.9*cm, "Auto-diagnostic stratŽgique (rŽsumŽ)")

    # Scores
    y = height - 4.1*cm
    c.setFont("Helvetica-Bold", 12)
    c.drawString(2*cm, y, f"Score total : {total} / 48")
    y -= 0.8*cm
    c.setFont("Helvetica", 11)
    c.drawString(2*cm, y, f"Axe A (Gouvernance & Protocoles) : {per_axis['A']} / 16")
    y -= 0.6*cm
    c.drawString(2*cm, y, f"Axe B (OpŽrations & Terrain) : {per_axis['B']} / 16")
    y -= 0.6*cm
    c.drawString(2*cm, y, f"Axe C (Alliances & Partenariats) : {per_axis['C']} / 16")

    # Profil
    y -= 1.2*cm
    c.setFont("Helvetica-Bold", 12)
    if profile:
        c.drawString(2*cm, y, f"Profil : {profile.nom} ({profile.min_score}Ð{profile.max_score})")
    else:
        c.drawString(2*cm, y, "Profil : (score insuffisant ou questionnaire incomplet)")

    def draw_paragraph(title: str, text: str, y: float) -> float:
        c.setFont("Helvetica-Bold", 11)
        c.drawString(2*cm, y, title)
        y -= 0.55*cm
        c.setFont("Helvetica", 10)

        # wrap simple
        max_width = width - 4*cm
        words = text.replace("\n", " ").split()
        line = ""
        for w in words:
            candidate = (line + " " + w).strip()
            if c.stringWidth(candidate, "Helvetica", 10) <= max_width:
                line = candidate
            else:
                c.drawString(2*cm, y, line)
                y -= 0.45*cm
                line = w
                if y < 3*cm:
                    c.showPage()
                    y = height - 2.5*cm
                    c.setFont("Helvetica", 10)
        if line:
            c.drawString(2*cm, y, line)
            y -= 0.65*cm
        return y

    if profile:
        y -= 0.8*cm
        y = draw_paragraph("Votre rŽalitŽ (synthse)", profile.realite, y)
        y = draw_paragraph("Action prioritaire", profile.action, y)
        y = draw_paragraph("Chapitres recommandŽs", profile.chapitres, y)

    # RŽponses
    y -= 0.2*cm
    c.setFont("Helvetica-Bold", 11)
    c.drawString(2*cm, y, "Vos rŽponses (AÐD)")
    y -= 0.6*cm
    c.setFont("Helvetica", 10)
    for q in QUESTIONS:
        code = answers.get(q.id, "Ñ")
        line = f"{q.id} : {code}"
        c.drawString(2*cm, y, line)
        y -= 0.42*cm
        if y < 2.2*cm:
            c.showPage()
            y = height - 2.5*cm
            c.setFont("Helvetica", 10)

    c.showPage()
    c.save()
    return buf.getvalue()


# -----------------------------
# UI Streamlit
# -----------------------------
st.set_page_config(page_title="Radar de MaturitŽ Ñ Cohabitation", layout="wide")

st.title("Le Radar de MaturitŽ en Cohabitation")
st.caption("Outil d'auto-diagnostic stratŽgique Ñ 5 minutes pour savoir par o commencer")

with st.expander("Mode d'emploi (ˆ lire une fois)", expanded=False):
    st.markdown(
        """
**Cet outil n'est pas un examen. C'est une boussole.**  
Choisissez, pour chaque question, la rŽponse qui reflte le mieux votre rŽalitŽ actuelle (pas l'idŽal).  
RŽsultat : score total /48, score par axe /16, profil + action prioritaire + lectures recommandŽes.
        """.strip()
    )

# Init state
if "answers" not in st.session_state:
    st.session_state["answers"] = {q.id: "A" for q in QUESTIONS}  # dŽfaut (modifiable)

answers: Dict[str, str] = st.session_state["answers"]

# Sidebar (12 questions radio ultra explicites)
st.sidebar.header("Questionnaire (12 questions)")
st.sidebar.caption("Choisissez A, B, C ou D pour chaque question (texte complet inclus).")

current_axis = None
for q in QUESTIONS:
    if q.axe != current_axis:
        current_axis = q.axe
        st.sidebar.markdown("---")
        st.sidebar.subheader(f"Axe {q.axe} Ñ {AXE_META[q.axe][0]}")
        st.sidebar.caption(AXE_META[q.axe][1])

    labels = [option_label(o) for o in q.options]
    default_index = ["A", "B", "C", "D"].index(answers.get(q.id, "A"))
    selected_label = st.sidebar.radio(
        label=f"{q.id}. {q.question}",
        options=labels,
        index=default_index,
        key=f"radio_{q.id}",
    )
    # Convert label back to code
    selected_code = selected_label.split(".")[0].strip()  # "A"
    answers[q.id] = selected_code

st.session_state["answers"] = answers

# Compute
total, per_axis = compute_scores(answers)
profile = resolve_profile(total)

# Main layout
col_left, col_right = st.columns([1.05, 1.25], gap="large")

with col_left:
    st.subheader("Scores (mise ˆ jour en temps rŽel)")
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Total", f"{total} / 48")
    k2.metric("Axe A", f"{per_axis['A']} / 16")
    k3.metric("Axe B", f"{per_axis['B']} / 16")
    k4.metric("Axe C", f"{per_axis['C']} / 16")

    weakest_axis = min(per_axis.items(), key=lambda kv: kv[1])[0]
    st.info(f"**Axe ˆ prioriser (score le plus faible)** : Axe {weakest_axis} Ñ {AXE_META[weakest_axis][0]}")

    st.subheader("Graphique Radar")
    st.plotly_chart(make_radar(per_axis), use_container_width=True)

with col_right:
    st.subheader("RŽsultats")
    if profile is None:
        st.warning(
            "Le profil sÕaffiche pleinement quand le score total est dans les plages 12Ð48. "
            "Si vous souhaitez autoriser lÕaffichage ds un score partiel, on peut ajuster la rgle."
        )
    else:
        st.success(f"**Votre profil : {profile.nom}** (score {profile.min_score}Ð{profile.max_score})")

        st.markdown("### ?? Votre rŽalitŽ (synthse)")
        st.write(profile.realite)

        st.markdown("### ?? Action prioritaire (Low Hanging Fruit)")
        st.write(profile.action)

        st.markdown("### ?? Chapitres recommandŽs")
        st.write(profile.chapitres)

    st.markdown("---")
    st.subheader("TŽlŽcharger mon rapport (PDF)")
    st.caption("GŽnre un PDF rŽcapitulatif : scores, profil, action, lectures, et vos rŽponses.")

    pdf_bytes = pdf_report_bytes(answers, total, per_axis, profile)
    st.download_button(
        label="?? TŽlŽcharger mon rapport PDF",
        data=pdf_bytes,
        file_name="Rapport_Radar_Cohabitation.pdf",
        mime="application/pdf",
        use_container_width=True,
    )

st.markdown("---")
st.caption("Note : Les points sont calculŽs selon A=1, B=2, C=3, D=4. Score max : 48. Axes : 4 questions par axe, max 16.")
