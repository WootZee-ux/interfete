"""Clase comune pentru ecrane."""
import tkinter as tk

from app.constants import THEME


class BaseScreen(tk.Frame):
    """Clasa de baza pentru ecrane."""

    def __init__(self, master, app, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app

    def build_header(self, title, subtitle=None, icon=None):
        """Construieste un antet comun pentru ecrane."""
        header = tk.Frame(self, bg=THEME["header_bg"])
        header.pack(fill="x")

        header_inner = tk.Frame(header, bg=THEME["header_bg"])
        header_inner.pack(fill="x", padx=18, pady=12)

        if icon:
            tk.Label(
                header_inner,
                text=icon,
                font=("Segoe UI Emoji", 20),
                bg=THEME["header_bg"],
                fg=THEME["accent_primary"],
            ).pack(side="left")

        title_frame = tk.Frame(header_inner, bg=THEME["header_bg"])
        title_frame.pack(side="left", padx=10)
        tk.Label(
            title_frame,
            text=title,
            font=("Segoe UI", 16, "bold"),
            bg=THEME["header_bg"],
            fg=THEME["text_light"],
        ).pack(anchor="w")
        if subtitle:
            tk.Label(
                title_frame,
                text=subtitle,
                font=("Segoe UI", 10),
                bg=THEME["header_bg"],
                fg=THEME["text_muted"],
            ).pack(anchor="w")

        separator = tk.Frame(self, bg=THEME["divider"], height=2)
        separator.pack(fill="x")
        return header

    def build_card(self, padding=(18, 16)):
        """Construieste un card pentru continut."""
        card = tk.Frame(
            self,
            bg=THEME["card_bg"],
            highlightbackground=THEME["card_border"],
            highlightthickness=1,
        )
        card.pack(padx=18, pady=18, fill="both", expand=True)
        inner = tk.Frame(card, bg=THEME["card_bg"])
        inner.pack(fill="both", expand=True, padx=padding[0], pady=padding[1])
        return inner

    def on_show(self):
        """Hook apelat cand ecranul devine activ."""
