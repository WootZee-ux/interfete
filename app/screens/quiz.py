"""Ecran de test grila."""
from tkinter import messagebox
import tkinter as tk

from app.constants import FONTS, THEME
from app.screens.base import BaseScreen


class QuizScreen(BaseScreen):
    """Ecran de test grila."""

    def __init__(self, master, app):
        super().__init__(master, app, bg=THEME["quiz_bg"])
        self.answer_var = tk.StringVar(value="")
        self.current_question = 0
        self.score = 0
        self._build_ui()

    def _build_ui(self):
        header = tk.Frame(self, bg=THEME["quiz_bg"], padx=20, pady=15)
        header.pack(fill="x")
        tk.Label(header, text="Test Grila", font=FONTS["title"], bg=THEME["quiz_bg"]).pack(anchor="w")
        self.progress_label = tk.Label(
            header,
            text="Intrebarea 1/1",
            font=FONTS["small"],
            bg=THEME["quiz_bg"],
            fg=THEME["text_muted"],
        )
        self.progress_label.pack(anchor="w", pady=(4, 0))

        card = tk.Frame(self, bg=THEME["panel_bg"], padx=16, pady=14, highlightbackground=THEME["outline"])
        card.pack(padx=25, pady=10, fill="both", expand=True)
        card.configure(highlightthickness=1)

        self.question_label = tk.Label(
            card,
            text="",
            bg=THEME["panel_bg"],
            font=FONTS["subtitle"],
            wraplength=420,
            justify="left",
        )
        self.question_label.pack(pady=10, anchor="w")

        self.options_frame = tk.Frame(card, bg=THEME["panel_bg"])
        self.options_frame.pack(pady=5, anchor="w", fill="x")

        self.feedback_label = tk.Label(card, text="", bg=THEME["panel_bg"], fg="#4a148c", font=FONTS["body"])
        self.feedback_label.pack(pady=5, anchor="w")

        score_panel = tk.Frame(self, bg=THEME["quiz_bg"])
        score_panel.pack(pady=(0, 5))
        self.score_label = tk.Label(
            score_panel,
            text="Scor curent: 0",
            bg=THEME["quiz_bg"],
            fg=THEME["text_muted"],
            font=FONTS["small"],
        )
        self.score_label.pack()

        btn_frame = tk.Frame(self, bg=THEME["quiz_bg"])
        btn_frame.pack(pady=10)

        self.submit_btn = tk.Button(
            btn_frame,
            text="Verifica raspunsul",
            command=self._submit,
            bg=THEME["accent"],
            fg="white",
        )
        self.submit_btn.pack(side="left", padx=5)

        self.next_btn = tk.Button(
            btn_frame,
            text="Urmatoarea intrebare",
            command=self._next_question,
            bg=THEME["accent_alt"],
            fg="white",
        )
        self.next_btn.pack(side="left", padx=5)

        reset_btn = tk.Button(
            btn_frame,
            text="Reia testul",
            command=self._reset_quiz,
        )
        reset_btn.pack(side="left", padx=5)

        tk.Button(self, text="Inapoi la meniu", command=lambda: self.app.show_screen("main_menu")).pack(pady=5)

    def on_show(self):
        self._reset_quiz()

    def _load_question(self):
        question = self.app.quiz_questions[self.current_question]
        self.answer_var = tk.StringVar(value="__fara_selectie__")
        self.question_label.config(text=f"{self.current_question + 1}. {question['question']}")
        self.progress_label.config(text=f"Intrebarea {self.current_question + 1}/{len(self.app.quiz_questions)}")
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        for option in question["options"]:
            tk.Radiobutton(
                self.options_frame,
                text=option,
                value=option,
                variable=self.answer_var,
                bg=THEME["panel_bg"],
                selectcolor="white",
                anchor="w",
            ).pack(anchor="w", padx=20, fill="x")
        self.feedback_label.config(text="")

    def _submit(self):
        if not self.answer_var.get():
            messagebox.showwarning("Raspuns", "Selecteaza un raspuns.")
            return
        correct = self.app.quiz_questions[self.current_question]["answer"]
        if self.answer_var.get() == correct:
            self.score += 1
            self.feedback_label.config(text="Corect!", fg="#2e7d32")
        else:
            self.feedback_label.config(text=f"Gresit. Raspuns corect: {correct}", fg="#c62828")
        self.score_label.config(text=f"Scor curent: {self.score}")

    def _next_question(self):
        if self.current_question < len(self.app.quiz_questions) - 1:
            self.current_question += 1
            self._load_question()
        else:
            messagebox.showinfo("Rezultat final", f"Scor: {self.score}/{len(self.app.quiz_questions)}")
            self._reset_quiz()

    def _reset_quiz(self):
        self.current_question = 0
        self.score = 0
        self.score_label.config(text="Scor curent: 0")
        self._load_question()
