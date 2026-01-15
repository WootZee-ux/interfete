"""Ecran de help."""
import tkinter as tk

from app.constants import FONTS, THEME
from app.screens.base import BaseScreen


class HelpScreen(BaseScreen):
    """Ecran de help."""

    def __init__(self, master, app):
        super().__init__(master, app, bg=THEME["help_bg"])
        self._build_ui()

    def _build_ui(self):
        header = tk.Frame(self, bg=THEME["help_bg"], padx=20, pady=15)
        header.pack(fill="x")
        tk.Label(header, text="Help & Suport", font=FONTS["title"], bg=THEME["help_bg"]).pack(anchor="w")
        tk.Label(
            header,
            text="Ghid rapid pentru utilizarea aplicatiei.",
            font=FONTS["small"],
            bg=THEME["help_bg"],
            fg=THEME["text_muted"],
        ).pack(anchor="w", pady=(4, 0))

        panel = tk.Frame(self, bg=THEME["panel_bg"], padx=16, pady=14, highlightbackground=THEME["outline"])
        panel.pack(padx=25, pady=15, fill="both", expand=True)
        panel.configure(highlightthickness=1)

        tips = [
            "Navigheaza intre ecrane folosind butoanele principale.",
            "In modulul de cursuri poti adauga sau sterge intrari.",
            "Intrebarile pentru test se editeaza din Gestionare Quiz.",
            "Scorul se actualizeaza automat dupa fiecare raspuns.",
        ]
        tk.Label(panel, text="Recomandari:", bg=THEME["panel_bg"], font=FONTS["subtitle"]).pack(anchor="w")
        for tip in tips:
            tk.Label(panel, text=f"• {tip}", bg=THEME["panel_bg"], anchor="w", font=FONTS["body"]).pack(
                anchor="w", pady=2
            )

        contact = tk.Label(
            panel,
            text="Suport: suport@campus.local | Program 09:00 - 17:00",
            bg=THEME["panel_bg"],
            fg=THEME["text_muted"],
            font=FONTS["small"],
        )
        contact.pack(anchor="w", pady=(12, 0))

        tk.Button(self, text="Inapoi la meniu", command=lambda: self.app.show_screen("main_menu")).pack(pady=10)
