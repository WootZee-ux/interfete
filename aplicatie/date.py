"""Gestionarea datelor persistente pentru aplicatie."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
DIRECTOR_STOCARE = BASE_DIR / "stocare"
FISIER_CURSURI = DIRECTOR_STOCARE / "cursuri.json"
FISIER_CHESTIONAR = DIRECTOR_STOCARE / "chestionar.json"

CURSURI_IMPLICITE = [
    {"curs": "Programare Python", "profesor": "Conf. Popescu"},
    {"curs": "Baze de date", "profesor": "Lect. Ionescu"},
    {"curs": "Retele de calculatoare", "profesor": "Prof. Georgescu"},
]

INTREBARI_IMPLICITE = [
    {
        "intrebare": "Care este biblioteca grafica folosita in aceasta aplicatie?",
        "optiuni": ["Tkinter", "PyQt", "Kivy"],
        "raspuns": "Tkinter",
    },
    {
        "intrebare": "Ce widget folosim pentru selectia unei singure optiuni?",
        "optiuni": ["Listbox", "Radiobutton", "Canvas"],
        "raspuns": "Radiobutton",
    },
]


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
