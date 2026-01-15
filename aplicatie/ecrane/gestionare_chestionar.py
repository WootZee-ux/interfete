"""Ecran de gestionare a intrebarilor pentru chestionar."""
from tkinter import messagebox
import tkinter as tk

from aplicatie.constante import TEMA
from aplicatie.date import salveaza_chestionar
from aplicatie.ecrane.baza import EcranBaza


class EcranGestionareChestionar(EcranBaza):
    """Ecran de gestionare a intrebarilor pentru chestionar."""

    def __init__(self, master, aplicatie):
        super().__init__(master, aplicatie, bg=TEMA["fundal_informatii"])
        self._construieste_ui()

    def _construieste_ui(self):
        self.build_header("Gestionare chestionar", "Configureaza intrebarile si optiunile", icon="🧩")
        continut = self.build_card()
        continut.columnconfigure(1, weight=1)

        tk.Label(
            continut,
            text="Intrebare noua",
            font=("Segoe UI", 12, "bold"),
            bg=TEMA["fundal_card"],
            fg=TEMA["text_inchis"],
        ).grid(row=0, column=0, columnspan=2, sticky="w")

        formular = tk.Frame(continut, bg=TEMA["fundal_card"])
        formular.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(6, 12))
        formular.columnconfigure(1, weight=1)

        tk.Label(formular, text="Intrebare", bg=TEMA["fundal_card"], fg=TEMA["text_pal"]).grid(
            row=0, column=0, sticky="w"
        )
        tk.Label(formular, text="Optiuni (cu virgula)", bg=TEMA["fundal_card"], fg=TEMA["text_pal"]).grid(
            row=1, column=0, sticky="w", pady=(8, 0)
        )
        tk.Label(formular, text="Raspuns corect", bg=TEMA["fundal_card"], fg=TEMA["text_pal"]).grid(
            row=2, column=0, sticky="w", pady=(8, 0)
        )

        self.camp_intrebare = tk.Entry(
            formular,
            bg=TEMA["fundal_intrare"],
            fg=TEMA["text_intrare"],
            relief="flat",
            highlightthickness=1,
            highlightbackground=TEMA["contur_card"],
        )
        self.camp_optiuni = tk.Entry(
            formular,
            bg=TEMA["fundal_intrare"],
            fg=TEMA["text_intrare"],
            relief="flat",
            highlightthickness=1,
            highlightbackground=TEMA["contur_card"],
        )
        self.camp_raspuns = tk.Entry(
            formular,
            bg=TEMA["fundal_intrare"],
            fg=TEMA["text_intrare"],
            relief="flat",
            highlightthickness=1,
            highlightbackground=TEMA["contur_card"],
        )

        self.camp_intrebare.grid(row=0, column=1, sticky="ew", padx=(12, 0))
        self.camp_optiuni.grid(row=1, column=1, sticky="ew", padx=(12, 0), pady=(8, 0))
        self.camp_raspuns.grid(row=2, column=1, sticky="ew", padx=(12, 0), pady=(8, 0))

        buton_adauga = tk.Button(
            formular,
            text="Adauga intrebare",
            command=self._adauga_intrebare,
            bg=TEMA["accent_succes"],
            fg=TEMA["text_deschis"],
            relief="flat",
            padx=12,
            pady=6,
        )
        buton_adauga.grid(row=0, column=2, rowspan=3, padx=(12, 0))

        tk.Label(
            continut,
            text="Intrebari existente",
            font=("Segoe UI", 12, "bold"),
            bg=TEMA["fundal_card"],
            fg=TEMA["text_inchis"],
        ).grid(row=2, column=0, columnspan=2, sticky="w")

        cadru_lista = tk.Frame(continut, bg=TEMA["fundal_card"])
        cadru_lista.grid(row=3, column=0, columnspan=2, sticky="nsew", pady=(6, 0))

        self.lista_intrebari = tk.Listbox(
            cadru_lista,
            width=48,
            height=6,
            bg=TEMA["fundal_lista"],
            fg=TEMA["text_lista"],
            highlightthickness=1,
            highlightbackground=TEMA["contur_card"],
        )
        self.lista_intrebari.pack(side="left", fill="both", expand=True, padx=(0, 6))

        scrollbar = tk.Scrollbar(cadru_lista, command=self.lista_intrebari.yview)
        scrollbar.pack(side="left", fill="y")
        self.lista_intrebari.config(yscrollcommand=scrollbar.set)

        butoane = tk.Frame(continut, bg=TEMA["fundal_card"])
        butoane.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(12, 0))
        tk.Button(
            butoane,
            text="Sterge selectia",
            command=self._sterge_intrebare,
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
        self.lista_intrebari.delete(0, tk.END)
        for intrebare in self.aplicatie.intrebari_chestionar:
            preview = intrebare["intrebare"]
            self.lista_intrebari.insert(tk.END, preview)

    def _adauga_intrebare(self):
        text_intrebare = self.camp_intrebare.get().strip()
        text_optiuni = self.camp_optiuni.get().strip()
        text_raspuns = self.camp_raspuns.get().strip()
        if not text_intrebare or not text_optiuni or not text_raspuns:
            messagebox.showwarning("Date incomplete", "Completeaza intrebarea, optiunile si raspunsul corect.")
            return
        optiuni = [item.strip() for item in text_optiuni.split(",") if item.strip()]
        if len(optiuni) < 2:
            messagebox.showwarning("Optiuni insuficiente", "Introdu cel putin doua optiuni separate prin virgula.")
            return
        if text_raspuns not in optiuni:
            messagebox.showwarning("Raspuns invalid", "Raspunsul corect trebuie sa fie unul dintre optiuni.")
            return
        self.aplicatie.intrebari_chestionar.append(
            {
                "intrebare": text_intrebare,
                "optiuni": optiuni,
                "raspuns": text_raspuns,
            }
        )
        salveaza_chestionar(self.aplicatie.intrebari_chestionar)
        self.camp_intrebare.delete(0, tk.END)
        self.camp_optiuni.delete(0, tk.END)
        self.camp_raspuns.delete(0, tk.END)
        self._reincarca_lista()

    def _sterge_intrebare(self):
        selectie = self.lista_intrebari.curselection()
        if not selectie:
            messagebox.showinfo("Stergere", "Nu ai selectat nimic.")
            return
        index = selectie[0]
        del self.aplicatie.intrebari_chestionar[index]
        salveaza_chestionar(self.aplicatie.intrebari_chestionar)
        self._reincarca_lista()
