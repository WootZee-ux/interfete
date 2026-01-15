"""Ecran de autentificare."""
from tkinter import messagebox, simpledialog
import tkinter as tk

from app.auth import update_password, verify_credentials
from app.constants import FONTS, THEME
from app.screens.base import BaseScreen


class LoginScreen(BaseScreen):
    """Ecran de autentificare."""

    def __init__(self, master, app):
        super().__init__(master, app, bg=THEME["login_bg"])
        self._build_ui()

    def _build_ui(self):
        header = tk.Frame(self, bg=THEME["login_bg"], padx=20, pady=15)
        header.pack(fill="x")
        tk.Label(
            header,
            text="Portal Acces",
            font=FONTS["title"],
            bg=THEME["login_bg"],
            fg=THEME["text_dark"],
        ).pack(anchor="w")
        tk.Label(
            header,
            text="Conecteaza-te pentru a continua in platforma de cursuri.",
            font=FONTS["small"],
            bg=THEME["login_bg"],
            fg=THEME["text_muted"],
        ).pack(anchor="w", pady=(4, 0))

        panel = tk.Frame(
            self,
            bg=THEME["panel_bg"],
            padx=20,
            pady=20,
            highlightbackground=THEME["outline"],
            highlightthickness=1,
        )
        panel.pack(padx=30, pady=25, fill="x")

        tk.Label(panel, text="Utilizator", font=FONTS["body"], bg=THEME["panel_bg"]).grid(
            row=0, column=0, sticky="w", pady=5
        )
        tk.Label(panel, text="Parola", font=FONTS["body"], bg=THEME["panel_bg"]).grid(
            row=2, column=0, sticky="w", pady=5
        )

        self.username_entry = tk.Entry(panel, width=28)
        self.password_entry = tk.Entry(panel, show="*", width=28)
        self.username_entry.grid(row=1, column=0, sticky="ew", pady=5)
        self.password_entry.grid(row=3, column=0, sticky="ew", pady=5)

        actions = tk.Frame(panel, bg=THEME["panel_bg"])
        actions.grid(row=4, column=0, pady=(15, 5), sticky="ew")
        login_btn = tk.Button(
            actions,
            text="Intra in cont",
            command=self._handle_login,
            bg=THEME["accent"],
            fg="white",
            width=16,
        )
        login_btn.pack(side="left", padx=(0, 10))

        change_password_btn = tk.Button(
            actions,
            text="Schimba parola",
            command=self._handle_set_password,
            bg=THEME["accent_alt"],
            fg="white",
            width=16,
        )
        change_password_btn.pack(side="left")

        info = tk.Label(
            panel,
            text="Sugestie: parola poate fi resetata din butonul dedicat.",
            bg=THEME["panel_bg"],
            fg=THEME["text_muted"],
            font=FONTS["small"],
        )
        info.grid(row=5, column=0, sticky="w", pady=(10, 0))

    def _handle_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        if not username:
            messagebox.showwarning("Autentificare", "Introduce un utilizator.")
            return
        if not password:
            messagebox.showwarning("Autentificare", "Introduce o parola.")
            return
        if not verify_credentials(username, password):
            messagebox.showerror("Autentificare", "Utilizator sau parola incorecta.")
            return
        self.app.show_screen("main_menu")

    def _handle_set_password(self):
        username = simpledialog.askstring("Setare parola", "Utilizator:", parent=self)
        if not username:
            return
        new_password = simpledialog.askstring("Setare parola", "Parola noua:", show="*", parent=self)
        if not new_password:
            return
        confirm_password = simpledialog.askstring(
            "Setare parola",
            "Confirma parola:",
            show="*",
            parent=self,
        )
        if not confirm_password:
            return
        if new_password != confirm_password:
            messagebox.showerror("Setare parola", "Parolele nu coincid.")
            return
        if update_password(username.strip(), new_password):
            messagebox.showinfo("Setare parola", "Parola a fost actualizata cu succes.")
        else:
            messagebox.showerror("Setare parola", "Utilizatorul nu este definit in fisier.")
