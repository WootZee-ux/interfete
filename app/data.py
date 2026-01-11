"""Gestionarea datelor persistente pentru aplicatie."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
STORAGE_DIR = BASE_DIR / "storage"
COURSES_PATH = STORAGE_DIR / "courses.json"
QUIZ_PATH = STORAGE_DIR / "quiz.json"

DEFAULT_COURSES = [
    {"course": "Programare Python", "teacher": "Conf. Popescu"},
    {"course": "Baze de date", "teacher": "Lect. Ionescu"},
    {"course": "Retele de calculatoare", "teacher": "Prof. Georgescu"},
]

DEFAULT_QUIZ_QUESTIONS = [
    {
        "question": "Care este biblioteca grafica folosita in aceasta aplicatie?",
        "options": ["Tkinter", "PyQt", "Kivy"],
        "answer": "Tkinter",
    },
    {
        "question": "Ce widget folosim pentru selectia unei singure optiuni?",
        "options": ["Listbox", "Radiobutton", "Canvas"],
        "answer": "Radiobutton",
    },
]


def load_courses() -> list[dict[str, str]]:
    """Incarca lista de cursuri din fisier."""
    return _load_json(COURSES_PATH, DEFAULT_COURSES)


def save_courses(courses: list[dict[str, str]]) -> None:
    """Salveaza lista de cursuri in fisier."""
    _save_json(COURSES_PATH, courses)


def load_quiz_questions() -> list[dict[str, Any]]:
    """Incarca intrebarile pentru testul grila."""
    return _load_json(QUIZ_PATH, DEFAULT_QUIZ_QUESTIONS)


def save_quiz_questions(questions: list[dict[str, Any]]) -> None:
    """Salveaza intrebarile pentru testul grila in fisier."""
    _save_json(QUIZ_PATH, questions)


def _load_json(path: Path, fallback: list[dict[str, Any]]) -> list[dict[str, Any]]:
    STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        _save_json(path, fallback)
        return [item.copy() for item in fallback]
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except json.JSONDecodeError:
        _save_json(path, fallback)
        return [item.copy() for item in fallback]
    if not isinstance(data, list):
        _save_json(path, fallback)
        return [item.copy() for item in fallback]
    return data


def _save_json(path: Path, data: list[dict[str, Any]]) -> None:
    STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
