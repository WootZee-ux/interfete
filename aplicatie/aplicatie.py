"""Aplicatia principala Tkinter care gestioneaza navigarea intre ecrane."""
import tkinter as tk

from aplicatie.constante import TITLU_APLICATIE, TEMA
from aplicatie.date import incarca_activitati, incarca_chestionar, incarca_cursuri, incarca_profil, incarca_utilizatori
from aplicatie.ecrane.ajutor import EcranAjutor
from aplicatie.ecrane.adauga_activitate import EcranAdaugaActivitate
from aplicatie.ecrane.autentificare import EcranAutentificare
from aplicatie.ecrane.calendar import EcranCalendar
from aplicatie.ecrane.chestionar import EcranChestionar
from aplicatie.ecrane.editeaza_profil import EcranEditeazaProfil
from aplicatie.ecrane.gestionare_chestionar import EcranGestionareChestionar
from aplicatie.ecrane.gestionare_cursuri import EcranGestionareCursuri
from aplicatie.ecrane.gestionare_utilizatori import EcranGestionareUtilizatori
from aplicatie.ecrane.informatii import EcranInformatii
from aplicatie.ecrane.meniu_principal import EcranMeniuPrincipal
from aplicatie.ecrane.profil import EcranProfil


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
        self.activitati = incarca_activitati()
        self.utilizatori = incarca_utilizatori()
        self.profil = incarca_profil()

        # Container comun in care sunt plasate toate ecranele.
        self.ecrane = {}
        container = tk.Frame(self, bg=TEMA["fundal_aplicatie"])
        container.pack(fill="both", expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self._init_ecrane(container)
        self.afiseaza_ecran("autentificare")

    def _init_ecrane(self, container):
        # Initializam ecranele o singura data pentru a pastra starea locala.
        self.ecrane = {
            "autentificare": EcranAutentificare(container, self),
            "meniu_principal": EcranMeniuPrincipal(container, self),
            "cursuri": EcranGestionareCursuri(container, self),
            "chestionar": EcranChestionar(container, self),
            "gestionare_chestionar": EcranGestionareChestionar(container, self),
            "informatii": EcranInformatii(container, self),
            "profil": EcranProfil(container, self),
            "calendar": EcranCalendar(container, self),
            "ajutor": EcranAjutor(container, self),
            "adauga_activitate": EcranAdaugaActivitate(container, self),
            "editeaza_profil": EcranEditeazaProfil(container, self),
            "gestionare_utilizatori": EcranGestionareUtilizatori(container, self),
        }
        for ecran in self.ecrane.values():
            ecran.grid(row=0, column=0, sticky="nsew")

    def afiseaza_ecran(self, nume):
        ecran = self.ecrane[nume]
        ecran.tkraise()
        self.title(TITLU_APLICATIE)
        ecran.on_show()
