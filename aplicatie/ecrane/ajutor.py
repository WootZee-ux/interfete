"""Ecran cu informatii de ajutor si ghid pentru utilizator."""
import tkinter as tk

from aplicatie.constante import TEMA
from aplicatie.ecrane.baza import EcranBaza


class EcranAjutor(EcranBaza):
    """Ecran de ajutor."""

    def __init__(self, master, aplicatie):
        super().__init__(master, aplicatie, bg=TEMA["fundal_ajutor"])
        self._construieste_ui()

    def _construieste_ui(self):
        self.build_header("Ajutor", "Sfaturi rapide pentru utilizare", icon="🆘")
        continut = self.build_card()

        tk.Label(
            continut,
            text="Ghid de utilizare",
            font=("Segoe UI", 12, "bold"),
            bg=TEMA["fundal_card"],
            fg=TEMA["text_inchis"],
        ).pack(anchor="w", pady=(0, 10))

        sfaturi = (
            "• Navigarea se face folosind butoanele din fiecare ecran.\n"
            "• Lista de cursuri poate fi completata cu date noi.\n"
            "• Intrebarile din test se pot modifica din \"Gestionare chestionar\".\n"
            "• Rezultatul testului grila este afisat la final.\n"
        )
        tk.Label(
            continut,
            text=sfaturi,
            bg=TEMA["fundal_card"],
            fg=TEMA["text_pal"],
            justify="left",
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
