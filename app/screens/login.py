"""Ecran de autentificare."""
from tkinter import messagebox, simpledialog
import tkinter as tk

from app.auth import update_password, verify_credentials
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

        change_password_btn = tk.Button(
            self,
            text="Setare parola",
            command=self._handle_set_password,
            bg="#2196f3",
            fg="white",
        )
        change_password_btn.pack(pady=5)

        info = tk.Label(
            self,
            text="Introdu datele tale pentru acces.",
            bg=THEME["login_bg"],
            fg="#555",
        )
        info.pack(pady=5)

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
