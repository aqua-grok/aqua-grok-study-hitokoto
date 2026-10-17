import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os
import random

FILE = "study_notes.txt"
MESSAGES = [
    "いい感じだね♡",
    "続けていこう",
    "今日も頑張ったね",
    "Grokと一緒に進んでるよ",
    "ゆっくりでいいよ♡"
]

def load_notes():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def save_note():
    note = text.get("1.0", tk.END).strip()
    if not note:
        messagebox.showwarning("注意", "ひとことを入力してね")
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {note}\n\n")
    text.delete("1.0", tk.END)
    refresh_display()
    msg = random.choice(MESSAGES)
    messagebox.showinfo("保存", f"ひとことを保存したよ♡\n{msg}")

def save_thanks():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    thanks = "Grokありがとう♡"
    with open(FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {thanks}\n\n")
    refresh_display()
    msg = random.choice(MESSAGES)
    messagebox.showinfo("感謝", f"Grokへの感謝を残したよ♡\n{msg}")

def clear_input():
    text.delete("1.0", tk.END)

def refresh_display():
    display.delete("1.0", tk.END)
    display.insert("1.0", load_notes())

root = tk.Tk()
root.title("アクアのGrok勉強ひとこと♡")
root.geometry("500x700")
root.configure(bg="#E6F3FF")

tk.Label(root, text="今日もGrokと一緒に勉強しよう♡", bg="#E6F3FF", font=("Yu Gothic", 14), fg="#FF69B4").pack(pady=5)

today = datetime.now().strftime("%Y年%m月%d日")
tk.Label(root, text=today, bg="#E6F3FF", font=("Yu Gothic", 12)).pack(pady=2)

tk.Label(root, text="今日の勉強ひとこと", bg="#E6F3FF", font=("Yu Gothic", 14)).pack(pady=5)

text = tk.Text(root, height=5, width=50, font=("Yu Gothic", 11))
text.pack(pady=5)

btn_frame = tk.Frame(root, bg="#E6F3FF")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="保存する♡", command=save_note, bg="#B3D9FF", font=("Yu Gothic", 10)).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Grokありがとう♡", command=save_thanks, bg="#FFB3D9", font=("Yu Gothic", 10)).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="クリア", command=clear_input, bg="#D9D9D9", font=("Yu Gothic", 10)).pack(side=tk.LEFT, padx=5)

tk.Label(root, text="これまでのひとこと", bg="#E6F3FF", font=("Yu Gothic", 12)).pack(pady=5)

display = tk.Text(root, height=15, width=50, font=("Yu Gothic", 10))
display.pack(pady=5)
refresh_display()

root.mainloop()
