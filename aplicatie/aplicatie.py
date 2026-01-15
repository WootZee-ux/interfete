"""Aplicatia principala Tkinter."""
import tkinter as tk

from aplicatie.constante import TITLU_APLICATIE, TEMA
from aplicatie.date import incarca_chestionar, incarca_cursuri
from aplicatie.ecrane.ajutor import EcranAjutor
from aplicatie.ecrane.autentificare import EcranAutentificare
from aplicatie.ecrane.chestionar import EcranChestionar
from aplicatie.ecrane.gestionare_chestionar import EcranGestionareChestionar
from aplicatie.ecrane.gestionare_cursuri import EcranGestionareCursuri
from aplicatie.ecrane.meniu_principal import EcranMeniuPrincipal


class Aplicatie(tk.Tk):
    """Aplicatia principala."""

    def __init__(self):
        super().__init__()
        self.configure(bg=TEMA["fundal_aplicatie"])
        self.title(TITLU_APLICATIE)
        self.geometry("520x460")
        self.minsize(520, 460)
        self.resizable(False, False)

        self.cursuri = incarca_cursuri()
        self.intrebari_chestionar = incarca_chestionar()

        self.ecrane = {}
        container = tk.Frame(self, bg=TEMA["fundal_aplicatie"])
        container.pack(fill="both", expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self._init_ecrane(container)
        self.afiseaza_ecran("autentificare")

    def _init_ecrane(self, container):
        self.ecrane = {
            "autentificare": EcranAutentificare(container, self),
            "meniu_principal": EcranMeniuPrincipal(container, self),
            "cursuri": EcranGestionareCursuri(container, self),
            "chestionar": EcranChestionar(container, self),
            "gestionare_chestionar": EcranGestionareChestionar(container, self),
            "ajutor": EcranAjutor(container, self),
        }
        for ecran in self.ecrane.values():
            ecran.grid(row=0, column=0, sticky="nsew")

    def afiseaza_ecran(self, nume):
        ecran = self.ecrane[nume]
        ecran.tkraise()
        self.title(TITLU_APLICATIE)
        ecran.on_show()
