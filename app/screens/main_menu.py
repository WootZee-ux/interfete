"""Ecran principal cu navigare."""
import tkinter as tk

from app.constants import THEME
from app.screens.base import BaseScreen


class MainMenuScreen(BaseScreen):
    """Ecran principal cu navigare."""

    def __init__(self, master, app):
        super().__init__(master, app, bg=THEME["menu_bg"])
        self._build_ui()

    def _build_ui(self):
        self.build_header("Meniu Principal", "Alege un modul pentru a continua", icon="🧭")
        content = self.build_card()

        title = tk.Label(
            content,
            text="Panou de comanda",
            font=("Segoe UI", 14, "bold"),
            bg=THEME["card_bg"],
            fg=THEME["text_dark"],
        )
        title.pack(anchor="w")

        grid = tk.Frame(content, bg=THEME["card_bg"])
        grid.pack(fill="both", expand=True, pady=12)
        for column in range(2):
            grid.columnconfigure(column, weight=1)

        buttons = [
            ("📚 Gestionare Cursuri", THEME["accent_primary"], lambda: self.app.show_screen("data")),
            ("📝 Test Grila", THEME["accent_purple"], lambda: self.app.show_screen("quiz")),
            ("🧩 Gestionare Quiz", THEME["accent_secondary"], lambda: self.app.show_screen("quiz_management")),
            ("🆘 Help & Ghid", THEME["accent_rose"], lambda: self.app.show_screen("help")),
        ]
        for idx, (label, color, cmd) in enumerate(buttons):
            row, col = divmod(idx, 2)
            btn = tk.Button(
                grid,
                text=label,
                command=cmd,
                bg=color,
                fg=THEME["text_light"],
                relief="flat",
                padx=12,
                pady=12,
            )
            btn.grid(row=row, column=col, padx=6, pady=6, sticky="ew")

        footer = tk.Frame(content, bg=THEME["card_bg"])
        footer.pack(fill="x", pady=(12, 0))
        tk.Label(
            footer,
            text="Status: conectat",
            bg=THEME["card_bg"],
            fg=THEME["text_muted"],
        ).pack(side="left")
        logout = tk.Button(
            footer,
            text="Deconectare",
            command=lambda: self.app.show_screen("login"),
            bg=THEME["text_dark"],
            fg=THEME["text_light"],
            relief="flat",
            padx=12,
            pady=6,
        )
        logout.pack(side="right")
