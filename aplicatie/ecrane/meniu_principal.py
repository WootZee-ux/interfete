"""Ecranul principal care ofera navigare catre modulele aplicatiei."""
import tkinter as tk

from aplicatie.constante import TEMA
from aplicatie.ecrane.baza import EcranBaza


class EcranMeniuPrincipal(EcranBaza):
    """Ecran principal care ofera navigare catre module."""

    def __init__(self, master, aplicatie):
        super().__init__(master, aplicatie, bg=TEMA["fundal_meniu"])
        self._construieste_ui()

    def _construieste_ui(self):
        self.build_header("Meniu Principal", "Alege un modul pentru a continua", icon="🧭")
        continut = self.build_card()

        titlu = tk.Label(
            continut,
            text="Panou de comanda",
            font=("Segoe UI", 14, "bold"),
            bg=TEMA["fundal_card"],
            fg=TEMA["text_inchis"],
        )
        titlu.pack(anchor="w")

        grila = tk.Frame(continut, bg=TEMA["fundal_card"])
        grila.pack(fill="both", expand=True, pady=12)
        for coloana in range(2):
            grila.columnconfigure(coloana, weight=1)

        butoane = [
            ("📚 Gestionare cursuri", TEMA["accent_principal"], lambda: self.aplicatie.afiseaza_ecran("cursuri")),
            ("📝 Test grila", TEMA["accent_mov"], lambda: self.aplicatie.afiseaza_ecran("chestionar")),
            (
                "🧩 Gestionare chestionar",
                TEMA["accent_secundar"],
                lambda: self.aplicatie.afiseaza_ecran("gestionare_chestionar"),
            ),
            ("🆘 Ajutor si ghid", TEMA["accent_roz"], lambda: self.aplicatie.afiseaza_ecran("ajutor")),
        ]
        for idx, (eticheta, culoare, actiune) in enumerate(butoane):
            rand, coloana = divmod(idx, 2)
            buton = tk.Button(
                grila,
                text=eticheta,
                command=actiune,
                bg=culoare,
                fg=TEMA["text_deschis"],
                relief="flat",
                padx=12,
                pady=12,
            )
            buton.grid(row=rand, column=coloana, padx=6, pady=6, sticky="ew")

        subsol = tk.Frame(continut, bg=TEMA["fundal_card"])
        subsol.pack(fill="x", pady=(12, 0))
        tk.Label(
            subsol,
            text="Status: conectat",
            bg=TEMA["fundal_card"],
            fg=TEMA["text_pal"],
        ).pack(side="left")
        deconectare = tk.Button(
            subsol,
            text="Deconectare",
            command=lambda: self.aplicatie.afiseaza_ecran("autentificare"),
            bg=TEMA["text_inchis"],
            fg=TEMA["text_deschis"],
            relief="flat",
            padx=12,
            pady=6,
        )
        deconectare.pack(side="right")
