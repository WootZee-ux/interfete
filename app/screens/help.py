"""Ecran de help."""
import tkinter as tk

from app.constants import THEME
from app.screens.base import BaseScreen


class HelpScreen(BaseScreen):
    """Ecran de help."""

    def __init__(self, master, app):
        super().__init__(master, app, bg=THEME["help_bg"])
        self._build_ui()

    def _build_ui(self):
        title = tk.Label(self, text="Help", font=("Helvetica", 18, "bold"), bg=THEME["help_bg"])
        title.pack(pady=15)

        tips = (
            "Navigarea se face folosind butoanele din fiecare ecran.\n"
            "Lista de cursuri poate fi completata cu date noi.\n"
            "Rezultatul testului grila este afisat la final.\n"
            "Pentru orice intrebare, contacteaza responsabilul de laborator."
        )
        tk.Label(self, text=tips, bg=THEME["help_bg"], justify="left").pack(pady=10)

        tk.Button(self, text="Inapoi la meniu", command=lambda: self.app.show_screen("main_menu")).pack(pady=10)
