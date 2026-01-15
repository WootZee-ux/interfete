"""Ecranul de profil al utilizatorului."""
import tkinter as tk

from aplicatie.constante import TEMA
from aplicatie.ecrane.baza import EcranBaza


class EcranProfil(EcranBaza):
    """Ecran de profil."""

    def __init__(self, master, aplicatie):
        super().__init__(master, aplicatie, bg=TEMA["fundal_profil"])
        self.valori = {}
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
            ("Nume", "nume"),
            ("Grupa", "grupa"),
            ("Specializare", "specializare"),
            ("Email", "email"),
            ("An", "an"),
        ]
        for eticheta, cheie in campuri:
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
            valoare_label = tk.Label(
                linie,
                text="",
                bg=TEMA["fundal_card"],
                fg=TEMA["text_inchis"],
            )
            valoare_label.pack(side="left")
            self.valori[cheie] = valoare_label

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

        actiuni = tk.Frame(continut, bg=TEMA["fundal_card"])
        actiuni.pack(fill="x", pady=(16, 0))
        tk.Button(
            actiuni,
            text="Editeaza profil",
            command=lambda: self.aplicatie.afiseaza_ecran("editeaza_profil"),
            bg=TEMA["accent_secundar"],
            fg=TEMA["text_deschis"],
            relief="flat",
            padx=12,
            pady=6,
        ).pack(side="left")
        tk.Button(
            actiuni,
            text="Adauga utilizator",
            command=lambda: self.aplicatie.afiseaza_ecran("gestionare_utilizatori"),
            bg=TEMA["accent_principal"],
            fg=TEMA["text_inchis"],
            relief="flat",
            padx=12,
            pady=6,
        ).pack(side="left", padx=(10, 0))
        tk.Button(
            actiuni,
            text="Inapoi la meniu",
            command=lambda: self.aplicatie.afiseaza_ecran("meniu_principal"),
            bg=TEMA["text_inchis"],
            fg=TEMA["text_deschis"],
            relief="flat",
            padx=12,
            pady=6,
        ).pack(side="right")

    def on_show(self):
        for cheie, label in self.valori.items():
            label.config(text=self.aplicatie.profil.get(cheie, ""))
