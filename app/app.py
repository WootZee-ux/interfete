"""Aplicatia principala Tkinter."""
import tkinter as tk

from app.constants import APP_TITLE, THEME
from app.data import load_courses, load_quiz_questions
from app.screens.login import LoginScreen
from app.screens.main_menu import MainMenuScreen
from app.screens.data_management import DataManagementScreen
from app.screens.quiz import QuizScreen
from app.screens.quiz_management import QuizManagementScreen
from app.screens.help import HelpScreen


class App(tk.Tk):
    """Aplicatia principala."""

    def __init__(self):
        super().__init__()
        self.configure(bg=THEME["app_bg"])
        self.title(APP_TITLE)
        self.geometry("520x460")
        self.minsize(520, 460)
        self.resizable(False, False)

        self.courses = load_courses()
        self.quiz_questions = load_quiz_questions()

        self.screens = {}
        container = tk.Frame(self, bg=THEME["app_bg"])
        container.pack(fill="both", expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self._init_screens(container)
        self.show_screen("login")

    def _init_screens(self, container):
        self.screens = {
            "login": LoginScreen(container, self),
            "main_menu": MainMenuScreen(container, self),
            "data": DataManagementScreen(container, self),
            "quiz": QuizScreen(container, self),
            "quiz_management": QuizManagementScreen(container, self),
            "help": HelpScreen(container, self),
        }
        for screen in self.screens.values():
            screen.grid(row=0, column=0, sticky="nsew")

    def show_screen(self, name):
        screen = self.screens[name]
        screen.tkraise()
        self.title(APP_TITLE)
        screen.on_show()
