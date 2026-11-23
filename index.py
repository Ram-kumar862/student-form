import calendar
import re
import tkinter as tk
from datetime import date
from tkinter import OptionMenu, messagebox

PAGE_BG = "#f2f6fc"
CARD_BG = "#ffffff"
TEXT_COLOR = "#172033"
INPUT_BG = "#f8fafc"
BORDER_COLOR = "#cbd5e1"
ACCENT_COLOR = "#87ceeb"
BUTTON_COLOR = "#2563eb"

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("600x700")
root.configure(bg=PAGE_BG)
root.resizable(False, False)

heading = tk.Label(
    root,
    text="Student Registration Form",
    font=("Segoe UI", 21, "bold"),
    fg=ACCENT_COLOR,
    bg=PAGE_BG
)
heading.pack(pady=(26, 18))
form_box = tk.Frame(
    root,
    bg=CARD_BG,
    bd=0,
    relief="flat",
    padx=26,
    pady=22,
    highlightbackground="#e3eaf4",
    highlightthickness=1,
)
form_box.pack(padx=30, fill="x")
form_box.columnconfigure(1, weight=1)
fields = [
    ("Name:", "name"),
    ("Email *:", "email"),
    ("Age:", "age"),
    ("Course:", "course"),
    ("Date of Birth:", "dob"),
    ("Phone *:", "phone"),
    ("Address:", "address"),
]
course_var = tk.StringVar(value="None")
course_options = ("None", "BCA", "BSc Math", "BSc CS", "BSc Biotech")
dob_var = tk.StringVar(value="Select date")
entries = {}
address_text = None
def open_calendar():
    today = date.today()
    popup = tk.Toplevel(root)
    popup.title("Select Date of Birth")
    popup.configure(bg=CARD_BG)
    popup.resizable(False, False)
    popup.transient(root)
    popup.grab_set()
    current_month = [today.year, today.month]
    month_label = tk.Label(
        popup, font=("Segoe UI", 11, "bold"), fg=TEXT_COLOR, bg=CARD_BG
    )
    month_label.grid(row=0, column=1, padx=10, pady=8)
    days_frame = tk.Frame(popup, bg=CARD_BG)
    days_frame.grid(row=1, column=0, columnspan=3, padx=8, pady=(0, 8))
    def draw_month():
        year, month = current_month
        month_label.config(text=f"{calendar.month_name[month]} {year}")
        for child in days_frame.winfo_children():
            child.destroy()
        for column, weekday in enumerate(("Mo", "Tu", "We", "Th", "Fr", "Sa", "Su")):
            tk.Label(
                days_frame,
                text=weekday,
                width=4,
                font=("Segoe UI", 9, "bold"),
                fg=TEXT_COLOR,
                bg=CARD_BG,
            ).grid(row=0, column=column)
        for week_index, week in enumerate(calendar.monthcalendar(year, month), start=1):
            for column, day in enumerate(week):
                if day:
                    selected_date = date(year, month, day)
                    tk.Button(
                        days_frame,
                        text=str(day),
                        width=3,
                        font=("Segoe UI", 9),
                        bg=INPUT_BG,
                        fg=TEXT_COLOR,
                        activebackground=ACCENT_COLOR,
                        relief="flat",
                        state="normal" if selected_date <= today else "disabled",
                        command=lambda selected_day=day: select_date(selected_day),
                    ).grid(row=week_index, column=column, padx=1, pady=1)

    def select_date(day):
        dob_var.set(date(current_month[0], current_month[1], day).strftime("%d-%m-%Y"))
        popup.destroy()
    def change_month(offset):
        year, month = current_month
        month += offset
        if month < 1:
            year -= 1
            month = 12
        elif month > 12:
            year += 1
            month = 1
        current_month[:] = [year, month]
        draw_month()
    tk.Button(
        popup,
        text="<",
        width=3,
        bg=INPUT_BG,
        fg=TEXT_COLOR,
        relief="flat",
        command=lambda: change_month(-1),
    ).grid(row=0, column=0, padx=8, pady=8)
    tk.Button(
        popup,
        text=">",
        width=3,
        bg=INPUT_BG,
        fg=TEXT_COLOR,
        relief="flat",
        command=lambda: change_month(1),
    ).grid(row=0, column=2, padx=8, pady=8)
    draw_month()
