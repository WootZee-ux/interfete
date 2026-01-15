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
        self.build_header("Test Grila", "Raspunde corect pentru scor maxim", icon="📝")
        content = self.build_card()

        self.progress_label = tk.Label(
            content,
            text="",
            bg=THEME["card_bg"],
            fg=THEME["text_muted"],
        )
        self.progress_label.pack(anchor="w")

        self.question_label = tk.Label(
            content,
            text="",
            bg=THEME["card_bg"],
            fg=THEME["text_dark"],
            font=("Segoe UI", 12, "bold"),
            wraplength=420,
            justify="left",
        )
        self.question_label.pack(pady=(8, 12), anchor="w")

        self.options_frame = tk.Frame(content, bg=THEME["card_bg"])
        self.options_frame.pack(pady=5, anchor="w", fill="x")

        self.feedback_label = tk.Label(content, text="", bg=THEME["card_bg"], fg=THEME["accent_purple"])
        self.feedback_label.pack(pady=(0, 6))

        btn_frame = tk.Frame(content, bg=THEME["card_bg"])
        btn_frame.pack(pady=10, fill="x")

        self.submit_btn = tk.Button(
            btn_frame,
            text="Trimite raspuns",
            command=self._submit,
            bg=THEME["accent_primary"],
            fg=THEME["text_dark"],
            relief="flat",
            padx=12,
            pady=6,
        )
        self.submit_btn.pack(side="left")

        self.next_btn = tk.Button(
            btn_frame,
            text="Urmatoarea intrebare",
            command=self._next_question,
            bg=THEME["accent_secondary"],
            fg=THEME["text_light"],
            relief="flat",
            padx=12,
            pady=6,
        )
        self.next_btn.pack(side="left", padx=8)

        tk.Button(
            btn_frame,
            text="Inapoi la meniu",
            command=lambda: self.app.show_screen("main_menu"),
            bg=THEME["text_dark"],
            fg=THEME["text_light"],
            relief="flat",
            padx=12,
            pady=6,
        ).pack(side="right")

    def on_show(self):
        self.current_question = 0
        self.score = 0
        self._load_question()

    def _load_question(self):
        question = self.app.quiz_questions[self.current_question]
        self.answer_var = tk.StringVar(value="__fara_selectie__")
        self.progress_label.config(
            text=f"Intrebarea {self.current_question + 1} din {len(self.app.quiz_questions)}"
        )
        self.question_label.config(text=question["question"])
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        for option in question["options"]:
            tk.Radiobutton(
                self.options_frame,
                text=option,
                value=option,
                variable=self.answer_var,
                bg=THEME["card_bg"],
                fg=THEME["text_dark"],
                selectcolor=THEME["accent_primary"],
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

    def _next_question(self):
        if self.current_question < len(self.app.quiz_questions) - 1:
            self.current_question += 1
            self._load_question()
        else:
            messagebox.showinfo("Rezultat final", f"Scor: {self.score}/{len(self.app.quiz_questions)}")
            self.current_question = 0
            self._load_question()
