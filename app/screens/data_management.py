"""Ecran de gestionare a datelor (cursuri)."""
from tkinter import messagebox
import tkinter as tk

from app.constants import THEME
from app.screens.base import BaseScreen


class DataManagementScreen(BaseScreen):
    """Ecran de gestionare a datelor (cursuri)."""

    def __init__(self, master, app):
        super().__init__(master, app, bg=THEME["data_bg"])
        self._build_ui()

    def _build_ui(self):
        title = tk.Label(self, text="Gestionare Cursuri", font=("Helvetica", 18, "bold"), bg=THEME["data_bg"])
        title.pack(pady=15)

        form = tk.Frame(self, bg=THEME["data_bg"])
        form.pack(pady=5)

        tk.Label(form, text="Nume curs:", bg=THEME["data_bg"]).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        tk.Label(form, text="Profesor:", bg=THEME["data_bg"]).grid(row=1, column=0, sticky="e", padx=5, pady=5)

        self.course_entry = tk.Entry(form)
        self.teacher_entry = tk.Entry(form)
        self.course_entry.grid(row=0, column=1, padx=5, pady=5)
        self.teacher_entry.grid(row=1, column=1, padx=5, pady=5)

        add_btn = tk.Button(form, text="Adauga", command=self._add_course, bg="#ff9800", fg="white")
        add_btn.grid(row=0, column=2, rowspan=2, padx=10)

        list_frame = tk.Frame(self, bg=THEME["data_bg"])
        list_frame.pack(pady=10)

        self.course_list = tk.Listbox(list_frame, width=42, height=7)
        self.course_list.pack(side="left", padx=(0, 5))

        scrollbar = tk.Scrollbar(list_frame, command=self.course_list.yview)
        scrollbar.pack(side="left", fill="y")
        self.course_list.config(yscrollcommand=scrollbar.set)

        btns = tk.Frame(self, bg=THEME["data_bg"])
        btns.pack(pady=5)
        tk.Button(btns, text="Sterge selectia", command=self._remove_course).pack(side="left", padx=5)
        tk.Button(btns, text="Inapoi la meniu", command=lambda: self.app.show_screen("main_menu")).pack(
            side="left", padx=5
        )

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
        self._refresh_list()
