from tkinter import *

def size(x):
    x.update()
    print(x.winfo_height())
    print(x.winfo_width())

window = Tk()
window.minsize(width=400,height=600)
window.title("Secret Notes")

label_1 = Label(text="Enter your title",font=("Arial",15,"bold"))
label_1.place(x=127,y=90)

title_entry = Entry(width=20)
title_entry.place(x=107,y=115)

label_2 = Label(text="Enter your secret",font=("Arial",15,"bold"))
label_2.place(x=117,y=140)

secret_text = Text(width=40,height=15)
secret_text.place(x=37,y=165)

label_3 = Label(text="Enter master key",font=("Arial",15,"bold"))
label_3.place(x=117,y=460)

key_entry = Entry(width=20)
key_entry.place(x=107,y=490)

encrypt_button = Button(text="Save & Encrypt",width=10)
encrypt_button.place(x=141,y=520)

decrypt_button = Button(text="Decrypt",width=10)
decrypt_button.place(x=141,y=550)

window.mainloop()

