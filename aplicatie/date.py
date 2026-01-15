"""Gestionarea fisierelor de date persistente pentru cursuri si chestionar."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
DIRECTOR_STOCARE = BASE_DIR / "stocare"
FISIER_CURSURI = DIRECTOR_STOCARE / "cursuri.json"
FISIER_CHESTIONAR = DIRECTOR_STOCARE / "chestionar.json"
FISIER_ACTIVITATI = DIRECTOR_STOCARE / "activitati.json"
FISIER_UTILIZATORI = DIRECTOR_STOCARE / "utilizatori.json"
FISIER_PROFIL = DIRECTOR_STOCARE / "profil.json"

CURSURI_IMPLICITE = [
    {"curs": "Algoritmi si structuri de date", "profesor": "Conf. Dumitrescu"},
    {"curs": "Ingineria programarii", "profesor": "Lect. Marin"},
    {"curs": "Sisteme de operare", "profesor": "Prof. Stan"},
]

INTREBARI_IMPLICITE = [
    {
        "intrebare": "Ce tip de fisier folosim pentru persistenta datelor cursurilor?",
        "optiuni": ["JSON", "CSV", "XML"],
        "raspuns": "JSON",
    },
    {
        "intrebare": "Care este widgetul folosit pentru afisarea unei liste selectabile?",
        "optiuni": ["Listbox", "Label", "Entry"],
        "raspuns": "Listbox",
    },
]

ACTIVITATI_IMPLICITE = [
    {"zi": "Luni", "activitate": "Curs Inteligenta Artificiala", "ora": "08:30"},
    {"zi": "Marti", "activitate": "Laborator Retele", "ora": "11:00"},
    {"zi": "Miercuri", "activitate": "Proiect Interfete", "ora": "13:30"},
    {"zi": "Joi", "activitate": "Seminar Sisteme de Operare", "ora": "15:00"},
    {"zi": "Vineri", "activitate": "Colocviu Matematica Discreta", "ora": "09:30"},
    {"zi": "Sambata", "activitate": "Consultatii proiect", "ora": "10:30"},
    {"zi": "Duminica", "activitate": "Pregatire examen", "ora": "17:00"},
]

UTILIZATORI_IMPLICITI = [
    {"nume": "Daniel Uta", "rol": "Student", "email": "daniel.uta@s.utm.ro"},
    {"nume": "Maria Ionescu", "rol": "Profesor", "email": "maria.ionescu@utm.ro"},
]

PROFIL_IMPLICIT = {
    "nume": "Daniel Uta",
    "grupa": "312",
    "specializare": "Informatica",
    "email": "daniel.uta@s.utm.ro",
    "an": "III",
}


def incarca_cursuri() -> list[dict[str, str]]:
    """Incarca lista de cursuri din fisier."""
    return _incarca_json(FISIER_CURSURI, CURSURI_IMPLICITE)


def salveaza_cursuri(cursuri: list[dict[str, str]]) -> None:
    """Salveaza lista de cursuri in fisier."""
    _salveaza_json(FISIER_CURSURI, cursuri)


def incarca_chestionar() -> list[dict[str, Any]]:
    """Incarca intrebarile pentru testul grila."""
    return _incarca_json(FISIER_CHESTIONAR, INTREBARI_IMPLICITE)


def salveaza_chestionar(intrebari: list[dict[str, Any]]) -> None:
    """Salveaza intrebarile pentru testul grila in fisier."""
    _salveaza_json(FISIER_CHESTIONAR, intrebari)


def incarca_activitati() -> list[dict[str, str]]:
    """Incarca lista de activitati din fisier."""
    return _incarca_json(FISIER_ACTIVITATI, ACTIVITATI_IMPLICITE)


def salveaza_activitati(activitati: list[dict[str, str]]) -> None:
    """Salveaza lista de activitati in fisier."""
    _salveaza_json(FISIER_ACTIVITATI, activitati)


def incarca_utilizatori() -> list[dict[str, str]]:
    """Incarca lista de utilizatori din fisier."""
    return _incarca_json(FISIER_UTILIZATORI, UTILIZATORI_IMPLICITI)


def salveaza_utilizatori(utilizatori: list[dict[str, str]]) -> None:
    """Salveaza lista de utilizatori in fisier."""
    _salveaza_json(FISIER_UTILIZATORI, utilizatori)


def incarca_profil() -> dict[str, str]:
    """Incarca datele de profil din fisier."""
    DIRECTOR_STOCARE.mkdir(parents=True, exist_ok=True)
    if not FISIER_PROFIL.exists():
        _salveaza_dict(FISIER_PROFIL, PROFIL_IMPLICIT)
        return PROFIL_IMPLICIT.copy()
    try:
        with FISIER_PROFIL.open("r", encoding="utf-8") as handle:
            date = json.load(handle)
    except json.JSONDecodeError:
        _salveaza_dict(FISIER_PROFIL, PROFIL_IMPLICIT)
        return PROFIL_IMPLICIT.copy()
    if not isinstance(date, dict):
        _salveaza_dict(FISIER_PROFIL, PROFIL_IMPLICIT)
        return PROFIL_IMPLICIT.copy()
    return {**PROFIL_IMPLICIT, **date}


def salveaza_profil(date_profil: dict[str, str]) -> None:
    """Salveaza datele de profil in fisier."""
    _salveaza_dict(FISIER_PROFIL, date_profil)


def _incarca_json(cale: Path, fallback: list[dict[str, Any]]) -> list[dict[str, Any]]:
    DIRECTOR_STOCARE.mkdir(parents=True, exist_ok=True)
    if not cale.exists():
        # Initializam fisierul cu date implicite daca lipseste.
        _salveaza_json(cale, fallback)
        return [item.copy() for item in fallback]
    try:
        with cale.open("r", encoding="utf-8") as handle:
            date = json.load(handle)
    except json.JSONDecodeError:
        # Refacem fisierul daca JSON-ul este corupt.
        _salveaza_json(cale, fallback)
        return [item.copy() for item in fallback]
    if not isinstance(date, list):
        # Pastram structura asteptata pentru ecranele aplicatiei.
        _salveaza_json(cale, fallback)
        return [item.copy() for item in fallback]
    return date


def _salveaza_json(cale: Path, date: list[dict[str, Any]]) -> None:
    DIRECTOR_STOCARE.mkdir(parents=True, exist_ok=True)
    # Salvam consistent datele pentru a fi reutilizate la urmatoarea pornire.
    with cale.open("w", encoding="utf-8") as handle:
        json.dump(date, handle, ensure_ascii=False, indent=2)


def _salveaza_dict(cale: Path, date: dict[str, Any]) -> None:
    DIRECTOR_STOCARE.mkdir(parents=True, exist_ok=True)
    with cale.open("w", encoding="utf-8") as handle:
        json.dump(date, handle, ensure_ascii=False, indent=2)
