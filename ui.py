import tkinter as tk
from steps import (
    run_clean_folder,
    run_copy_purchase,
    run_open_excel,
    run_save_cvs,
    run_copy_cvs,
    step2_unzip,
    step3_convert,
    step4_rename,
    step5_copy,
)
from styles import btn_params, default_font, header_font, title_font

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
        fg="#1b4f4f",
        bg="#fadee3"
    )
    label.pack(anchor="w", pady=(0, 1))
    return frame

def create_main_window():
    window = tk.Tk()
    window.title("🍉 Subarashii Melon 🍉")
    window.geometry("440x710")
    window.configure(bg="#d5ffbf")

    tk.Label(
        window,
        text="🍉 Eecamg Watermelon",
        font=title_font,
        fg="#072020",
        bg="#d5ffbf"
    ).pack(pady=6)

    # Step 1
    frame1 = make_step_frame(window, "Step 1: Purchase Process")
    frame1.pack(padx=35, pady=10, fill="x")
    tk.Button(frame1, text="1.Clean Folder", command=run_clean_folder, **btn_params).pack(padx=4, pady=2)
    tk.Button(frame1, text="2.Copy Purchase Files", command=run_copy_purchase, **btn_params).pack(padx=4, pady=2)
    tk.Button(frame1, text="3.Open Excel", command=run_open_excel, **btn_params).pack(padx=4, pady=2)
    tk.Button(frame1, text="4.Save As CSV", command=run_save_cvs, **btn_params).pack(padx=4, pady=2)
    tk.Button(frame1, text="5.Copy CSV Files", command=run_copy_cvs, **btn_params).pack(padx=4, pady=2)

    # Step 2
    frame2 = make_step_frame(window, "Step 2: Unzip ZIP")
    frame2.pack(padx=35, pady=10, fill="x")
    tk.Button(frame2, text="Unzip all ZIP", command=step2_unzip, **btn_params).pack(padx=4, pady=2)

    # Step 3
    frame3 = make_step_frame(window, "Step 3: Convert XLS ➜ CSV")
    frame3.pack(padx=35, pady=10, fill="x")
    tk.Button(frame3, text="Convert XLS to CSV", command=step3_convert, **btn_params).pack(padx=4, pady=2)

    # Step 4
    frame4 = make_step_frame(window, "Step 4: Rename Files")
    frame4.pack(padx=35, pady=10, fill="x")
    tk.Button(frame4, text="Rename Files", command=step4_rename, **btn_params).pack(padx=4, pady=2)

    # Step 5
    frame5 = make_step_frame(window, "Step 5: Copy Downloaded Files")
    frame5.pack(padx=35, pady=10, fill="x")
    tk.Button(frame5, text="Copy Downloaded Files", command=step5_copy, **btn_params).pack(padx=4, pady=2)

    return window
