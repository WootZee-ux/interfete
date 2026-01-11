"""Ecran de test grila."""
from tkinter import messagebox
import tkinter as tk

from app.constants import THEME
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
        title = tk.Label(self, text="Test Grila", font=("Helvetica", 18, "bold"), bg=THEME["quiz_bg"])
        title.pack(pady=15)

        self.question_label = tk.Label(
            self,
            text="",
            bg=THEME["quiz_bg"],
            font=("Helvetica", 12),
            wraplength=420,
            justify="left",
        )
        self.question_label.pack(pady=10)

        self.options_frame = tk.Frame(self, bg=THEME["quiz_bg"])
        self.options_frame.pack(pady=5, anchor="w")

        self.feedback_label = tk.Label(self, text="", bg=THEME["quiz_bg"], fg="#4a148c")
        self.feedback_label.pack(pady=5)

        btn_frame = tk.Frame(self, bg=THEME["quiz_bg"])
        btn_frame.pack(pady=10)

        self.submit_btn = tk.Button(btn_frame, text="Trimite raspuns", command=self._submit, bg="#9c27b0", fg="white")
        self.submit_btn.pack(side="left", padx=5)

        self.next_btn = tk.Button(btn_frame, text="Urmatoarea intrebare", command=self._next_question)
        self.next_btn.pack(side="left", padx=5)

        tk.Button(self, text="Inapoi la meniu", command=lambda: self.app.show_screen("main_menu")).pack(pady=5)

    def on_show(self):
        self.current_question = 0
        self.score = 0
        self._load_question()

    def _load_question(self):
        question = self.app.quiz_questions[self.current_question]
        self.answer_var.set("")
        self.question_label.config(text=f"{self.current_question + 1}. {question['question']}")
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        for option in question["options"]:
            tk.Radiobutton(
                self.options_frame,
                text=option,
                value=option,
                variable=self.answer_var,
                bg=THEME["quiz_bg"],
            ).pack(anchor="w", padx=20)
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

    def _next_question(self):
        if self.current_question < len(self.app.quiz_questions) - 1:
            self.current_question += 1
            self._load_question()
        else:
            messagebox.showinfo("Rezultat final", f"Scor: {self.score}/{len(self.app.quiz_questions)}")
            self.current_question = 0
            self._load_question()
