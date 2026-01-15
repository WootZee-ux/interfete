"""Clasa de baza si utilitare comune pentru ecranele aplicatiei."""
import tkinter as tk

from aplicatie.constante import TEMA


class EcranBaza(tk.Frame):
    """Clasa de baza pentru ecrane."""

    def __init__(self, master, aplicatie, **kwargs):
        super().__init__(master, **kwargs)
        self.aplicatie = aplicatie

    def build_header(self, title, subtitle=None, icon=None):
        """Construieste un antet comun pentru ecrane."""
        header = tk.Frame(self, bg=TEMA["fundal_antet"])
        header.pack(fill="x")

        header_inner = tk.Frame(header, bg=TEMA["fundal_antet"])
        header_inner.pack(fill="x", padx=18, pady=12)

        if icon:
            tk.Label(
                header_inner,
                text=icon,
                font=("Segoe UI Emoji", 20),
                bg=TEMA["fundal_antet"],
                fg=TEMA["accent_principal"],
            ).pack(side="left")

        title_frame = tk.Frame(header_inner, bg=TEMA["fundal_antet"])
        title_frame.pack(side="left", padx=10)
        tk.Label(
            title_frame,
            text=title,
            font=("Segoe UI", 16, "bold"),
            bg=TEMA["fundal_antet"],
            fg=TEMA["text_deschis"],
        ).pack(anchor="w")
        if subtitle:
            tk.Label(
                title_frame,
                text=subtitle,
                font=("Segoe UI", 10),
                bg=TEMA["fundal_antet"],
                fg=TEMA["text_pal"],
            ).pack(anchor="w")

        separator = tk.Frame(self, bg=TEMA["separator"], height=2)
        separator.pack(fill="x")
        return header

    def build_card(self, padding=(18, 16)):
        """Construieste un card pentru continut."""
        card = tk.Frame(
            self,
            bg=TEMA["fundal_card"],
            highlightbackground=TEMA["contur_card"],
            highlightthickness=1,
        )
        card.pack(padx=18, pady=18, fill="both", expand=True)
        inner = tk.Frame(card, bg=TEMA["fundal_card"])
        inner.pack(fill="both", expand=True, padx=padding[0], pady=padding[1])
        return inner

    def on_show(self):
        """Hook apelat cand ecranul devine activ."""
