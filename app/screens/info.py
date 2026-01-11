"""Ecran de informatii."""
import tkinter as tk

from app.constants import THEME
from app.screens.base import BaseScreen


class InfoScreen(BaseScreen):
    """Ecran de informatii."""

    def __init__(self, master, app):
        super().__init__(master, app, bg=THEME["info_bg"])
        self._build_ui()

    def _build_ui(self):
        title = tk.Label(self, text="Informatii", font=("Helvetica", 18, "bold"), bg=THEME["info_bg"])
        title.pack(pady=15)

        content = (
            "Aplicatie pentru managementul cursurilor si testare rapida.\n"
            "Include module: autentificare, meniu, gestionare cursuri,\n"
            "test grila si sectiune de help.\n\n"
            "Informatiile sunt incarcate si salvate local pentru continuitate."
        )
        tk.Label(self, text=content, bg=THEME["info_bg"], justify="center").pack(pady=10)

        tk.Button(self, text="Inapoi la meniu", command=lambda: self.app.show_screen("main_menu")).pack(pady=10)
