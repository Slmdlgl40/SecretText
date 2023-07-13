from tkinter import *
from PIL import Image, ImageTk
import base64
def encrypt():
    metin = secret_text.get("1.0",END)
    sifre = key_entry.get()
    metin_bytes = metin.encode()
    sifre_bytes = sifre.encode()
    encrypted_text_bytes = []

    for i in range(len(metin_bytes)):
        encrypted_byte = metin_bytes[i] ^ sifre_bytes[i % len(sifre_bytes)]
        encrypted_text_bytes.append(encrypted_byte)

    encrypted_text = base64.b64encode(bytes(encrypted_text_bytes))
    return encrypted_text

def decrypt():
    sifre = key_entry.get()
    sifre_bytes = sifre.encode()
    encrypted_text = secret_text.get("1.0",END)
    encrypted_text_bytes = base64.b64decode(encrypted_text)
    decrypted_text_bytes = []

    for i in range(len(encrypted_text_bytes)):
        decrypted_byte = encrypted_text_bytes[i] ^ sifre_bytes[i % len(sifre_bytes)]
        decrypted_text_bytes.append(decrypted_byte)

    decrypted_text = bytes(decrypted_text_bytes).decode()
    return decrypted_text

def dosya_kaydet():
    baslik = title_entry.get()
    baslik_bytes = baslik.encode()
    sifreli_metin = encrypt()
    with open("secret.txt","ab") as dosya:
        dosya.write(b"\n" + baslik_bytes + b"\n" + sifreli_metin)

def encrypt_button_clicked():
    dosya_kaydet()

def decrypt_button_clicked():
    decrypted_text = decrypt()
    secret_text.delete("1.0",END)
    secret_text.insert("1.0",decrypted_text)

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

encrypt_button = Button(text="Save & Encrypt",width=10,command=encrypt_button_clicked)
encrypt_button.place(x=141,y=620)

decrypt_button = Button(text="Decrypt",width=10,command=decrypt_button_clicked)
decrypt_button.place(x=141,y=650)

window.mainloop()