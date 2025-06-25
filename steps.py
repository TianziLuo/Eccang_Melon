from tkinter import messagebox
from purchase.func import (
    clean_folder,
    copy_purchase,
    open_excel,
    save_cvs,
    copy_cvs,
)
from unzip import unzip
from xls2csv import xls2csv
from rename import rename
from copy_download import copy_download

def run_clean_folder():
    print("🍉 Running: Clean folder")
    try:
        clean_folder()
        messagebox.showinfo("Done", "Folder cleaned ✅")
    except Exception as e:
        messagebox.showerror("Error", f"Clean folder failed:\n{e}")

def run_copy_purchase():
    print("🍉 Running: Copy purchase files")
    try:
        copy_purchase()
        messagebox.showinfo("Done", "Purchase files copied ✅")
    except Exception as e:
        messagebox.showerror("Error", f"Copy purchase failed:\n{e}")

def run_open_excel():
    print("🍉 Running: Open Excel template")
    try:
        open_excel()
        messagebox.showinfo("Done", "Excel template opened ✅")
    except Exception as e:
        messagebox.showerror("Error", f"Open Excel failed:\n{e}")

def run_save_cvs():
    print("🍉 Running: Save CSV")
    try:
        save_cvs()
        messagebox.showinfo("Done", "CSV saved ✅")
    except Exception as e:
        messagebox.showerror("Error", f"Save CSV failed:\n{e}")

def run_copy_cvs():
    print("🍉 Running: Copy CSV files")
    try:
        copy_cvs()
        messagebox.showinfo("Done", "CSV files copied ✅")
    except Exception as e:
        messagebox.showerror("Error", f"Copy CSV failed:\n{e}")

def step2_unzip():
    print("🍉 Running: Unzip files")
    try:
        unzip()
        messagebox.showinfo("Done", "Step 2 (Unzip) completed ✅")
    except Exception as e:
        messagebox.showerror("Error", f"Step 2 error:\n{e}")

def step3_convert():
    print("🍉 Running: Convert XLS to CSV")
    try:
        xls2csv()
        messagebox.showinfo("Done", "Step 3 (Convert CSV) completed ✅")
    except Exception as e:
        messagebox.showerror("Error", f"Step 3 error:\n{e}")

def step4_rename():
    print("🍉 Running: Rename files")
    try:
        rename()
        messagebox.showinfo("Done", "Step 4 (Rename) completed ✅")
    except Exception as e:
        messagebox.showerror("Error", f"Step 4 error:\n{e}")

def step5_copy():
    print("🍉 Running: Copy downloaded files")
    try:
        copy_download()
        messagebox.showinfo("Done", "Step 5 (Copy downloaded files) completed ✅")
    except Exception as e:
        messagebox.showerror("Error", f"Step 5 error:\n{e}")
