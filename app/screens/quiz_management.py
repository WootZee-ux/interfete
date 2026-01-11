"""Ecran de gestionare a intrebarilor pentru quiz."""
from tkinter import messagebox
import tkinter as tk

from app.constants import THEME
from app.data import save_quiz_questions
from app.screens.base import BaseScreen


class QuizManagementScreen(BaseScreen):
    """Ecran de gestionare a intrebarilor pentru quiz."""

    def __init__(self, master, app):
        super().__init__(master, app, bg=THEME["info_bg"])
        self._build_ui()

    def _build_ui(self):
        title = tk.Label(self, text="Gestionare Quiz", font=("Helvetica", 18, "bold"), bg=THEME["info_bg"])
        title.pack(pady=15)

        form = tk.Frame(self, bg=THEME["info_bg"])
        form.pack(pady=5)

        tk.Label(form, text="Intrebare:", bg=THEME["info_bg"]).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        tk.Label(form, text="Optiuni (cu virgula):", bg=THEME["info_bg"]).grid(
            row=1, column=0, sticky="e", padx=5, pady=5
        )
        tk.Label(form, text="Raspuns corect:", bg=THEME["info_bg"]).grid(
            row=2, column=0, sticky="e", padx=5, pady=5
        )

        self.question_entry = tk.Entry(form, width=40)
        self.options_entry = tk.Entry(form, width=40)
        self.answer_entry = tk.Entry(form, width=40)

        self.question_entry.grid(row=0, column=1, padx=5, pady=5)
        self.options_entry.grid(row=1, column=1, padx=5, pady=5)
        self.answer_entry.grid(row=2, column=1, padx=5, pady=5)

        add_btn = tk.Button(form, text="Adauga", command=self._add_question, bg="#43a047", fg="white")
        add_btn.grid(row=0, column=2, rowspan=3, padx=10)

        list_frame = tk.Frame(self, bg=THEME["info_bg"])
        list_frame.pack(pady=10)

        self.question_list = tk.Listbox(list_frame, width=48, height=6)
        self.question_list.pack(side="left", padx=(0, 5))

        scrollbar = tk.Scrollbar(list_frame, command=self.question_list.yview)
        scrollbar.pack(side="left", fill="y")
        self.question_list.config(yscrollcommand=scrollbar.set)

        btns = tk.Frame(self, bg=THEME["info_bg"])
        btns.pack(pady=5)
        tk.Button(btns, text="Sterge selectia", command=self._remove_question).pack(side="left", padx=5)
        tk.Button(btns, text="Inapoi la meniu", command=lambda: self.app.show_screen("main_menu")).pack(
            side="left", padx=5
        )

    def on_show(self):
        self._refresh_list()

    def _refresh_list(self):
        self.question_list.delete(0, tk.END)
        for question in self.app.quiz_questions:
            preview = question["question"]
            self.question_list.insert(tk.END, preview)

    def _add_question(self):
        question_text = self.question_entry.get().strip()
        options_text = self.options_entry.get().strip()
        answer_text = self.answer_entry.get().strip()
        if not question_text or not options_text or not answer_text:
            messagebox.showwarning("Date incomplete", "Completeaza intrebarea, optiunile si raspunsul corect.")
            return
        options = [item.strip() for item in options_text.split(",") if item.strip()]
        if len(options) < 2:
            messagebox.showwarning("Optiuni insuficiente", "Introdu cel putin doua optiuni separate prin virgula.")
            return
        if answer_text not in options:
            messagebox.showwarning("Raspuns invalid", "Raspunsul corect trebuie sa fie unul dintre optiuni.")
            return
        self.app.quiz_questions.append(
            {
                "question": question_text,
                "options": options,
                "answer": answer_text,
            }
        )
        save_quiz_questions(self.app.quiz_questions)
        self.question_entry.delete(0, tk.END)
        self.options_entry.delete(0, tk.END)
        self.answer_entry.delete(0, tk.END)
        self._refresh_list()

    def _remove_question(self):
        selection = self.question_list.curselection()
        if not selection:
            messagebox.showinfo("Stergere", "Nu ai selectat nimic.")
            return
        index = selection[0]
        del self.app.quiz_questions[index]
        save_quiz_questions(self.app.quiz_questions)
        self._refresh_list()
