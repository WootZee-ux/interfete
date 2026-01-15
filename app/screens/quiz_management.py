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
        self.build_header("Gestionare Quiz", "Configureaza intrebarile si optiunile", icon="🧩")
        content = self.build_card()
        content.columnconfigure(1, weight=1)

        tk.Label(
            content,
            text="Intrebare noua",
            font=("Segoe UI", 12, "bold"),
            bg=THEME["card_bg"],
            fg=THEME["text_dark"],
        ).grid(row=0, column=0, columnspan=2, sticky="w")

        form = tk.Frame(content, bg=THEME["card_bg"])
        form.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(6, 12))
        form.columnconfigure(1, weight=1)

        tk.Label(form, text="Intrebare", bg=THEME["card_bg"], fg=THEME["text_muted"]).grid(
            row=0, column=0, sticky="w"
        )
        tk.Label(form, text="Optiuni (cu virgula)", bg=THEME["card_bg"], fg=THEME["text_muted"]).grid(
            row=1, column=0, sticky="w", pady=(8, 0)
        )
        tk.Label(form, text="Raspuns corect", bg=THEME["card_bg"], fg=THEME["text_muted"]).grid(
            row=2, column=0, sticky="w", pady=(8, 0)
        )

        self.question_entry = tk.Entry(
            form,
            bg=THEME["entry_bg"],
            fg=THEME["entry_fg"],
            relief="flat",
            highlightthickness=1,
            highlightbackground=THEME["card_border"],
        )
        self.options_entry = tk.Entry(
            form,
            bg=THEME["entry_bg"],
            fg=THEME["entry_fg"],
            relief="flat",
            highlightthickness=1,
            highlightbackground=THEME["card_border"],
        )
        self.answer_entry = tk.Entry(
            form,
            bg=THEME["entry_bg"],
            fg=THEME["entry_fg"],
            relief="flat",
            highlightthickness=1,
            highlightbackground=THEME["card_border"],
        )

        self.question_entry.grid(row=0, column=1, sticky="ew", padx=(12, 0))
        self.options_entry.grid(row=1, column=1, sticky="ew", padx=(12, 0), pady=(8, 0))
        self.answer_entry.grid(row=2, column=1, sticky="ew", padx=(12, 0), pady=(8, 0))

        add_btn = tk.Button(
            form,
            text="Adauga intrebare",
            command=self._add_question,
            bg=THEME["accent_success"],
            fg=THEME["text_light"],
            relief="flat",
            padx=12,
            pady=6,
        )
        add_btn.grid(row=0, column=2, rowspan=3, padx=(12, 0))

        tk.Label(
            content,
            text="Intrebari existente",
            font=("Segoe UI", 12, "bold"),
            bg=THEME["card_bg"],
            fg=THEME["text_dark"],
        ).grid(row=2, column=0, columnspan=2, sticky="w")

        list_frame = tk.Frame(content, bg=THEME["card_bg"])
        list_frame.grid(row=3, column=0, columnspan=2, sticky="nsew", pady=(6, 0))

        self.question_list = tk.Listbox(
            list_frame,
            width=48,
            height=6,
            bg=THEME["list_bg"],
            fg=THEME["list_fg"],
            highlightthickness=1,
            highlightbackground=THEME["card_border"],
        )
        self.question_list.pack(side="left", fill="both", expand=True, padx=(0, 6))

        scrollbar = tk.Scrollbar(list_frame, command=self.question_list.yview)
        scrollbar.pack(side="left", fill="y")
        self.question_list.config(yscrollcommand=scrollbar.set)

        btns = tk.Frame(content, bg=THEME["card_bg"])
        btns.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(12, 0))
        tk.Button(
            btns,
            text="Sterge selectia",
            command=self._remove_question,
            bg=THEME["accent_rose"],
            fg=THEME["text_light"],
            relief="flat",
            padx=12,
            pady=6,
        ).pack(side="left")
        tk.Button(
            btns,
            text="Inapoi la meniu",
            command=lambda: self.app.show_screen("main_menu"),
            bg=THEME["text_dark"],
            fg=THEME["text_light"],
            relief="flat",
            padx=12,
            pady=6,
        ).pack(side="right")

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
