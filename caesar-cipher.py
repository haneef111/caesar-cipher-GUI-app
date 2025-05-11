import tkinter as tk
from tkinter import messagebox

li = list('abcdefghijklmnopqrstuvwxyz')

def encrypt_message():
    message = entry_message.get().lower()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift number must be an integer.")
        return
    
    result = ''
    for char in message:
        if char in li:
            index = li.index(char)
            new_index = (index + shift) % len(li)
            result += li[new_index]
        else:
            result += char
    output_label.config(text=f" Encrypted: {result}")

def decrypt_message():
    message = entry_message.get().lower()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift number must be an integer.")
        return

    result = ''
    for char in message:
        if char in li:
            index = li.index(char)
            new_index = (index - shift) % len(li)
            result += li[new_index]
        else:
            result += char
    output_label.config(text=f"Decrypted: {result}")

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher App")
root.geometry("450x330")
root.configure(bg="#2c3e50")
root.resizable(False, False)

tk.Label(root, text="Caesar Cipher Tool", font=("Helvetica", 20, "bold"), bg="#2c3e50", fg="white").pack(pady=10)

frame = tk.Frame(root, bg="#2c3e50")
frame.pack(pady=5)

tk.Label(frame, text="Enter your message:", bg="#2c3e50", fg="white").grid(row=0, column=0, sticky="w")
entry_message = tk.Entry(frame, width=40, font=("Arial", 12))
entry_message.grid(row=1, column=0, pady=5)

tk.Label(frame, text="Enter shift number:", bg="#2c3e50", fg="white").grid(row=2, column=0, sticky="w")
entry_shift = tk.Entry(frame, width=10, font=("Arial", 12))
entry_shift.grid(row=3, column=0, pady=5)

btn_frame = tk.Frame(root, bg="#2c3e50")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Encrypt", command=encrypt_message, bg="#27ae60", fg="white", font=("Arial", 12), width=12).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Decrypt", command=decrypt_message, bg="#2980b9", fg="white", font=("Arial", 12), width=12).grid(row=0, column=1, padx=10)

output_label = tk.Label(root, text="", wraplength=380, bg="#2c3e50", fg="#f1c40f", font=("Arial", 13, "bold"))
output_label.pack(pady=20)

tk.Label(root, text="Developed by Shaik Mohammad Haneef  using Tkinter and Python", bg="#2c3e50", fg="#95a5a6", font=("Helvetica", 9)).pack(side="bottom", pady=5)

root.mainloop()
