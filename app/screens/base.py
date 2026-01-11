"""Clase comune pentru ecrane."""
import tkinter as tk


class BaseScreen(tk.Frame):
    """Clasa de baza pentru ecrane."""

    def __init__(self, master, app, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app

    def on_show(self):
        """Hook apelat cand ecranul devine activ."""
