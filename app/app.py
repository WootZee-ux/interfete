"""Aplicatia principala Tkinter."""
import tkinter as tk

from app.constants import APP_TITLE
from app.data import DUMMY_COURSES, QUIZ_QUESTIONS
from app.screens.login import LoginScreen
from app.screens.main_menu import MainMenuScreen
from app.screens.data_management import DataManagementScreen
from app.screens.quiz import QuizScreen
from app.screens.info import InfoScreen
from app.screens.help import HelpScreen


class App(tk.Tk):
    """Aplicatia principala."""

    def __init__(self):
        super().__init__()
        self.configure(bg="#ffffff")
        self.title(APP_TITLE)
        self.geometry("560x460")
        self.resizable(False, False)

        self.courses = [course.copy() for course in DUMMY_COURSES]
        self.quiz_questions = [question.copy() for question in QUIZ_QUESTIONS]

        self.screens = {}
        container = tk.Frame(self, bg="#ffffff")
        container.pack(fill="both", expand=True)

        self._init_screens(container)
        self.show_screen("login")

    def _init_screens(self, container):
        self.screens = {
            "login": LoginScreen(container, self),
            "main_menu": MainMenuScreen(container, self),
            "data": DataManagementScreen(container, self),
            "quiz": QuizScreen(container, self),
            "info": InfoScreen(container, self),
            "help": HelpScreen(container, self),
        }
        for screen in self.screens.values():
            screen.grid(row=0, column=0, sticky="nsew")

    def show_screen(self, name):
        screen = self.screens[name]
        screen.tkraise()
        self.title(APP_TITLE)
        screen.on_show()
