"""Ecran de gestionare a datelor (cursuri)."""
from tkinter import messagebox
import tkinter as tk

from aplicatie.constante import TEMA
from aplicatie.date import salveaza_cursuri
from aplicatie.ecrane.baza import EcranBaza


class EcranGestionareCursuri(EcranBaza):
    """Ecran de gestionare a datelor (cursuri)."""

    def __init__(self, master, aplicatie):
        super().__init__(master, aplicatie, bg=TEMA["fundal_date"])
        self._construieste_ui()

    def _construieste_ui(self):
        self.build_header("Gestionare cursuri", "Adauga si actualizeaza cursurile active", icon="📚")
        continut = self.build_card()
        continut.columnconfigure(0, weight=1)

        titlu_formular = tk.Label(
            continut,
            text="Detalii curs",
            font=("Segoe UI", 12, "bold"),
            bg=TEMA["fundal_card"],
            fg=TEMA["text_inchis"],
        )
        titlu_formular.grid(row=0, column=0, sticky="w")

        formular = tk.Frame(continut, bg=TEMA["fundal_card"])
        formular.grid(row=1, column=0, sticky="ew", pady=(6, 12))
        formular.columnconfigure(1, weight=1)

        tk.Label(
            formular,
            text="Nume curs",
            bg=TEMA["fundal_card"],
            fg=TEMA["text_pal"],
        ).grid(row=0, column=0, sticky="w")
        tk.Label(
            formular,
            text="Profesor",
            bg=TEMA["fundal_card"],
            fg=TEMA["text_pal"],
        ).grid(row=1, column=0, sticky="w", pady=(8, 0))

        self.camp_curs = tk.Entry(
            formular,
            bg=TEMA["fundal_intrare"],
            fg=TEMA["text_intrare"],
            relief="flat",
            highlightthickness=1,
            highlightbackground=TEMA["contur_card"],
        )
        self.camp_profesor = tk.Entry(
            formular,
            bg=TEMA["fundal_intrare"],
            fg=TEMA["text_intrare"],
            relief="flat",
            highlightthickness=1,
            highlightbackground=TEMA["contur_card"],
        )
        self.camp_curs.grid(row=0, column=1, sticky="ew", padx=(12, 0))
        self.camp_profesor.grid(row=1, column=1, sticky="ew", padx=(12, 0), pady=(8, 0))

        buton_adauga = tk.Button(
            formular,
            text="Adauga curs",
            command=self._adauga_curs,
            bg=TEMA["accent_secundar"],
            fg=TEMA["text_deschis"],
            relief="flat",
            padx=12,
            pady=6,
        )
        buton_adauga.grid(row=0, column=2, rowspan=2, padx=(12, 0))

        titlu_lista = tk.Label(
            continut,
            text="Cursuri salvate",
            font=("Segoe UI", 12, "bold"),
            bg=TEMA["fundal_card"],
            fg=TEMA["text_inchis"],
        )
        titlu_lista.grid(row=2, column=0, sticky="w")

        cadru_lista = tk.Frame(continut, bg=TEMA["fundal_card"])
        cadru_lista.grid(row=3, column=0, sticky="nsew", pady=(6, 0))
        cadru_lista.columnconfigure(0, weight=1)

        self.lista_cursuri = tk.Listbox(
            cadru_lista,
            width=42,
            height=7,
            bg=TEMA["fundal_lista"],
            fg=TEMA["text_lista"],
            highlightthickness=1,
            highlightbackground=TEMA["contur_card"],
        )
        self.lista_cursuri.pack(side="left", fill="both", expand=True, padx=(0, 6))

        scrollbar = tk.Scrollbar(cadru_lista, command=self.lista_cursuri.yview)
        scrollbar.pack(side="left", fill="y")
        self.lista_cursuri.config(yscrollcommand=scrollbar.set)

        butoane = tk.Frame(continut, bg=TEMA["fundal_card"])
        butoane.grid(row=4, column=0, sticky="ew", pady=(12, 0))
        tk.Button(
            butoane,
            text="Sterge selectia",
            command=self._sterge_curs,
            bg=TEMA["accent_roz"],
            fg=TEMA["text_deschis"],
            relief="flat",
            padx=12,
            pady=6,
        ).pack(side="left")
        tk.Button(
            butoane,
            text="Inapoi la meniu",
            command=lambda: self.aplicatie.afiseaza_ecran("meniu_principal"),
            bg=TEMA["text_inchis"],
            fg=TEMA["text_deschis"],
            relief="flat",
            padx=12,
            pady=6,
        ).pack(side="right")

    def on_show(self):
        self._reincarca_lista()

    def _reincarca_lista(self):
        self.lista_cursuri.delete(0, tk.END)
        for curs in self.aplicatie.cursuri:
            self.lista_cursuri.insert(tk.END, f"{curs['curs']} - {curs['profesor']}")

    def _adauga_curs(self):
        curs = self.camp_curs.get().strip()
        profesor = self.camp_profesor.get().strip()
        if not curs or not profesor:
            messagebox.showwarning("Date incomplete", "Completeaza numele cursului si profesorul.")
            return
        self.aplicatie.cursuri.append({"curs": curs, "profesor": profesor})
        salveaza_cursuri(self.aplicatie.cursuri)
        self.camp_curs.delete(0, tk.END)
        self.camp_profesor.delete(0, tk.END)
        self._reincarca_lista()

    def _sterge_curs(self):
        selectie = self.lista_cursuri.curselection()
        if not selectie:
            messagebox.showinfo("Stergere", "Nu ai selectat nimic.")
            return
        index = selectie[0]
        del self.aplicatie.cursuri[index]
        salveaza_cursuri(self.aplicatie.cursuri)
        self._reincarca_lista()
