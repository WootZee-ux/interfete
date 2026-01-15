"""Ecran pentru adaugarea activitatilor in calendar."""
from tkinter import messagebox
import tkinter as tk

from aplicatie.constante import TEMA
from aplicatie.date import salveaza_activitati
from aplicatie.ecrane.baza import EcranBaza


class EcranAdaugaActivitate(EcranBaza):
    """Ecran pentru adaugarea unei activitati."""

    def __init__(self, master, aplicatie):
        super().__init__(master, aplicatie, bg=TEMA["fundal_calendar"])
        self.camp_zi = None
        self.camp_activitate = None
        self.camp_ora = None
        self._construieste_ui()

    def _construieste_ui(self):
        self.build_header("Adauga activitate", "Completeaza detaliile pentru calendar", icon="➕")
        continut = self.build_card()
        continut.columnconfigure(1, weight=1)

        tk.Label(
            continut,
            text="Zi",
            bg=TEMA["fundal_card"],
            fg=TEMA["text_pal"],
        ).grid(row=0, column=0, sticky="w")
        tk.Label(
            continut,
            text="Activitate",
            bg=TEMA["fundal_card"],
            fg=TEMA["text_pal"],
        ).grid(row=1, column=0, sticky="w", pady=(8, 0))
        tk.Label(
            continut,
            text="Ora",
            bg=TEMA["fundal_card"],
            fg=TEMA["text_pal"],
        ).grid(row=2, column=0, sticky="w", pady=(8, 0))

        self.camp_zi = tk.Entry(
            continut,
            bg=TEMA["fundal_intrare"],
            fg=TEMA["text_intrare"],
            relief="flat",
            highlightthickness=1,
            highlightbackground=TEMA["contur_card"],
        )
        self.camp_activitate = tk.Entry(
            continut,
            bg=TEMA["fundal_intrare"],
            fg=TEMA["text_intrare"],
            relief="flat",
            highlightthickness=1,
            highlightbackground=TEMA["contur_card"],
        )
        self.camp_ora = tk.Entry(
            continut,
            bg=TEMA["fundal_intrare"],
            fg=TEMA["text_intrare"],
            relief="flat",
            highlightthickness=1,
            highlightbackground=TEMA["contur_card"],
        )
        self.camp_zi.grid(row=0, column=1, sticky="ew", padx=(12, 0))
        self.camp_activitate.grid(row=1, column=1, sticky="ew", padx=(12, 0), pady=(8, 0))
        self.camp_ora.grid(row=2, column=1, sticky="ew", padx=(12, 0), pady=(8, 0))

        actiuni = tk.Frame(continut, bg=TEMA["fundal_card"])
        actiuni.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(16, 0))
        tk.Button(
            actiuni,
            text="Salveaza",
            command=self._salveaza,
            bg=TEMA["accent_secundar"],
            fg=TEMA["text_deschis"],
            relief="flat",
            padx=12,
            pady=6,
        ).pack(side="left")
        tk.Button(
            actiuni,
            text="Inapoi la calendar",
            command=lambda: self.aplicatie.afiseaza_ecran("calendar"),
            bg=TEMA["text_inchis"],
            fg=TEMA["text_deschis"],
            relief="flat",
            padx=12,
            pady=6,
        ).pack(side="right")

    def _salveaza(self):
        zi = self.camp_zi.get().strip()
        activitate = self.camp_activitate.get().strip()
        ora = self.camp_ora.get().strip()
        if not zi or not activitate or not ora:
            messagebox.showwarning("Date incomplete", "Completeaza ziua, activitatea si ora.")
            return
        self.aplicatie.activitati.append({"zi": zi, "activitate": activitate, "ora": ora})
        salveaza_activitati(self.aplicatie.activitati)
        self.camp_zi.delete(0, tk.END)
        self.camp_activitate.delete(0, tk.END)
        self.camp_ora.delete(0, tk.END)
        messagebox.showinfo("Salvare", "Activitatea a fost adaugata.")
        self.aplicatie.afiseaza_ecran("calendar")
