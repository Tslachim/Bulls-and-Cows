"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Michal Stuchlík 
email: tslachim@gmail.com
discord: Mišakus#1763
"""
import random
from time import time

print("""Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
""")

# nahodné vygenerování čtyřciferného čísla, které nesmí začínat nulou

numbers = [0,1,2,3,4,5,6,7,9,]
generated = []
end = True
bull = 0
cow = 0
attemp = 0

for i in range(0,4):
    num = random.choice(numbers)
    generated.append(num)
    numbers.remove(num)

while generated[0] == 0:
    generated[0] == random.choice(numbers)

# uživatel zadá čtyřčíselné číslo number = input("")
    # pokud bude kratší, nebo delší upozorní ho a nechá ho to vypsat znova
    # if len(number) > 4: print je delší
    # elif len(number) < 4: print je kratší 
    # číslo nesmí začínat 0 
    # číslo nesmí být duplicitní
print(generated)
start_time = time()
while end:
    while len(number := input("Enter a four-digit number:\n")) != 4 or not number.isnumeric() or int(number[0]) == 0 or len(set(number)) < 4:
        if len(number) > 4:
            print("Your number is too long. Write four-digit number!")
        elif len(number) < 4:
            print("Your number is too short. Write four-digit number!")
        elif not number.isnumeric():
            print("Your choice is not number. Try again!")
        elif int(number[0]) == 0:
            print("Number must not start with 0")
        elif len(set(number)) != 4:
            print("Numbers must be unique!")

    # počitadlo kolikrát je potřeba zadávat (správné) číslo 
    attemp += 1

    # vytvořit promněné na Cows and Bulls 
    # pokud je uživatelské číslo v generated pak cows, pokud je se stejným indexem tak bull přes funkci for?

    for num in range(0,4):
        if int(number[num]) == generated[num]:
            bull += 1
        elif int(number[num]) in generated and int(number[num]) != generated[num]:
            cow += 1

    # Vypiš počet Bull and Cow a pokud to je to množné číslo tak /s      přes funkci if pokud zjistíš jestli je to množné nebo jednotné
    print(20 * "-")
    print(f"{bull} Bull") if bull <= 1 else print(f"{bull} Bulls"), print(f"{cow} Cow") if cow <= 1 else print(f"{cow} Cows")
    print(20 * "-")
    # v případě uspěšného uhádnutí ukončit cyklus!

    if bull == 4:
        end = False
        stop_time = time()
        
    # vymazat hodnoty bull and cow aby počítání neovlivnilo další kolo 
    bull = 0
    cow = 0
    
game_time = round(stop_time - start_time, 1)

print(f"""You find all numbers, You win!
{30 * '='}
Your time is: {game_time}/s 
your number of attemps: {attemp} 
{30 * '='}""")
