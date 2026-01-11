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
        title = tk.Label(self, text="Meniu Principal", font=("Helvetica", 18, "bold"), bg=THEME["menu_bg"])
        title.pack(pady=20)

        subtitle = tk.Label(
            self,
            text="Selecteaza un modul:",
            font=("Helvetica", 12),
            bg=THEME["menu_bg"],
        )
        subtitle.pack(pady=5)

        btn_frame = tk.Frame(self, bg=THEME["menu_bg"])
        btn_frame.pack(pady=10)

        buttons = [
            ("Gestionare Cursuri", lambda: self.app.show_screen("data")),
            ("Test Grila", lambda: self.app.show_screen("quiz")),
            ("Gestionare Quiz", lambda: self.app.show_screen("quiz_management")),
            ("Help", lambda: self.app.show_screen("help")),
        ]
        for idx, (label, cmd) in enumerate(buttons):
            btn = tk.Button(btn_frame, text=label, width=22, command=cmd, bg="#2196f3", fg="white")
            btn.grid(row=idx, column=0, pady=6)

        logout = tk.Button(self, text="Deconectare", command=lambda: self.app.show_screen("login"))
        logout.pack(pady=10)
