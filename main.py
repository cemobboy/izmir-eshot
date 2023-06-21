import json
import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def get_hatlar():
    selected_hat = hatlar_entry.get()
    if selected_hat:
        for hat in data["Hatlar"]:
            if str(hat["HimHatId"]) == selected_hat:
                hat_detay = f"Hat Adı: {hat['Adi']}\n"
                hat_detay += f"Hat Başlangıç: {hat['HatBaslangic']}\n"
                hat_detay += f"Hat Bitiş: {hat['HatBitis']}\n"
                hat_detay += f"Tarife: {hat['Tarife']}\n"
                hat_detay += f"Çalışma saati başlangıç: {hat['CalismaSaatiGidis']}\n"
                hat_detay += f"Çalışma saati dönüş: {hat['CalismaSaatiDonus']}\n"
                hat_detay += f"Güzergah: {hat['GuzergahAciklama']}\n"
                messagebox.showinfo("Hat Detayları", hat_detay)
                return
        messagebox.showerror("Hata", "Hat bulunamadı.")


url = "https://openapi.izmir.bel.tr/api/eshot/hatlar"
response = requests.get(url, verify=False)
data = json.loads(response.text)


window = tk.Tk()
window.title("İZMİR ESHOT")
window.geometry("500x500")


image_path = "İzmir_icon.png"
image = Image.open(image_path)
image = image.resize((200, 200), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

photo_label = tk.Label(window, image=photo)
photo_label.pack()

hatlar_label = tk.Label(window, text="Eshot No Girin", font=("Arial", 30, "bold"))
hatlar_label.pack()

hatlar_entry = tk.Entry(window)
hatlar_entry.pack()

hatlar_button = tk.Button(window, text="ARA", command=get_hatlar)
hatlar_button.pack()

window.mainloop()
