"""Ecran pentru gestionarea utilizatorilor aplicatiei."""
from tkinter import messagebox
import tkinter as tk

from aplicatie.constante import TEMA
from aplicatie.date import salveaza_utilizatori
from aplicatie.ecrane.baza import EcranBaza


class EcranGestionareUtilizatori(EcranBaza):
    """Ecran pentru adaugarea si stergerea utilizatorilor."""

    def __init__(self, master, aplicatie):
        super().__init__(master, aplicatie, bg=TEMA["fundal_date"])
        self.camp_nume = None
        self.camp_rol = None
        self.camp_email = None
        self.lista_utilizatori = None
        self._construieste_ui()

    def _construieste_ui(self):
        self.build_header("Gestionare utilizatori", "Adauga si administreaza conturi", icon="👥")
        continut = self.build_card()
        continut.columnconfigure(1, weight=1)

        tk.Label(
            continut,
            text="Nume",
            bg=TEMA["fundal_card"],
            fg=TEMA["text_pal"],
        ).grid(row=0, column=0, sticky="w")
        tk.Label(
            continut,
            text="Rol",
            bg=TEMA["fundal_card"],
            fg=TEMA["text_pal"],
        ).grid(row=1, column=0, sticky="w", pady=(8, 0))
        tk.Label(
            continut,
            text="Email",
            bg=TEMA["fundal_card"],
            fg=TEMA["text_pal"],
        ).grid(row=2, column=0, sticky="w", pady=(8, 0))

        self.camp_nume = tk.Entry(
            continut,
            bg=TEMA["fundal_intrare"],
            fg=TEMA["text_intrare"],
            relief="flat",
            highlightthickness=1,
            highlightbackground=TEMA["contur_card"],
        )
        self.camp_rol = tk.Entry(
            continut,
            bg=TEMA["fundal_intrare"],
            fg=TEMA["text_intrare"],
            relief="flat",
            highlightthickness=1,
            highlightbackground=TEMA["contur_card"],
        )
        self.camp_email = tk.Entry(
            continut,
            bg=TEMA["fundal_intrare"],
            fg=TEMA["text_intrare"],
            relief="flat",
            highlightthickness=1,
            highlightbackground=TEMA["contur_card"],
        )
        self.camp_nume.grid(row=0, column=1, sticky="ew", padx=(12, 0))
        self.camp_rol.grid(row=1, column=1, sticky="ew", padx=(12, 0), pady=(8, 0))
        self.camp_email.grid(row=2, column=1, sticky="ew", padx=(12, 0), pady=(8, 0))

        tk.Button(
            continut,
            text="Adauga utilizator",
            command=self._adauga_utilizator,
            bg=TEMA["accent_secundar"],
            fg=TEMA["text_deschis"],
            relief="flat",
            padx=12,
            pady=6,
        ).grid(row=0, column=2, rowspan=3, padx=(12, 0))

        tk.Label(
            continut,
            text="Utilizatori existenti",
            font=("Segoe UI", 12, "bold"),
            bg=TEMA["fundal_card"],
            fg=TEMA["text_inchis"],
        ).grid(row=3, column=0, columnspan=3, sticky="w", pady=(16, 6))

        cadru_lista = tk.Frame(continut, bg=TEMA["fundal_card"])
        cadru_lista.grid(row=4, column=0, columnspan=3, sticky="nsew")
        cadru_lista.columnconfigure(0, weight=1)

        self.lista_utilizatori = tk.Listbox(
            cadru_lista,
            height=6,
            bg=TEMA["fundal_lista"],
            fg=TEMA["text_lista"],
            highlightthickness=1,
            highlightbackground=TEMA["contur_card"],
        )
        self.lista_utilizatori.pack(side="left", fill="both", expand=True, padx=(0, 6))

        scrollbar = tk.Scrollbar(cadru_lista, command=self.lista_utilizatori.yview)
        scrollbar.pack(side="left", fill="y")
        self.lista_utilizatori.config(yscrollcommand=scrollbar.set)

        actiuni = tk.Frame(continut, bg=TEMA["fundal_card"])
        actiuni.grid(row=5, column=0, columnspan=3, sticky="ew", pady=(12, 0))
        tk.Button(
            actiuni,
            text="Sterge selectia",
            command=self._sterge_utilizator,
            bg=TEMA["accent_roz"],
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
        self._reincarca_lista()

    def _reincarca_lista(self):
        self.lista_utilizatori.delete(0, tk.END)
        for utilizator in self.aplicatie.utilizatori:
            self.lista_utilizatori.insert(
                tk.END, f"{utilizator['nume']} ({utilizator['rol']}) - {utilizator['email']}"
            )

    def _adauga_utilizator(self):
        nume = self.camp_nume.get().strip()
        rol = self.camp_rol.get().strip()
        email = self.camp_email.get().strip()
        if not nume or not rol or not email:
            messagebox.showwarning("Date incomplete", "Completeaza numele, rolul si emailul.")
            return
        self.aplicatie.utilizatori.append({"nume": nume, "rol": rol, "email": email})
        salveaza_utilizatori(self.aplicatie.utilizatori)
        self.camp_nume.delete(0, tk.END)
        self.camp_rol.delete(0, tk.END)
        self.camp_email.delete(0, tk.END)
        self._reincarca_lista()

    def _sterge_utilizator(self):
        selectie = self.lista_utilizatori.curselection()
        if not selectie:
            messagebox.showinfo("Stergere", "Nu ai selectat niciun utilizator.")
            return
        index = selectie[0]
        del self.aplicatie.utilizatori[index]
        salveaza_utilizatori(self.aplicatie.utilizatori)
        self._reincarca_lista()
