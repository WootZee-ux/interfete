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
        self.build_header("Informatii", "Prezentare generala a aplicatiei", icon="ℹ️")
        content = self.build_card()

        tk.Label(
            content,
            text="Aplicatie pentru managementul cursurilor si testare rapida.",
            font=("Segoe UI", 12, "bold"),
            bg=THEME["card_bg"],
            fg=THEME["text_dark"],
            wraplength=420,
            justify="left",
        ).pack(anchor="w", pady=(0, 10))

        details = (
            "Include module: autentificare, meniu, gestionare cursuri, test grila si sectiune de help.\n\n"
            "Informatiile sunt incarcate si salvate local pentru continuitate si acces rapid."
        )
        tk.Label(
            content,
            text=details,
            bg=THEME["card_bg"],
            fg=THEME["text_muted"],
            justify="left",
            wraplength=420,
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
