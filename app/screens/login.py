"""Ecran de autentificare."""
from tkinter import messagebox
import tkinter as tk

from app.constants import THEME
from app.screens.base import BaseScreen


class LoginScreen(BaseScreen):
    """Ecran de autentificare."""

    def __init__(self, master, app):
        super().__init__(master, app, bg=THEME["login_bg"])
        self._build_ui()

    def _build_ui(self):
        title = tk.Label(
            self,
            text="Autentificare",
            font=("Helvetica", 18, "bold"),
            bg=THEME["login_bg"],
        )
        title.pack(pady=20)

        form = tk.Frame(self, bg=THEME["login_bg"])
        form.pack(pady=10)

        tk.Label(form, text="Utilizator:", bg=THEME["login_bg"]).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        tk.Label(form, text="Parola:", bg=THEME["login_bg"]).grid(row=1, column=0, sticky="e", padx=5, pady=5)

        self.username_entry = tk.Entry(form)
        self.password_entry = tk.Entry(form, show="*")
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        login_btn = tk.Button(self, text="Autentificare", command=self._handle_login, bg="#4caf50", fg="white")
        login_btn.pack(pady=10)

        info = tk.Label(
            self,
            text="Introdu datele tale pentru acces.",
            bg=THEME["login_bg"],
            fg="#555",
        )
        info.pack(pady=5)

    def _handle_login(self):
        if not self.username_entry.get().strip():
            messagebox.showwarning("Autentificare", "Introduce un utilizator.")
            return
        self.app.show_screen("main_menu")
