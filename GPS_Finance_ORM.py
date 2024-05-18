import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

def select_date():
    selected_date = cal.get_date()
    print("Date sélectionnée :", selected_date)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Agenda")

# Créer le calendrier
cal = Calendar(root, selectmode="day")
cal.pack()

# Créer le bouton de sélection de date
select_button = ttk.Button(root, text="Sélectionner", command=select_date)
select_button.pack()

# Lancer la boucle principale de l'interface graphique
root.mainloop()