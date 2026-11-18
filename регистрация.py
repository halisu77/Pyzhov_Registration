from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Авторизация")
root.geometry("300x200")

label = ttk.Label(
    text="Вход в систему",
    font=("Arial", 14))
label.pack(anchor=NW, padx=10, pady=6)

label_login = ttk.Label(text="Логин:")
label_login.pack(anchor=NW, padx=10)
entry_login = Entry()
entry_login.pack(anchor=NW, padx=10, pady=4)

label_pass = ttk.Label(text="Пароль:")
label_pass.pack(anchor=NW, padx=10)
entry_pass = Entry(show="*")
entry_pass.pack(anchor=NW, padx=10, pady=4)

def click():
    login = entry_login.get()
    label_result["text"] = f"Привет, {login}!"

btn = ttk.Button(text="Войти", command=click)
btn.pack(anchor=NW, padx=10, pady=8)
label_result = ttk.Label(text="")
label_result.pack(anchor=NW, padx=10, pady=4)
root.mainloop()
