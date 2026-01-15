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
        self.build_header("Autentificare", "Acces rapid la portalul cursurilor", icon="🔐")
        content = self.build_card()
        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=1)

        info_panel = tk.Frame(content, bg=THEME["card_bg"])
        info_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 16))
        tk.Label(
            info_panel,
            text="Bine ai venit!",
            font=("Segoe UI", 16, "bold"),
            bg=THEME["card_bg"],
            fg=THEME["text_dark"],
        ).pack(anchor="w", pady=(0, 6))
        tk.Label(
            info_panel,
            text="Autentifica-te pentru a gestiona cursurile, testele si resursele academice.",
            bg=THEME["card_bg"],
            fg=THEME["text_muted"],
            wraplength=190,
            justify="left",
        ).pack(anchor="w")
        tk.Label(
            info_panel,
            text="• Salvare locala\n• Quiz-uri rapide\n• Navigare intuitiva",
            bg=THEME["card_bg"],
            fg=THEME["text_dark"],
            justify="left",
            pady=12,
        ).pack(anchor="w")

        form = tk.Frame(content, bg=THEME["card_bg"])
        form.grid(row=0, column=1, sticky="nsew")

        tk.Label(
            form,
            text="Utilizator",
            bg=THEME["card_bg"],
            fg=THEME["text_muted"],
            font=("Segoe UI", 9, "bold"),
        ).grid(row=0, column=0, sticky="w")
        self.username_entry = tk.Entry(
            form,
            bg=THEME["entry_bg"],
            fg=THEME["entry_fg"],
            relief="flat",
            highlightthickness=1,
            highlightbackground=THEME["card_border"],
        )
        self.username_entry.grid(row=1, column=0, sticky="ew", pady=(4, 12))

        tk.Label(
            form,
            text="Parola",
            bg=THEME["card_bg"],
            fg=THEME["text_muted"],
            font=("Segoe UI", 9, "bold"),
        ).grid(row=2, column=0, sticky="w")
        self.password_entry = tk.Entry(
            form,
            show="*",
            bg=THEME["entry_bg"],
            fg=THEME["entry_fg"],
            relief="flat",
            highlightthickness=1,
            highlightbackground=THEME["card_border"],
        )
        self.password_entry.grid(row=3, column=0, sticky="ew", pady=(4, 16))

        form.columnconfigure(0, weight=1)
        login_btn = tk.Button(
            form,
            text="Intra in cont",
            command=self._handle_login,
            bg=THEME["accent_primary"],
            fg=THEME["text_dark"],
            relief="flat",
            padx=12,
            pady=6,
        )
        login_btn.grid(row=4, column=0, sticky="ew")

        change_password_btn = tk.Button(
            form,
            text="Schimba parola",
            command=self._handle_set_password,
            bg=THEME["accent_secondary"],
            fg=THEME["text_light"],
            relief="flat",
            padx=12,
            pady=6,
        )
        change_password_btn.grid(row=5, column=0, sticky="ew", pady=(10, 0))

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
