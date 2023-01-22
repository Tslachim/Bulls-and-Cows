import random
from time import time
from tkinter import *

# Proměné 
numbers = list(range(0,10))
generated = []
end = True
attemp = 0
main_font = ("Times New Roman", 15)
main_color = "#F2C777"
generated = [9, 7, 5, 3]
note = ""

# Okno 
window = Tk()
window.minsize(500, 500)
window.resizable(False, False)
window.title("Bulls & Cows")
window.iconbitmap("input/bull.ico")
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

# Funkce 
# Tlačítko o pravidlech hry

# Start nove hry 
def new_game():
    for _ in range(0,4):
        num = random.choice(numbers)
        generated.append(num)
        numbers.remove(num)

    while generated[0] == 0:
        generated[0] == random.choice(numbers)
 
    start_time = time()
    attemp = 0
    list_box.delete(0, END)
    
# Funkce na ověření čísla # Funkce tlačítka vyhodnocení čísla
def evaulation():
    number = user_input.get()
    if len(number) != 4 or not number.isnumeric() or int(number[0]) == 0 or len(set(number)) < 4:
        if len(number) > 4:
            output.config(text= "Tvé číslo je příliš dlouhé!")
        elif len(number) < 4:
            output.config(text= "Tvé číslo je příliš krátké!")
        elif not number.isnumeric():
            output.config(text= "Zadaná hodnota není číslo!")
        elif int(number[0]) == 0:
            output.config(text="Číslo nesmí začínat 0!")
        elif len(set(number)) != 4:
            output.config(text="Číslice se nesmí opakovat!")
    else:
        bull = 0
        cow = 0 
        global attemp
        attemp += 1
        for num in range(0,4):
            if int(number[num]) == generated[num]:
                bull += 1
            elif int(number[num]) in generated and int(number[num]) != generated[num]:
                cow += 1

        if bull == 4:
            stop_time = time()
            note = f"{number} = 4 Bulls, 0 Cow"
            end_label.config(text= "Uhádl jsi všechny čtyři čísla!")
        elif bull > 1 and cow < 1:
            note = f"{number} = {bull} Bulls, {cow} Cow."
            output.config(text= note)
            list_box.insert(0, note)
        elif bull < 1 and cow > 1:
            note = f"{number} = {bull} Bull, {cow} Cows."
            output.config(text= note)
            list_box.insert(0, note)
        elif bull > 1 and cow > 1:
            note = f"{number} = {bull} Bulls, {cow} Cows."
            output.config(text= note)
            list_box.insert(0, note)
        elif bull < 1 and cow < 1:
            note = f"{number} = {bull} Bull, {cow} Cow."
            output.config(text= note)
            list_box.insert(0, note)
    user_input.delete(0, END)


# Hlavní nadpis - Label
title = Label(title_frame, text="Vítejte ve hře", bg= main_color, fg="#8C442A", font= ("Arial", 15, "bold"))
title.pack(pady= 5)
title1 = Label(title_frame, text="Bulls & Cows", bg= main_color, fg="#8C442A", font= ("Arial", 30, "bold"))
title1.pack(pady= 10)

# popis - label
code = """
Bull/s  = počet uhádnutých čísel, uhádnutých pozic
Cow/s   = počet uhádnutých čísel, špatných pozic
"""
info = """Stiskni 'Nová Hra'
Poté zadej čtyřcifené číslo, které nezačíná 0
Zároveň se číslice nesmí opakovat"""

descri = Label(info_frame, text= code, bg= main_color, fg="#8C442A", font= ("Arial", 8, "italic"))
descri.grid(row= 0, column= 0)

description = Label(info_frame, text= code, bg= main_color, fg="#8C442A", font= ("Arial", 8, "italic"))
description.grid(row= 1, column= 0)

# New game - button, Exit - button
new_g = Button(info_frame, text="Nová hra", width=20, bg= "#8C442A", fg= main_color, font= ("Arial", 10, "bold"), command= new_game)
new_g.grid(row=1, column=1, padx= 5, pady=10)

# tlačítko na pravidla hry 
rules = Button(info_frame, text= "Pravidla hry", bg= "#8C442A", fg= main_color, font= ("Arial", 8, "italic"))
rules.grid(row= 0, column= 1, padx=30, pady= 20, ipadx= 5, ipady= 5)

    # Zapis pravidel hry do vyhodnocovacího Labelu s popiskem jak hrát 


# Hádané číslo (input)  # místo pro zapsání že číslo je dlouhé, krátké, začíná nulou .... a Bull and Cows
user_input = Entry(input_frame, text= "Zde zadej číslo", width= 8)
user_input.grid(row= 0, column= 0, padx= 15)

# tlačítko pro vyhodnocení 
correct_button = Button(input_frame, text="Vyhodnoť číslo", width=20, bg= "#8C442A", fg= main_color, font= ("Arial", 8, "bold"), command= evaulation)
correct_button.grid(row=0, column=1, padx= 5, pady=20)

# aktuální Bull and Cow případně chyba zadání
output = Label(input_frame, text= "", bg= main_color, fg="#8C442A", font= ("Arial", 8, "italic"))
output.grid(row= 0, column=2, padx=5)

# seznam neuhádnutých čísel a u nich Bull and Cow - textové okno se scrolbarem
list_box = Listbox(text_frame, width= 25, height= 10, bg= main_color, fg= "#8C442A", font= ("Arial", 8,))
list_box.grid(row= 0 ,column= 0)

scroll_bar = Scrollbar(text_frame, bg= "#8C442A")
scroll_bar.grid(row= 0, column= 1, sticky="NS")

# na konci výpis konec hry, čas hry, počet pokusů, nejlepší počet pokusu - potřeba uložit do txt.
end_label = Label(text_frame, font= ("Arial", 10, "bold"), bg= main_color, fg="#8C442A")
end_label.grid(row=0, column= 2)


window.mainloop()
