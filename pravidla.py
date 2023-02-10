from tkinter import Tk,Label

main_color = "#F2C777"
dark_brown = "#401201"

rules_note_1 = """
Uhádnout čtyřciferné číslo ve správném pořadí\n
Máš neomezený počet pokusů\n
Musíš zadat čtyřciferné číslo,
které nezačíná 0,
čisla se nesmí opakovat(4444)\n
"""
rules_note_2 = """
Je to počet uhádnutých číslic, s nesprávnou pozicí.\n
Hádané číslo pro příklad je 1234
Pokud zadám hodnotu 2871 tak Cows = 2\n 
Uhádnul jsem čísla 2,1 ale jsou na špatné pozici.
 """

rules_note_3 = """
Je to počet uhádnutých číslic, na správné pozici.\n
Hádané číslo pro příklad je opět 1234
Pokud zadám hodnotu 1287 tak Bulls = 2\n 
Uhádnul jsem čísla 1,2 a mají správnou pozici.

Pokud bych zadal 1782, pak Bull = 1, Cow = 1
"""

def open_rules():
    w_rules = Tk()
    w_rules.minsize(300, 500)
    w_rules.title("Pravidla Hry")
    w_rules.resizable(False, False)
    w_rules.iconbitmap("bull.ico")
    w_rules.config(bg=main_color)

    rules_title = Label(w_rules, text= "Pravidla hry Bulls and Cows", bg= main_color, fg=dark_brown, font= ("Arial", 25, "bold"))
    rules_title.grid(row= 0, column= 1, pady=15, padx=15)

    rules_title_1 = Label(w_rules, relief="raised", anchor="w", borderwidth=3, text= "Cíl hry:", bg= main_color, fg=dark_brown, font= ("Arial", 15, "bold"))
    rules_title_1.grid(row=1, column=0, padx=30)
    rules_text_1 = Label(w_rules, text= rules_note_1, anchor="w", bg= main_color, fg=dark_brown, font= ("Arial", 12, "bold"))
    rules_text_1.grid(row=1, column=1, pady=10)

    rules_title_2 = Label(w_rules, relief="raised", anchor="w", borderwidth=3, text= "Vysvětlení Cow/s:", bg= main_color, fg=dark_brown, font= ("Arial", 15, "bold"))
    rules_title_2.grid(row=2, column=0, padx=30)
    rules_text_2 = Label(w_rules, text= rules_note_2, anchor="w", bg= main_color, fg=dark_brown, font= ("Arial", 12, "bold"))
    rules_text_2.grid(row=2, column=1, pady=10)

    rules_title_3 = Label(w_rules, relief="raised", anchor="w", borderwidth=3, text= "Vysvětlená Bull/s", bg= main_color, fg=dark_brown, font= ("Arial", 15, "bold"))
    rules_title_3.grid(row=3, column=0, padx=30)
    rules_text_3 = Label(w_rules, text= rules_note_3, anchor="w", bg= main_color, fg=dark_brown, font= ("Arial", 12, "bold"))
    rules_text_3.grid(row=3, column=1, pady=10)






# w_rules.mainloop() # tohle nebudu potřebuovat při volání funkce Pravidel hry 