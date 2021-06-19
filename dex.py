import pypokedex
import urllib3
from io import BytesIO
import tkinter as tk
import PIL.Image
import PIL.ImageTk

# set the window and title
window = tk.Tk()
window.geometry("600x500")
window.title("bugomaster pokedex")
window.config(padx=10, pady=10)


title = tk.Label(window, text="pokedex")
title.config(font=("Arial", 32))
title.pack(padx=10, pady=10)

# create an empty label that after the load pokemon method will be the image
pokemon_img = tk.Label(window)
pokemon_img.pack(padx=10, pady=10)


pokemon_inf = tk.Label(window)
pokemon_inf.config(font=("Arial", 20))
pokemon_inf.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 20))
pokemon_types.pack(padx=10, pady=10)


def load_pokemon():
    pokemon = pypokedex.get(name=id_name_txt.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_img.config(image=img)
    pokemon_img.image = img

    pokemon_inf.config(text=f"{pokemon.dex} - {pokemon.name}")
    pokemon_types.config(text=" - ".join([t for t in pokemon.types]))


id_name = tk.Label(window, text="ID or Name")
id_name.config(font=("Arial", 20))
id_name.pack(padx=10, pady=10)

id_name_txt = tk.Text(window, height=1)
id_name_txt.config(font=("Arial", 20))
id_name_txt.pack(padx=10, pady=10)

btn = tk.Button(window, text="load pokemon", command=load_pokemon)
btn.config(font=("Arial", 20))
btn.pack(padx=10, pady=10)


window.mainloop()
