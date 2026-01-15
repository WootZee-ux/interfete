"""Ecran de test grila."""
from tkinter import messagebox
import tkinter as tk

from aplicatie.constante import TEMA
from aplicatie.ecrane.baza import EcranBaza


class EcranChestionar(EcranBaza):
    """Ecran de test grila."""

    def __init__(self, master, aplicatie):
        super().__init__(master, aplicatie, bg=TEMA["fundal_chestionar"])
        self.variabila_raspuns = tk.StringVar(value="")
        self.intrebare_curenta = 0
        self.scor = 0
        self._construieste_ui()

    def _construieste_ui(self):
        self.build_header("Test grila", "Raspunde corect pentru scor maxim", icon="📝")
        continut = self.build_card()

        self.eticheta_progres = tk.Label(
            continut,
            text="",
            bg=TEMA["fundal_card"],
            fg=TEMA["text_pal"],
        )
        self.eticheta_progres.pack(anchor="w")

        self.eticheta_intrebare = tk.Label(
            continut,
            text="",
            bg=TEMA["fundal_card"],
            fg=TEMA["text_inchis"],
            font=("Segoe UI", 12, "bold"),
            wraplength=420,
            justify="left",
        )
        self.eticheta_intrebare.pack(pady=(8, 12), anchor="w")

        self.cadru_optiuni = tk.Frame(continut, bg=TEMA["fundal_card"])
        self.cadru_optiuni.pack(pady=5, anchor="w", fill="x")

        self.eticheta_feedback = tk.Label(continut, text="", bg=TEMA["fundal_card"], fg=TEMA["accent_mov"])
        self.eticheta_feedback.pack(pady=(0, 6))

        cadru_butoane = tk.Frame(continut, bg=TEMA["fundal_card"])
        cadru_butoane.pack(pady=10, fill="x")

        self.buton_trimite = tk.Button(
            cadru_butoane,
            text="Trimite raspuns",
            command=self._trimite_raspuns,
            bg=TEMA["accent_principal"],
            fg=TEMA["text_inchis"],
            relief="flat",
            padx=12,
            pady=6,
        )
        self.buton_trimite.pack(side="left")

        self.buton_urmator = tk.Button(
            cadru_butoane,
            text="Urmatoarea intrebare",
            command=self._urmatoarea_intrebare,
            bg=TEMA["accent_secundar"],
            fg=TEMA["text_deschis"],
            relief="flat",
            padx=12,
            pady=6,
        )
        self.buton_urmator.pack(side="left", padx=8)

        tk.Button(
            cadru_butoane,
            text="Inapoi la meniu",
            command=lambda: self.aplicatie.afiseaza_ecran("meniu_principal"),
            bg=TEMA["text_inchis"],
            fg=TEMA["text_deschis"],
            relief="flat",
            padx=12,
            pady=6,
        ).pack(side="right")

    def on_show(self):
        self.intrebare_curenta = 0
        self.scor = 0
        self._incarca_intrebare()

    def _incarca_intrebare(self):
        intrebare = self.aplicatie.intrebari_chestionar[self.intrebare_curenta]
        self.variabila_raspuns = tk.StringVar(value="__fara_selectie__")
        self.eticheta_progres.config(
            text=f"Intrebarea {self.intrebare_curenta + 1} din {len(self.aplicatie.intrebari_chestionar)}"
        )
        self.eticheta_intrebare.config(text=intrebare["intrebare"])
        for widget in self.cadru_optiuni.winfo_children():
            widget.destroy()
        for optiune in intrebare["optiuni"]:
            tk.Radiobutton(
                self.cadru_optiuni,
                text=optiune,
                value=optiune,
                variable=self.variabila_raspuns,
                bg=TEMA["fundal_card"],
                fg=TEMA["text_inchis"],
                selectcolor=TEMA["accent_principal"],
                anchor="w",
            ).pack(anchor="w", padx=20, fill="x")
        self.eticheta_feedback.config(text="")

    def _trimite_raspuns(self):
        if not self.variabila_raspuns.get():
            messagebox.showwarning("Raspuns", "Selecteaza un raspuns.")
            return
        corect = self.aplicatie.intrebari_chestionar[self.intrebare_curenta]["raspuns"]
        if self.variabila_raspuns.get() == corect:
            self.scor += 1
            self.eticheta_feedback.config(text="Corect!", fg="#2e7d32")
        else:
            self.eticheta_feedback.config(text=f"Gresit. Raspuns corect: {corect}", fg="#c62828")

    def _urmatoarea_intrebare(self):
        if self.intrebare_curenta < len(self.aplicatie.intrebari_chestionar) - 1:
            self.intrebare_curenta += 1
            self._incarca_intrebare()
        else:
            messagebox.showinfo(
                "Rezultat final", f"Scor: {self.scor}/{len(self.aplicatie.intrebari_chestionar)}"
            )
            self.intrebare_curenta = 0
            self._incarca_intrebare()
