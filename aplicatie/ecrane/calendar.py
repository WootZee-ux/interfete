"""Ecranul de calendar pentru activitati."""
import tkinter as tk

from aplicatie.constante import TEMA
from aplicatie.ecrane.baza import EcranBaza


class EcranCalendar(EcranBaza):
    """Ecran de calendar."""

    def __init__(self, master, aplicatie):
        super().__init__(master, aplicatie, bg=TEMA["fundal_calendar"])
        self.lista = None
        self._construieste_ui()

    def _construieste_ui(self):
        self.build_header("Calendar activitati", "Program si termene limita", icon="📅")
        continut = self.build_card()

        tk.Label(
            continut,
            text="Saptamana curenta",
            font=("Segoe UI", 12, "bold"),
            bg=TEMA["fundal_card"],
            fg=TEMA["text_inchis"],
        ).pack(anchor="w", pady=(0, 10))

        self.lista = tk.Frame(continut, bg=TEMA["fundal_card"])
        self.lista.pack(fill="both", expand=True)

        actiuni = tk.Frame(continut, bg=TEMA["fundal_card"])
        actiuni.pack(fill="x", pady=(12, 0))
        tk.Button(
            actiuni,
            text="Adauga activitate",
            command=lambda: self.aplicatie.afiseaza_ecran("adauga_activitate"),
            bg=TEMA["accent_principal"],
            fg=TEMA["text_inchis"],
            relief="flat",
            padx=12,
            pady=6,
        ).pack(side="left")
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
        for widget in self.lista.winfo_children():
            widget.destroy()
        for activitate in self.aplicatie.activitati:
            rand = tk.Frame(self.lista, bg=TEMA["fundal_card"])
            rand.pack(fill="x", pady=3)
            tk.Label(
                rand,
                text=activitate.get("zi", ""),
                width=10,
                anchor="w",
                bg=TEMA["fundal_card"],
                fg=TEMA["text_pal"],
            ).pack(side="left")
            descriere = f"{activitate.get('activitate', '')} - {activitate.get('ora', '')}".strip(" -")
            tk.Label(
                rand,
                text=descriere,
                bg=TEMA["fundal_card"],
                fg=TEMA["text_inchis"],
            ).pack(side="left")
