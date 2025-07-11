import tkinter as tk
from steps import (
    run_purchase_files,
    run_save_copy_cvs,
    step2_to_4_all,
    step5_copy,
)
from styles import btn_params, header_font, title_font

def make_step_frame(parent, text):
    frame = tk.Frame(
        parent,
        bg="#fadee3",
        bd=2,
        relief="ridge",
        padx=2,
        pady=3
    )
    label = tk.Label(
        frame,
        text=text + " 🍉",
        font=header_font,
        fg="#143b3b",
        bg="#fadee3"
    )
    label.pack(anchor="w", pady=(0, 1))
    return frame

def create_main_window():
    window = tk.Tk()
    window.title("🍉 Subarashii Melon 🍉")
    window.geometry("400x400")
    window.configure(bg="#EDFCA6")

    tk.Label(
        window,
        text="🍉 Eecamg Watermelon",
        font=title_font,
        fg="#072020",
        bg="#EDFCA6"
    ).pack(pady=6)

    # Step 1
    frame1 = make_step_frame(window, "Step 1: Purchase Process")
    frame1.pack(padx=25, pady=10, fill="x")
    tk.Button(frame1, text="Update Purchase Folder", command=run_purchase_files, **btn_params).pack(padx=4, pady=2)
    tk.Button(frame1, text="Save & Copy CSV", command=run_save_copy_cvs, **btn_params).pack(padx=4, pady=2)
    
    # Step 2
    frame2 = make_step_frame(window, "Step 2 - 4: Unzip ➜ Convert ➜ Rename")
    frame2.pack(padx=25, pady=10, fill="x")
    tk.Button(
    frame2,
    text= "Unzip, Convert, Rename",
    command=step2_to_4_all,
    **btn_params
).pack(padx=4, pady=2)

    # Step 3
    frame3 = make_step_frame(window, "Step 5: Copy Downloads Files")
    frame3.pack(padx=25, pady=10, fill="x")
    tk.Button(frame3, text="Copy Downloaded Files", command=step5_copy, **btn_params).pack(padx=4, pady=2)

    return window
