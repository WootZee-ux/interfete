"""Ecranul de profil al utilizatorului."""
import tkinter as tk

from aplicatie.constante import TEMA
from aplicatie.ecrane.baza import EcranBaza


class EcranProfil(EcranBaza):
    """Ecran de profil."""

    def __init__(self, master, aplicatie):
        super().__init__(master, aplicatie, bg=TEMA["fundal_profil"])
        self._construieste_ui()

    def _construieste_ui(self):
        self.build_header("Profil utilizator", "Date personale si preferinte", icon="👤")
        continut = self.build_card()

        tk.Label(
            continut,
            text="Profil student",
            font=("Segoe UI", 12, "bold"),
            bg=TEMA["fundal_card"],
            fg=TEMA["text_inchis"],
        ).pack(anchor="w", pady=(0, 10))

        detalii = tk.Frame(continut, bg=TEMA["fundal_card"])
        detalii.pack(fill="x")
        campuri = [
            ("Nume", "Ana Popescu"),
            ("Grupa", "101"),
            ("Specializare", "Informatica"),
            ("Email", "ana.popescu@exemplu.ro"),
        ]
        for eticheta, valoare in campuri:
            linie = tk.Frame(detalii, bg=TEMA["fundal_card"])
            linie.pack(fill="x", pady=2)
            tk.Label(
                linie,
                text=f"{eticheta}:",
                width=14,
                anchor="w",
                bg=TEMA["fundal_card"],
                fg=TEMA["text_pal"],
            ).pack(side="left")
            tk.Label(
                linie,
                text=valoare,
                bg=TEMA["fundal_card"],
                fg=TEMA["text_inchis"],
            ).pack(side="left")

        preferinte = tk.Frame(continut, bg=TEMA["fundal_card"])
        preferinte.pack(fill="x", pady=(12, 0))
        tk.Label(
            preferinte,
            text="Preferinte notificari",
            font=("Segoe UI", 11, "bold"),
            bg=TEMA["fundal_card"],
            fg=TEMA["text_inchis"],
        ).pack(anchor="w")

        tk.Checkbutton(
            preferinte,
            text="Trimite remindere pentru teste",
            bg=TEMA["fundal_card"],
            fg=TEMA["text_inchis"],
            activebackground=TEMA["fundal_card"],
            selectcolor=TEMA["fundal_card"],
        ).pack(anchor="w")
        tk.Checkbutton(
            preferinte,
            text="Primesti notificari pentru cursuri noi",
            bg=TEMA["fundal_card"],
            fg=TEMA["text_inchis"],
            activebackground=TEMA["fundal_card"],
            selectcolor=TEMA["fundal_card"],
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
