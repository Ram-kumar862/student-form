import calendar
import re
import tkinter as tk
from datetime import date
from tkinter import messagebox
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("560x650")
root.configure(bg="lightblue")
root.resizable(False, False)
heading = tk.Label(
    root,
    text="Student Registration Form",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
heading.pack(pady=(20, 14))
form_box = tk.Frame(root, bg="white", bd=2, relief="groove", padx=20, pady=14)
form_box.pack(padx=30, fill="x")
form_box.columnconfigure(1, weight=1)
fields = [
    ("Name:", "name"),
    ("Email:", "email"),
    ("Age:", "age"),
    ("Course:", "course"),
    ("Date of Birth:", "dob"),
    ("Phone:", "phone"),
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
    popup.resizable(False, False)
    popup.transient(root)
    popup.grab_set()
    current_month = [today.year, today.month]
    month_label = tk.Label(popup, font=("Arial", 11, "bold"))
    month_label.grid(row=0, column=1, padx=10, pady=8)
    days_frame = tk.Frame(popup)
    days_frame.grid(row=1, column=0, columnspan=3, padx=8, pady=(0, 8))
    def draw_month():
        year, month = current_month
        month_label.config(text=f"{calendar.month_name[month]} {year}")
        for child in days_frame.winfo_children():
            child.destroy()
        for column, weekday in enumerate(("Mo", "Tu", "We", "Th", "Fr", "Sa", "Su")):
            tk.Label(days_frame, text=weekday, width=4).grid(row=0, column=column)
        for week_index, week in enumerate(calendar.monthcalendar(year, month), start=1):
            for column, day in enumerate(week):
                if day:
                    selected_date = date(year, month, day)
                    tk.Button(
                        days_frame,
                        text=str(day),
                        width=3,
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
    tk.Button(popup, text="<", width=3, command=lambda: change_month(-1)).grid(
        row=0, column=0, padx=8, pady=8
    )
    tk.Button(popup, text=">", width=3, command=lambda: change_month(1)).grid(
        row=0, column=2, padx=8, pady=8
    )
    draw_month()
for row, (label, field) in enumerate(fields):
    tk.Label(
        form_box,
        text=label,
        font=("Arial", 11),
        bg="white",
        anchor="w",
    ).grid(row=row, column=0, sticky="nw", padx=(0, 18), pady=6)
    if field == "course":
        course_menu = tk.OptionMenu(form_box, course_var, *course_options)
        course_menu.config(width=27, anchor="w")
        course_menu.grid(row=row, column=1, sticky="ew", pady=6)
    elif field == "dob":
        dob_frame = tk.Frame(form_box, bg="white")
        dob_frame.grid(row=row, column=1, sticky="ew", pady=6)
        tk.Entry(dob_frame, textvariable=dob_var, state="readonly").pack(
            side="left", fill="x", expand=True
        )
        tk.Button(dob_frame, text="Choose date", command=open_calendar).pack(
            side="left", padx=(8, 0)
        )
    elif field == "phone":
        phone_frame = tk.Frame(form_box, bg="white")
        phone_frame.grid(row=row, column=1, sticky="ew", pady=6)
        tk.Label(phone_frame, text="+91", bg="white", font=("Arial", 11)).pack(
            side="left", padx=(0, 8)
        )
        entries[field] = tk.Entry(phone_frame, width=25, font=("Arial", 11))
        entries[field].pack(side="left", fill="x", expand=True)
    elif field == "address":
        address_text = tk.Text(form_box, width=30, height=3, font=("Arial", 11))
        address_text.grid(row=row, column=1, sticky="ew", pady=6)
    else:
        entries[field] = tk.Entry(form_box, width=30, font=("Arial", 11))
        entries[field].grid(row=row, column=1, sticky="ew", pady=6)
def register():
    name = entries["name"].get().strip()
    email = entries["email"].get().strip()
    age = entries["age"].get().strip()
    course = course_var.get()
    dob = dob_var.get()
    phone = entries["phone"].get().strip()
    address = address_text.get("1.0", tk.END).strip()
    if (
        not name
        or not re.fullmatch(r"[A-Za-z0-9._%+-]+@gmail\.com", email, re.IGNORECASE)
        or not age.isdigit()
        or int(age) <= 0
        or course == "None"
        or dob == "Select date"
        or not re.fullmatch(r"[6-9]\d{9}", phone)
        or not address
    ):
        messagebox.showerror(
            "Error",
            "Enter all details correctly. Use a Gmail address and a valid 10-digit Indian phone number.",
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
    bg="green",
    fg="white",
    font=("Arial", 12, "bold")
)
register_btn.pack(pady=(14, 8))
exit_btn = tk.Button(
    root,
    text="EXIT",
    command=root.destroy,
    bg="red",
    fg="white"
)
exit_btn.pack()
root.mainloop()