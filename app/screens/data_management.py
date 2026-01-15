"""Ecran de gestionare a datelor (cursuri)."""
from tkinter import messagebox, ttk
import tkinter as tk

from app.constants import FONTS, THEME
from app.data import save_courses
from app.screens.base import BaseScreen


class DataManagementScreen(BaseScreen):
    """Ecran de gestionare a datelor (cursuri)."""

    def __init__(self, master, app):
        super().__init__(master, app, bg=THEME["data_bg"])
        self._build_ui()

    def _build_ui(self):
        header = tk.Frame(self, bg=THEME["data_bg"], padx=20, pady=15)
        header.pack(fill="x")
        tk.Label(header, text="Gestionare Cursuri", font=FONTS["title"], bg=THEME["data_bg"]).pack(anchor="w")
        tk.Label(
            header,
            text="Adauga cursuri noi si actualizeaza lista curenta.",
            font=FONTS["small"],
            bg=THEME["data_bg"],
            fg=THEME["text_muted"],
        ).pack(anchor="w", pady=(4, 0))

        form = tk.Frame(self, bg=THEME["panel_bg"], padx=15, pady=12, highlightbackground=THEME["outline"])
        form.pack(padx=25, pady=10, fill="x")
        form.configure(highlightthickness=1)

        tk.Label(form, text="Nume curs", bg=THEME["panel_bg"], font=FONTS["body"]).grid(
            row=0, column=0, sticky="w", pady=5
        )
        tk.Label(form, text="Profesor", bg=THEME["panel_bg"], font=FONTS["body"]).grid(
            row=0, column=1, sticky="w", pady=5
        )

        self.course_entry = tk.Entry(form, width=22)
        self.teacher_entry = tk.Entry(form, width=22)
        self.course_entry.grid(row=1, column=0, padx=(0, 10), pady=5, sticky="ew")
        self.teacher_entry.grid(row=1, column=1, padx=(0, 10), pady=5, sticky="ew")

        add_btn = tk.Button(form, text="Adauga curs", command=self._add_course, bg=THEME["accent"], fg="white")
        add_btn.grid(row=1, column=2, padx=5)
        form.columnconfigure(0, weight=1)
        form.columnconfigure(1, weight=1)

        list_frame = tk.Frame(self, bg=THEME["panel_bg"], padx=10, pady=10, highlightbackground=THEME["outline"])
        list_frame.pack(padx=25, pady=10, fill="both", expand=True)
        list_frame.configure(highlightthickness=1)

        self.course_list = ttk.Treeview(list_frame, columns=("course", "teacher"), show="headings", height=7)
        self.course_list.heading("course", text="Curs")
        self.course_list.heading("teacher", text="Profesor")
        self.course_list.column("course", width=200)
        self.course_list.column("teacher", width=170)
        self.course_list.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame, command=self.course_list.yview)
        scrollbar.pack(side="right", fill="y")
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
        for item in self.course_list.get_children():
            self.course_list.delete(item)
        for course in self.app.courses:
            self.course_list.insert("", tk.END, values=(course["course"], course["teacher"]))

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
        selection = self.course_list.selection()
        if not selection:
            messagebox.showinfo("Stergere", "Nu ai selectat nimic.")
            return
        index = self.course_list.index(selection[0])
        del self.app.courses[index]
        save_courses(self.app.courses)
        self._refresh_list()
