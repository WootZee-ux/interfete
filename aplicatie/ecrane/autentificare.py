"""Ecran de autentificare."""
from tkinter import messagebox, simpledialog
import tkinter as tk

from aplicatie.autentificare import actualizeaza_parola, verifica_credentiale
from aplicatie.constante import TEMA
from aplicatie.ecrane.baza import EcranBaza


class EcranAutentificare(EcranBaza):
    """Ecran de autentificare."""

    def __init__(self, master, aplicatie):
        super().__init__(master, aplicatie, bg=TEMA["fundal_autentificare"])
        self._construieste_ui()

    def _construieste_ui(self):
        self.build_header("Autentificare", "Acces rapid la portalul cursurilor", icon="🔐")
        continut = self.build_card()
        continut.columnconfigure(0, weight=1)
        continut.columnconfigure(1, weight=1)

        panou_info = tk.Frame(continut, bg=TEMA["fundal_card"])
        panou_info.grid(row=0, column=0, sticky="nsew", padx=(0, 16))
        tk.Label(
            panou_info,
            text="Bine ai venit!",
            font=("Segoe UI", 16, "bold"),
            bg=TEMA["fundal_card"],
            fg=TEMA["text_inchis"],
        ).pack(anchor="w", pady=(0, 6))
        tk.Label(
            panou_info,
            text="Autentifica-te pentru a gestiona cursurile, testele si resursele academice.",
            bg=TEMA["fundal_card"],
            fg=TEMA["text_pal"],
            wraplength=190,
            justify="left",
        ).pack(anchor="w")
        tk.Label(
            panou_info,
            text="• Salvare locala\n• Chestionare rapide\n• Navigare intuitiva",
            bg=TEMA["fundal_card"],
            fg=TEMA["text_inchis"],
            justify="left",
            pady=12,
        ).pack(anchor="w")

        formular = tk.Frame(continut, bg=TEMA["fundal_card"])
        formular.grid(row=0, column=1, sticky="nsew")

        tk.Label(
            formular,
            text="Utilizator",
            bg=TEMA["fundal_card"],
            fg=TEMA["text_pal"],
            font=("Segoe UI", 9, "bold"),
        ).grid(row=0, column=0, sticky="w")
        self.camp_utilizator = tk.Entry(
            formular,
            bg=TEMA["fundal_intrare"],
            fg=TEMA["text_intrare"],
            relief="flat",
            highlightthickness=1,
            highlightbackground=TEMA["contur_card"],
        )
        self.camp_utilizator.grid(row=1, column=0, sticky="ew", pady=(4, 12))

        tk.Label(
            formular,
            text="Parola",
            bg=TEMA["fundal_card"],
            fg=TEMA["text_pal"],
            font=("Segoe UI", 9, "bold"),
        ).grid(row=2, column=0, sticky="w")
        self.camp_parola = tk.Entry(
            formular,
            show="*",
            bg=TEMA["fundal_intrare"],
            fg=TEMA["text_intrare"],
            relief="flat",
            highlightthickness=1,
            highlightbackground=TEMA["contur_card"],
        )
        self.camp_parola.grid(row=3, column=0, sticky="ew", pady=(4, 16))

        formular.columnconfigure(0, weight=1)
        buton_autentificare = tk.Button(
            formular,
            text="Intra in cont",
            command=self._gestioneaza_autentificare,
            bg=TEMA["accent_principal"],
            fg=TEMA["text_inchis"],
            relief="flat",
            padx=12,
            pady=6,
        )
        buton_autentificare.grid(row=4, column=0, sticky="ew")

        buton_parola = tk.Button(
            formular,
            text="Schimba parola",
            command=self._gestioneaza_schimbare_parola,
            bg=TEMA["accent_secundar"],
            fg=TEMA["text_deschis"],
            relief="flat",
            padx=12,
            pady=6,
        )
        buton_parola.grid(row=5, column=0, sticky="ew", pady=(10, 0))

    def _gestioneaza_autentificare(self):
        utilizator = self.camp_utilizator.get().strip()
        parola = self.camp_parola.get()
        if not utilizator:
            messagebox.showwarning("Autentificare", "Introduce un utilizator.")
            return
        if not parola:
            messagebox.showwarning("Autentificare", "Introduce o parola.")
            return
        if not verifica_credentiale(utilizator, parola):
            messagebox.showerror("Autentificare", "Utilizator sau parola incorecta.")
            return
        self.aplicatie.afiseaza_ecran("meniu_principal")

    def _gestioneaza_schimbare_parola(self):
        utilizator = simpledialog.askstring("Setare parola", "Utilizator:", parent=self)
        if not utilizator:
            return
        parola_noua = simpledialog.askstring("Setare parola", "Parola noua:", show="*", parent=self)
        if not parola_noua:
            return
        confirma_parola = simpledialog.askstring(
            "Setare parola",
            "Confirma parola:",
            show="*",
            parent=self,
        )
        if not confirma_parola:
            return
        if parola_noua != confirma_parola:
            messagebox.showerror("Setare parola", "Parolele nu coincid.")
            return
        if actualizeaza_parola(utilizator.strip(), parola_noua):
            messagebox.showinfo("Setare parola", "Parola a fost actualizata cu succes.")
        else:
            messagebox.showerror("Setare parola", "Utilizatorul nu este definit in fisier.")
