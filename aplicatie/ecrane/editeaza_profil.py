"""Ecran pentru editarea profilului utilizatorului."""
from tkinter import messagebox
import tkinter as tk

from aplicatie.constante import TEMA
from aplicatie.date import salveaza_profil
from aplicatie.ecrane.baza import EcranBaza


class EcranEditeazaProfil(EcranBaza):
    """Ecran de editare a datelor de profil."""

    def __init__(self, master, aplicatie):
        super().__init__(master, aplicatie, bg=TEMA["fundal_profil"])
        self.campuri = {}
        self._construieste_ui()

    def _construieste_ui(self):
        self.build_header("Editeaza profil", "Actualizeaza datele personale", icon="✏️")
        continut = self.build_card()
        continut.columnconfigure(1, weight=1)

        etichete = [
            ("Nume", "nume"),
            ("Grupa", "grupa"),
            ("Specializare", "specializare"),
            ("Email", "email"),
            ("An", "an"),
        ]
        for index, (eticheta, cheie) in enumerate(etichete):
            tk.Label(
                continut,
                text=eticheta,
                bg=TEMA["fundal_card"],
                fg=TEMA["text_pal"],
            ).grid(row=index, column=0, sticky="w", pady=(8 if index else 0, 0))
            camp = tk.Entry(
                continut,
                bg=TEMA["fundal_intrare"],
                fg=TEMA["text_intrare"],
                relief="flat",
                highlightthickness=1,
                highlightbackground=TEMA["contur_card"],
            )
            camp.grid(row=index, column=1, sticky="ew", padx=(12, 0), pady=(8 if index else 0, 0))
            self.campuri[cheie] = camp

        actiuni = tk.Frame(continut, bg=TEMA["fundal_card"])
        actiuni.grid(row=len(etichete), column=0, columnspan=2, sticky="ew", pady=(18, 0))
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
            text="Inapoi la profil",
            command=lambda: self.aplicatie.afiseaza_ecran("profil"),
            bg=TEMA["text_inchis"],
            fg=TEMA["text_deschis"],
            relief="flat",
            padx=12,
            pady=6,
        ).pack(side="right")

    def on_show(self):
        for cheie, camp in self.campuri.items():
            camp.delete(0, tk.END)
            camp.insert(0, self.aplicatie.profil.get(cheie, ""))

    def _salveaza(self):
        date = {cheie: camp.get().strip() for cheie, camp in self.campuri.items()}
        if not all(date.values()):
            messagebox.showwarning("Date incomplete", "Completeaza toate campurile profilului.")
            return
        self.aplicatie.profil = date
        salveaza_profil(date)
        messagebox.showinfo("Salvare", "Profilul a fost actualizat.")
        self.aplicatie.afiseaza_ecran("profil")
