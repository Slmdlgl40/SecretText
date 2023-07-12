from tkinter import *
from PIL import Image, ImageTk
import base64

def sifrele():
    metin = secret_text.get("1.0",END)
    metin_bytes = metin.encode()
    sifreli_metin = base64.b64encode(metin_bytes)
    return sifreli_metin

def dosya_kaydet(metin,baslik):
    baslik_bytes = baslik.encode()
    with open("secret.txt","ab") as dosya:
        dosya.write(b"\n" + baslik_bytes + b"\n" + metin)

def button_clicked():
    dosya_kaydet(sifrele(),title_entry.get())

window = Tk()
window.minsize(width=400,height=700)
window.title("Secret Notes")

image = Image.open("image.jpg")
photo_width = 100
photo_height = 100
resize = image.resize((photo_width,photo_height))
photo = ImageTk.PhotoImage(resize)

photo_label = Label(image=photo)
photo_label.place(x=150,y=50)

label_1 = Label(text="Enter your title",font=("Arial",15,"bold"))
label_1.place(x=127,y=190)

title_entry = Entry(width=20)
title_entry.place(x=107,y=215)

label_2 = Label(text="Enter your secret",font=("Arial",15,"bold"))
label_2.place(x=117,y=240)

secret_text = Text(width=40,height=15)
secret_text.place(x=37,y=265)

label_3 = Label(text="Enter master key",font=("Arial",15,"bold"))
label_3.place(x=117,y=560)

key_entry = Entry(width=20)
key_entry.place(x=107,y=590)

encrypt_button = Button(text="Save & Encrypt",width=10,command=button_clicked)
encrypt_button.place(x=141,y=620)

decrypt_button = Button(text="Decrypt",width=10)
decrypt_button.place(x=141,y=650)

window.mainloop()

