"""Ecran de gestionare a datelor (cursuri)."""
from tkinter import messagebox
import tkinter as tk

from app.constants import THEME
from app.data import save_courses
from app.screens.base import BaseScreen


class DataManagementScreen(BaseScreen):
    """Ecran de gestionare a datelor (cursuri)."""

    def __init__(self, master, app):
        super().__init__(master, app, bg=THEME["data_bg"])
        self._build_ui()

    def _build_ui(self):
        self.build_header("Gestionare Cursuri", "Adauga si actualizeaza cursurile active", icon="📚")
        content = self.build_card()
        content.columnconfigure(0, weight=1)

        form_title = tk.Label(
            content,
            text="Detalii curs",
            font=("Segoe UI", 12, "bold"),
            bg=THEME["card_bg"],
            fg=THEME["text_dark"],
        )
        form_title.grid(row=0, column=0, sticky="w")

        form = tk.Frame(content, bg=THEME["card_bg"])
        form.grid(row=1, column=0, sticky="ew", pady=(6, 12))
        form.columnconfigure(1, weight=1)

        tk.Label(
            form,
            text="Nume curs",
            bg=THEME["card_bg"],
            fg=THEME["text_muted"],
        ).grid(row=0, column=0, sticky="w")
        tk.Label(
            form,
            text="Profesor",
            bg=THEME["card_bg"],
            fg=THEME["text_muted"],
        ).grid(row=1, column=0, sticky="w", pady=(8, 0))

        self.course_entry = tk.Entry(
            form,
            bg=THEME["entry_bg"],
            fg=THEME["entry_fg"],
            relief="flat",
            highlightthickness=1,
            highlightbackground=THEME["card_border"],
        )
        self.teacher_entry = tk.Entry(
            form,
            bg=THEME["entry_bg"],
            fg=THEME["entry_fg"],
            relief="flat",
            highlightthickness=1,
            highlightbackground=THEME["card_border"],
        )
        self.course_entry.grid(row=0, column=1, sticky="ew", padx=(12, 0))
        self.teacher_entry.grid(row=1, column=1, sticky="ew", padx=(12, 0), pady=(8, 0))

        add_btn = tk.Button(
            form,
            text="Adauga curs",
            command=self._add_course,
            bg=THEME["accent_secondary"],
            fg=THEME["text_light"],
            relief="flat",
            padx=12,
            pady=6,
        )
        add_btn.grid(row=0, column=2, rowspan=2, padx=(12, 0))

        list_title = tk.Label(
            content,
            text="Cursuri salvate",
            font=("Segoe UI", 12, "bold"),
            bg=THEME["card_bg"],
            fg=THEME["text_dark"],
        )
        list_title.grid(row=2, column=0, sticky="w")

        list_frame = tk.Frame(content, bg=THEME["card_bg"])
        list_frame.grid(row=3, column=0, sticky="nsew", pady=(6, 0))
        list_frame.columnconfigure(0, weight=1)

        self.course_list = tk.Listbox(
            list_frame,
            width=42,
            height=7,
            bg=THEME["list_bg"],
            fg=THEME["list_fg"],
            highlightthickness=1,
            highlightbackground=THEME["card_border"],
        )
        self.course_list.pack(side="left", fill="both", expand=True, padx=(0, 6))

        scrollbar = tk.Scrollbar(list_frame, command=self.course_list.yview)
        scrollbar.pack(side="left", fill="y")
        self.course_list.config(yscrollcommand=scrollbar.set)

        btns = tk.Frame(content, bg=THEME["card_bg"])
        btns.grid(row=4, column=0, sticky="ew", pady=(12, 0))
        tk.Button(
            btns,
            text="Sterge selectia",
            command=self._remove_course,
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
        self.course_list.delete(0, tk.END)
        for course in self.app.courses:
            self.course_list.insert(tk.END, f"{course['course']} - {course['teacher']}")

    def _add_course(self):
        course = self.course_entry.get().strip()
        teacher = self.teacher_entry.get().strip()
        if not course or not teacher:
            messagebox.showwarning("Date incomplete", "Completeaza numele cursului si profesorul.")
            return
        self.app.courses.append({"course": course, "teacher": teacher})
        save_courses(self.app.courses)
        self.course_entry.delete(0, tk.END)
        self.teacher_entry.delete(0, tk.END)
        self._refresh_list()

    def _remove_course(self):
        selection = self.course_list.curselection()
        if not selection:
            messagebox.showinfo("Stergere", "Nu ai selectat nimic.")
            return
        index = selection[0]
        del self.app.courses[index]
        save_courses(self.app.courses)
        self._refresh_list()
