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
        self.build_header("Help", "Sfaturi rapide pentru utilizare", icon="🆘")
        content = self.build_card()

        tk.Label(
            content,
            text="Ghid de utilizare",
            font=("Segoe UI", 12, "bold"),
            bg=THEME["card_bg"],
            fg=THEME["text_dark"],
        ).pack(anchor="w", pady=(0, 10))

        tips = (
            "• Navigarea se face folosind butoanele din fiecare ecran.\n"
            "• Lista de cursuri poate fi completata cu date noi.\n"
            "• Intrebarile din test se pot modifica din \"Gestionare Quiz\".\n"
            "• Rezultatul testului grila este afisat la final.\n"
        )
        tk.Label(
            content,
            text=tips,
            bg=THEME["card_bg"],
            fg=THEME["text_muted"],
            justify="left",
        ).pack(anchor="w")

        tk.Button(
            content,
            text="Inapoi la meniu",
            command=lambda: self.app.show_screen("main_menu"),
            bg=THEME["text_dark"],
            fg=THEME["text_light"],
            relief="flat",
            padx=12,
            pady=6,
        ).pack(anchor="e", pady=(16, 0))
