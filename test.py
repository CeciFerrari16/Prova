adj1 = [ "bene", "meglio", "traquilla", "molto bene", "normalmente", "a meraviglia", "egregiamente", "d'incanto", "degnamente"]
adj2 = [ "male", "peggio", "molto male", "male, non mi parlare", "infelicemente", "rovinosamente"]

print("Ciao!!")
print("Sto testando le mie conoscenze facendo alcune prove sul terminale e riutilizzando comandi "\
"imparati anche l'anno scorso...")
input()
print("Come va la vita? :)")
print()
print("Puoi scegliere tra queste opzioni per rispondere: (oppure puoi personalizzarla)")
print("Positivo:", "; ".join(adj1))
print("Negativo:", "; ".join(adj2))
print()
vita = input("La tua risposta: ").lower()
pos = vita in adj1
neg = vita in adj2
# dà una risposta True or False
if pos == True:
    print("Ah quindi la tua vita prosegue", vita)
    print("Sono contenta!!")
elif neg == True:
    print("Ah quindi la tua vita prosegue", vita)
    print("Mi dispiace molto :( ")
else:
    print("Ah quindi", vita)
print()
print("Ad ogni modo se va bene o male, non abbandonare mai la speranza.")
print("E se non riesci in qualcosa ricordati che tutte le cose sono difficili prima di diventare facili, "\
    "quindi continua a provare e non ti arrendere.")
print("Conto su di te! <3")