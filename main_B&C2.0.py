import random 

from time import time
from tkinter import *
from pravidla import open_rules

# Proměné Barvy
main_color = "#A66B37"
dark_brown = "#401201"
light_color = "#F2C3A7"
light_color2 = "#F2B47E"
brown = "#59380E"

# Okno 
window = Tk()
window.minsize(550, 600)
window.resizable(False, False)
window.title("Bulls & Cows")
window.iconbitmap("bull.ico")
window.config(bg=main_color)

# Framy
title_frame = Frame(window, bg= main_color)
title_frame.pack()
info_frame = Frame(window, bg= main_color)
info_frame.pack()
input_frame = Frame(window, bg= main_color)
input_frame.pack()
text_frame = Frame(window, bg= main_color)
text_frame.pack()

# Hlavní nadpis - Label
title = Label(title_frame, text="Vítejte ve hře", bg= main_color, fg= dark_brown, font= ("Arial", 10, "bold"))
title.pack(pady= 5)
title1 = Label(title_frame, text="Bulls & Cows", bg= main_color, fg= dark_brown, font= ("Arial", 30, "bold"))
title1.pack(pady= 10)

# Zapis pravidel hry do Labelu s popiskem jak hrát 
code = """
Bull/s  = počet uhádnutých čísel, uhádnutých pozic
Cow/s   = počet uhádnutých čísel, špatných pozic
"""
info = """
Zadej čtyřcifené číslo
Číslice nesmí začínat 0
Číslice se za sebou nesmí opakovat(4444)"""

# popis - label
descri = Label(info_frame, text= code, bg= main_color, fg=dark_brown, font= ("Arial", 8, "italic"))
descri.grid(row= 0, column= 0)

description = Label(info_frame, text= info, bg= main_color, fg=dark_brown, font= ("Arial", 8, "italic"))
description.grid(row= 1, column= 0)

#Scroll bar
scroll_bar = Scrollbar(text_frame, bg= light_color)
scroll_bar.grid(row= 0, column= 1, sticky="NS")

# seznam neuhádnutých čísel a u nich Bull and Cow - textové okno se scrolbarem
list_box = Listbox(text_frame, width= 40, height= 15, bg= light_color, fg= dark_brown, font= ("Arial", 8,), yscrollcommand=scroll_bar.set)
list_box.grid(row= 0 ,column= 0)

# Nastavení scroll baru
scroll_bar.config(command=list_box.yview)

# Start nove hry 
def new_game():
    """Funkce spustí novou hru
    Vybere čtyřciferné číslo, které nezačíná nulou, kde se neopakuji čislice"""
    
    list_generated = []
    numbers = list(range(0,10))
    for num in range(0,4): # vygeneruje číso      
        num = random.choice(numbers)
        list_generated.append(num)
        numbers.remove(num)

    while list_generated[0] == 0: # pokud je první číslo nula tak jej změní na jiné.
        list_generated[0] = random.choice(numbers)
    list_box.delete(0, END)
    # print(list_generated) # --->> pro případné ověřování je potřeba odkomentovat tento print
    return list_generated
new_game_value = new_game()

# New game - button, Exit - button
new_g = Button(info_frame, text="Nová hra", width=20, bg= dark_brown, fg= light_color2, font= ("Arial", 10, "bold"), command= new_game)
new_g.grid(row=1, column=1, padx= 5, pady=10)

# tlačítko na pravidla hry 
rules = Button(info_frame, width= 20, text= "Pravidla hry", bg= dark_brown, fg= light_color2, font= ("Arial", 10, "bold"), command= open_rules)
rules.grid(row= 0, column= 1, padx=10, pady= 20)

# Hádané číslo (input)  # místo pro zapsání že číslo je dlouhé, krátké, začíná nulou .... a Bull and Cows
user_input = Entry(input_frame, text= "0000", width= 8, bg=light_color, fg=dark_brown)
user_input.grid(row= 0, column= 0, padx= 15)

# aktuální Bull and Cow případně chyba zadání
output = Label(input_frame, bg= main_color, fg=brown, font= ("Arial", 12, "bold"))
output.grid(row= 0, column=2, padx=5)

#Varování při chybě
output1 = Label(input_frame, bg= main_color, fg=dark_brown, font= ("Arial", 12, "bold"))
output1.grid(row= 1, column=2, padx=10, pady=10)

number = user_input.get()

# Funkce pro správný zápis Bull/s Cow/s
def bull_cow(bull, cow):
    user_number = user_input.get()
    if bull == 4:
        stop_time = time()
        note = f"{user_number} = 4 Bulls, 0 Cow"
        end_label.config(text= f"Uhádl jsi všechny čísla!\n {user_number}\n Stiskni 'Nová hra' \na dej si to ještě jednou!")
    elif bull > 1 and cow <= 1:
        note = f"{user_number} = {bull} Bulls, {cow} Cow."
        output.config(text= note)
        list_box.insert(0, note)
    elif bull <= 1 and cow > 1:
        note = f"{user_number} = {bull} Bull, {cow} Cows."
        output.config(text= note)
        list_box.insert(0, note)
    elif bull > 1 and cow > 1:
        note = f"{user_number} = {bull} Bulls, {cow} Cows."
        output.config(text= note)
        list_box.insert(0, note)
    elif bull <= 1 and cow <= 1:
        note = f"{user_number} = {bull} Bull, {cow} Cow."
        output.config(text= note)
        list_box.insert(0, note)
    user_input.delete(0, END)

# Funkce na ověření čísla # Funkce tlačítka vyhodnocení čísla
def evaulation():
    """Vyhodnocení čísla zadaného uživatelem
    Pokud je vhodné vyhodnotí se počet bulls and coww"""
    bull = 0
    cow = 0
    user_number = user_input.get()
    if len(user_number) != 4 or not user_number.isnumeric() or int(user_number[0]) == 0 or len(set(list(user_number))) < 4:
        if len(user_number) > 4:
            output1.config(text= "Tvé číslo je příliš dlouhé!")

        elif len(user_number) < 4:
            output1.config(text= "Tvé číslo je příliš krátké!")

        elif not user_number.isnumeric():
            output1.config(text= "Zadaná hodnota není číslo!")

        elif int(user_number[0]) == 0:
            output1.config(text="Číslo nesmí začínat 0!")

        elif len(set(user_number)) != 4:
            output1.config(text="Číslice se nesmí opakovat!")

    elif len(user_number) == 4 and user_number.isnumeric() and len(set(list(user_number))) == 4:
        for num in range(0,4):
            if int(user_number[num]) == new_game_value[num]:
                bull += 1
            elif int(user_number[num]) in new_game_value and int(user_number[num]) != new_game_value[num]:
                cow += 1
    bull_cow(bull, cow) 

# tlačítko pro vyhodnocení 
correct_button = Button(input_frame, text="Vyhodnoť číslo", width=20, bg= dark_brown, fg= light_color2, font= ("Arial", 8, "bold"), command= evaulation)
correct_button.grid(row=0, column=1, padx= 5, pady=20)

# na konci výpis konec hry, čas hry, počet pokusů, nejlepší počet pokusu - potřeba uložit do txt.
end_label = Label(text_frame, font= ("Arial", 15, "bold"), bg= main_color, fg=dark_brown)
end_label.grid(row=0, column= 2)

window.mainloop()