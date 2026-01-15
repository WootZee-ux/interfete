"""Ecran principal cu navigare."""
import tkinter as tk

from app.constants import FONTS, THEME
from app.screens.base import BaseScreen


class MainMenuScreen(BaseScreen):
    """Ecran principal cu navigare."""

    def __init__(self, master, app):
        super().__init__(master, app, bg=THEME["menu_bg"])
        self.course_count = tk.StringVar(value="0")
        self.quiz_count = tk.StringVar(value="0")
        self._build_ui()

    def _build_ui(self):
        header = tk.Frame(self, bg=THEME["menu_bg"], padx=20, pady=15)
        header.pack(fill="x")
        tk.Label(header, text="Meniu Principal", font=FONTS["title"], bg=THEME["menu_bg"]).pack(anchor="w")
        tk.Label(
            header,
            text="Alege modulul dorit sau verifica statusul datelor.",
            font=FONTS["small"],
            bg=THEME["menu_bg"],
            fg=THEME["text_muted"],
        ).pack(anchor="w", pady=(4, 0))

        stats = tk.Frame(self, bg=THEME["panel_bg"], padx=16, pady=12, highlightbackground=THEME["outline"])
        stats.pack(padx=25, pady=10, fill="x")
        stats.configure(highlightthickness=1)
        tk.Label(stats, text="Cursuri inregistrate:", bg=THEME["panel_bg"], font=FONTS["body"]).grid(
            row=0, column=0, sticky="w"
        )
        tk.Label(stats, textvariable=self.course_count, bg=THEME["panel_bg"], font=FONTS["subtitle"]).grid(
            row=0, column=1, sticky="e", padx=10
        )
        tk.Label(stats, text="Intrebari quiz:", bg=THEME["panel_bg"], font=FONTS["body"]).grid(
            row=1, column=0, sticky="w", pady=(6, 0)
        )
        tk.Label(stats, textvariable=self.quiz_count, bg=THEME["panel_bg"], font=FONTS["subtitle"]).grid(
            row=1, column=1, sticky="e", padx=10
        )
        stats.columnconfigure(0, weight=1)

        btn_frame = tk.Frame(self, bg=THEME["menu_bg"])
        btn_frame.pack(pady=15)

        buttons = [
            ("Gestionare Cursuri", lambda: self.app.show_screen("data"), THEME["accent"]),
            ("Test Grila", lambda: self.app.show_screen("quiz"), "#7e57c2"),
            ("Gestionare Quiz", lambda: self.app.show_screen("quiz_management"), THEME["accent_alt"]),
            ("Help & Suport", lambda: self.app.show_screen("help"), "#546e7a"),
        ]
        for idx, (label, cmd, color) in enumerate(buttons):
            btn = tk.Button(btn_frame, text=label, width=24, command=cmd, bg=color, fg="white")
            btn.grid(row=idx, column=0, pady=6)

        logout = tk.Button(
            self,
            text="Iesire din cont",
            command=lambda: self.app.show_screen("login"),
            bg=THEME["warn"],
            fg="white",
        )
        logout.pack(pady=10)

    def on_show(self):
        self.course_count.set(str(len(self.app.courses)))
        self.quiz_count.set(str(len(self.app.quiz_questions)))
