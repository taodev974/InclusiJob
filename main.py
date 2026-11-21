from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Offre(BaseModel):
    texte: str


@app.get("/")
def root():
    return {
        "message": "Bonjour Tony"
    }

@app.post("/analyse")
def analyse(offre: Offre):

    texte = offre.texte.lower()

    score = 100
    problemes = []
    suggestions = []
    criteres = []

    for critere, details in CRITERES.items():
        if critere in texte:
            score -= details["malus"]
            problemes.append(details["probleme"])
            suggestions.append(details["suggestion"])
            criteres.append(critere)

    return {
        "score": score,
        "problemes": problemes,
        "suggestions": suggestions,
        "criteres": criteres,
    }

    

CRITERES = {
    "jeune équipe dynamique": {
        "malus": 10,
        "probleme": "Expression potentiellement discriminante",
        "suggestion": "Privilégier une description centrée sur les compétences"
    },

    "disponible immédiatement": {
        "malus": 10,
        "probleme": "Critère d'urgence pouvant exclure certains candidats",
        "suggestion": "Éviter les contraintes de disponibilité non essentielles"
    },

    "sous pression": {
    "malus": 10,
    "probleme": "Peut banaliser des conditions de travail génératrices de stress",
    "suggestion": "Préciser les situations exigeantes et les moyens mis en place pour accompagner les collaborateurs"
    },

    "homme": {
        "malus": 10,
        "probleme": "Formulation genrée pouvant exclure certains candidats",
        "suggestion": "Utiliser une formulation neutre et inclusive"
    },

    "femme": {
        "malus": 10,
        "probleme": "Formulation genrée pouvant exclure certains candidats",
        "suggestion": "Utiliser une formulation neutre et inclusive"
    },

    "jeune diplômé": {
        "malus": 10,
        "probleme": "Critère lié à l'âge ou à l'ancienneté professionnelle",
        "suggestion": "Privilégier les compétences et le niveau de qualification"
    },

    "moins de 30 ans": {
        "malus": 10,
        "probleme": "Critère d'âge potentiellement discriminant",
        "suggestion": "Supprimer les restrictions d'âge non justifiées"
    },

    "expérience récente": {
        "malus": 10,
        "probleme": "Peut pénaliser les candidats ayant connu une interruption de carrière",
        "suggestion": "Valoriser les compétences et l'expérience globale"
    },

    "sans handicap": {
        "malus": 10,
        "probleme": "Exclusion directe des personnes en situation de handicap",
        "suggestion": "Décrire les exigences réelles du poste et les aménagements possibles"
    },

    "bonne condition physique": {
        "malus": 10,
        "probleme": "Exigence physique potentiellement excessive ou discriminante",
        "suggestion": "Préciser les capacités physiques réellement nécessaires au poste"
    },

    "présentation irréprochable": {
        "malus": 10,
        "probleme": "Critère subjectif pouvant favoriser certains profils",
        "suggestion": "Décrire les exigences vestimentaires ou professionnelles objectives"
    },

    "langue maternelle française": {
        "malus": 10,
        "probleme": "Critère linguistique pouvant exclure des candidats compétents",
        "suggestion": "Préciser le niveau de français réellement nécessaire"
    },

    "sans accent": {
        "malus": 10,
        "probleme": "Critère pouvant entraîner une discrimination liée à l'origine",
        "suggestion": "Évaluer uniquement la capacité à communiquer efficacement"
    },

    "permis obligatoire": {
        "malus": 10,
        "probleme": "Contrainte pouvant exclure des candidats sans nécessité professionnelle",
        "suggestion": "Vérifier si le permis est réellement indispensable au poste"
    },

    "disponibilité totale": {
        "malus": 10,
        "probleme": "Contrainte pouvant pénaliser les personnes ayant des obligations personnelles",
        "suggestion": "Préciser les horaires et contraintes réelles du poste"
    },

    "célibataire": {
        "malus": 10,
        "probleme": "Critère lié à la situation familiale",
        "suggestion": "Supprimer toute référence à la situation familiale"
    },

    "sans enfants": {
        "malus": 10,
        "probleme": "Critère discriminant lié à la situation familiale",
        "suggestion": "Évaluer uniquement la disponibilité professionnelle nécessaire"
    },

    "résistance au stress": {
        "malus": 10,
        "probleme": "Formulation vague pouvant masquer des conditions de travail difficiles",
        "suggestion": "Décrire les situations concrètes et les contraintes du poste"
    },

    "culture jeune": {
        "malus": 10,
        "probleme": "Expression pouvant suggérer une préférence liée à l'âge",
        "suggestion": "Décrire les valeurs et méthodes de travail de l'entreprise"
    }
}





    

