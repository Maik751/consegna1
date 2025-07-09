# Scrivi una funzione che analizzi una stringa di testo e restituisca un dizionario con il conteggio delle occorrenze 
# di ciascuna parola. Ignora la punteggiatura e considera le parole in modo case-insensitive.

# richiedere una stringa di testo
# trasformare la stringa in minuscolo
# ignora la punteggiatura
# riconoscere le singole parole
# inserire le parole in un dizionario
# stampare il dizionario

import re

def contatore_parole_stringa(stringa):
    stringa = stringa.lower()
    stringa = re.sub(r"[^\w\s]", '', stringa)
    lista_parole = stringa.split()
    dizionario = {}
    for parola in lista_parole:
        if parola in dizionario:
            dizionario[parola] = dizionario[parola]+1
        else:
            dizionario[parola] = 1
        
    return dizionario

        


testo = "Ciao, ciao! Come stai? Stai bene?"

print(contatore_parole_stringa(testo))

testo = "Eccolo sempre lui! Pippo mio! Pippo mio! sempre Pippo la mette mette"

print(contatore_parole_stringa(testo))