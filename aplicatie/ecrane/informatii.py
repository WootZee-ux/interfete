"""Ecran de informatii."""
import tkinter as tk

from aplicatie.constante import TEMA
from aplicatie.ecrane.baza import EcranBaza


class EcranInformatii(EcranBaza):
    """Ecran de informatii."""

    def __init__(self, master, aplicatie):
        super().__init__(master, aplicatie, bg=TEMA["fundal_informatii"])
        self._construieste_ui()

    def _construieste_ui(self):
        self.build_header("Informatii", "Prezentare generala a aplicatiei", icon="ℹ️")
        continut = self.build_card()

        tk.Label(
            continut,
            text="Aplicatie pentru managementul cursurilor si testare rapida.",
            font=("Segoe UI", 12, "bold"),
            bg=TEMA["fundal_card"],
            fg=TEMA["text_inchis"],
            wraplength=420,
            justify="left",
        ).pack(anchor="w", pady=(0, 10))

        detalii = (
            "Include module: autentificare, meniu, gestionare cursuri, test grila si sectiune de ajutor.\n\n"
            "Informatiile sunt incarcate si salvate local pentru continuitate si acces rapid."
        )
        tk.Label(
            continut,
            text=detalii,
            bg=TEMA["fundal_card"],
            fg=TEMA["text_pal"],
            justify="left",
            wraplength=420,
        ).pack(anchor="w")

        tk.Button(
            continut,
            text="Inapoi la meniu",
            command=lambda: self.aplicatie.afiseaza_ecran("meniu_principal"),
            bg=TEMA["text_inchis"],
            fg=TEMA["text_deschis"],
            relief="flat",
            padx=12,
            pady=6,
        ).pack(anchor="e", pady=(16, 0))
