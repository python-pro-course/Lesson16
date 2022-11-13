from tkinter import *
import os
from PIL import Image, ImageTk


# ФУНКЦИИ
def sign_up():
    sign_up_window = Toplevel(main)
    sign_up_window.title('Регистрация')
    sign_up_window.geometry('400x500')

    # Labels
    Label(sign_up_window, text='Введите логин и пароль', font=('Calibri', 25)).grid(row=0, sticky=N, pady=10)
    Label(sign_up_window, text='Логин: ', font=('Calibri', 15)).grid(row=1, sticky=W, pady=10)
    Label(sign_up_window, text='Пароль: ', font=('Calibri', 15)).grid(row=2, sticky=W, pady=10)

    # Button


def login():
    sign_up_window = Toplevel(main)
    sign_up_window.title('Вход')
    sign_up_window.geometry('400x500')


# main
main = Tk()
main.title('Банк')
main.geometry('400x500')

# image
img = Image.open('image/img1.png')
img = img.resize((200, 200))
img = ImageTk.PhotoImage(img)

# Labels
Label(main, text='Самый простой банк', font=('Calibri', 25)).pack(side=TOP)
Label(main, image=img).pack(side=TOP)

# Button
Button(main, text='Регистрация', font=('Calibri', 12), width=15, command=sign_up).pack(side=TOP, pady=10)
Button(main, text='Вход', font=('Calibri', 12), width=15, command=login).pack(side=TOP, pady=10)

main.mainloop()



