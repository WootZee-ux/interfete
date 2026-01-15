"""Ecran de gestionare a intrebarilor pentru quiz."""
from tkinter import messagebox, ttk
import tkinter as tk

from app.constants import FONTS, THEME
from app.data import save_quiz_questions
from app.screens.base import BaseScreen


class QuizManagementScreen(BaseScreen):
    """Ecran de gestionare a intrebarilor pentru quiz."""

    def __init__(self, master, app):
        super().__init__(master, app, bg=THEME["info_bg"])
        self._build_ui()

    def _build_ui(self):
        header = tk.Frame(self, bg=THEME["info_bg"], padx=20, pady=15)
        header.pack(fill="x")
        tk.Label(header, text="Gestionare Quiz", font=FONTS["title"], bg=THEME["info_bg"]).pack(anchor="w")
        tk.Label(
            header,
            text="Defineste intrebari si raspunsuri pentru test.",
            font=FONTS["small"],
            bg=THEME["info_bg"],
            fg=THEME["text_muted"],
        ).pack(anchor="w", pady=(4, 0))

        form = tk.Frame(self, bg=THEME["panel_bg"], padx=15, pady=12, highlightbackground=THEME["outline"])
        form.pack(padx=25, pady=10, fill="x")
        form.configure(highlightthickness=1)

        tk.Label(form, text="Intrebare", bg=THEME["panel_bg"], font=FONTS["body"]).grid(
            row=0, column=0, sticky="w", padx=5, pady=5
        )
        tk.Label(form, text="Optiuni (cu virgula)", bg=THEME["panel_bg"], font=FONTS["body"]).grid(
            row=1, column=0, sticky="w", padx=5, pady=5
        )
        tk.Label(form, text="Raspuns corect", bg=THEME["panel_bg"], font=FONTS["body"]).grid(
            row=2, column=0, sticky="w", padx=5, pady=5
        )

        self.question_entry = tk.Entry(form, width=42)
        self.options_entry = tk.Entry(form, width=42)
        self.answer_entry = tk.Entry(form, width=42)

        self.question_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.options_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.answer_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        add_btn = tk.Button(form, text="Adauga intrebare", command=self._add_question, bg=THEME["accent"], fg="white")
        add_btn.grid(row=0, column=2, rowspan=3, padx=10)
        form.columnconfigure(1, weight=1)

        list_frame = tk.Frame(self, bg=THEME["panel_bg"], padx=10, pady=10, highlightbackground=THEME["outline"])
        list_frame.pack(padx=25, pady=10, fill="both", expand=True)
        list_frame.configure(highlightthickness=1)

        self.question_list = ttk.Treeview(list_frame, columns=("question", "answer"), show="headings", height=6)
        self.question_list.heading("question", text="Intrebare")
        self.question_list.heading("answer", text="Raspuns")
        self.question_list.column("question", width=260)
        self.question_list.column("answer", width=140)
        self.question_list.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame, command=self.question_list.yview)
        scrollbar.pack(side="right", fill="y")
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
        for item in self.question_list.get_children():
            self.question_list.delete(item)
        for question in self.app.quiz_questions:
            self.question_list.insert("", tk.END, values=(question["question"], question["answer"]))

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
        selection = self.question_list.selection()
        if not selection:
            messagebox.showinfo("Stergere", "Nu ai selectat nimic.")
            return
        index = self.question_list.index(selection[0])
        del self.app.quiz_questions[index]
        save_quiz_questions(self.app.quiz_questions)
        self._refresh_list()