for row, (label, field) in enumerate(fields):
    tk.Label(
        form_box,
        text=label,
        font=("Segoe UI", 10, "bold"),
        fg=TEXT_COLOR,
        bg=CARD_BG,
        anchor="w",
    ).grid(row=row, column=0, sticky="nw", padx=(0, 18), pady=6)
    if field == "course":
        course_menu = OptionMenu(
            form_box,
            course_var,
            *course_options,
        )
        course_menu.config(
            width=27,
            anchor="w",
            font=("Segoe UI", 10),
            background=INPUT_BG,
            foreground=TEXT_COLOR,
            activebackground=ACCENT_COLOR,
            relief="flat",
            highlightthickness=1,
            highlightbackground=BORDER_COLOR,
        )
        course_menu["menu"].config(
            font=("Segoe UI", 10), background=CARD_BG, foreground=TEXT_COLOR
        )
        course_menu.grid(row=row, column=1, sticky="ew", pady=6)
    elif field == "dob":
        dob_frame = tk.Frame(form_box, bg="white")
        dob_frame.grid(row=row, column=1, sticky="ew", pady=6)
        tk.Entry(
            dob_frame,
            textvariable=dob_var,
            state="readonly",
            font=("Segoe UI", 10),
            readonlybackground=INPUT_BG,
            relief="flat",
            highlightthickness=1,
            highlightbackground=BORDER_COLOR,
        ).pack(side="left", fill="x", expand=True)
        tk.Button(
            dob_frame,
            text="Choose date",
            command=open_calendar,
            font=("Segoe UI", 9, "bold"),
            bg=BUTTON_COLOR,
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            relief="flat",
            padx=10,
            pady=6,
        ).pack(side="left", padx=(8, 0))
    elif field == "phone":
        phone_frame = tk.Frame(form_box, bg="white")
        phone_frame.grid(row=row, column=1, sticky="ew", pady=6)
        tk.Label(
            phone_frame,
            text="+91",
            bg=INPUT_BG,
            fg=TEXT_COLOR,
            font=("Segoe UI", 10, "bold"),
            padx=10,
            pady=8,
        ).pack(
            side="left", padx=(0, 8)
        )
        entries[field] = tk.Entry(
            phone_frame,
            width=25,
            font=("Segoe UI", 10),
            bg=INPUT_BG,
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            relief="flat",
            highlightthickness=1,
            highlightbackground=BORDER_COLOR,
            highlightcolor=BUTTON_COLOR,
        )
        entries[field].pack(side="left", fill="x", expand=True)
    elif field == "address":
        address_text = tk.Text(
            form_box,
            width=30,
            height=3,
            font=("Segoe UI", 10),
            bg=INPUT_BG,
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            relief="flat",
            highlightthickness=1,
            highlightbackground=BORDER_COLOR,
            highlightcolor=BUTTON_COLOR,
            padx=10,
            pady=8,
        )
        address_text.grid(row=row, column=1, sticky="ew", pady=6)
    else:
        entries[field] = tk.Entry(
            form_box,
            width=30,
            font=("Segoe UI", 10),
            bg=INPUT_BG,
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            relief="flat",
            highlightthickness=1,
            highlightbackground=BORDER_COLOR,
            highlightcolor=BUTTON_COLOR,
        )
        entries[field].grid(row=row, column=1, sticky="ew", pady=6)
def register():
    name = entries["name"].get().strip()
    email = entries["email"].get().strip()
    age = entries["age"].get().strip()
    course = course_var.get()
    dob = dob_var.get()
    phone = entries["phone"].get().strip()
    address = address_text.get("1.0", tk.END).strip()
    if not email:
        messagebox.showerror("Required Field", "Email is required.")
        return
    if not re.fullmatch(r"[A-Za-z0-9._%+-]+@gmail\.com", email, re.IGNORECASE):
        messagebox.showerror("Invalid Email", "Enter a valid Gmail address ending in @gmail.com.")
        return
    if not phone:
        messagebox.showerror("Required Field", "Phone number is required.")
        return
    if not re.fullmatch(r"[6-9]\d{9}", phone):
        messagebox.showerror("Invalid Phone", "Enter a valid 10-digit Indian phone number.")
        return
    if (
        not name
        or not age.isdigit()
        or int(age) <= 0
        or course == "None"
        or dob == "Select date"
        or not address
    ):
        messagebox.showerror(
            "Error",
            "Please complete all other fields correctly.",
        )
        return
    messagebox.showinfo(
        "Success",
        "Registration successful!\n\n"
        + f"Name: {name}\n"
        + f"Email: {email}\n"
        + f"Age: {age}\n"
        + f"Course: {course}\n"
        + f"Date of Birth: {dob}\n"
        + f"Phone: +91 {phone}\n"
        + f"Address: {address}",
    )
    for entry in entries.values():
        entry.delete(0, tk.END)
    course_var.set("None")
    dob_var.set("Select date")
    address_text.delete("1.0", tk.END)
register_btn = tk.Button(
    root,
    text="REGISTER",
    command=register,
    bg=BUTTON_COLOR,
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    font=("Segoe UI", 11, "bold"),
    relief="flat",
    padx=20,
    pady=9,
)
register_btn.pack(pady=(18, 8))
exit_btn = tk.Button(
    root,
    text="EXIT",
    command=root.destroy,
    bg=CARD_BG,
    fg=TEXT_COLOR,
    activebackground=INPUT_BG,
    font=("Segoe UI", 10),
    relief="flat",
    padx=20,
    pady=7,
)
exit_btn.pack()
root.mainloop()