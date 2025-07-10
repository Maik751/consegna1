import math
# Si scriva un programma in Python che in base alla scelta dellʼutente permetta di calcolare il perimetro di diverse figure geometriche
# Per la risoluzione dellʼesercizio abbiamo scelto:
# Quadrato (perimetro = lato*4) 
# Cerchio (circonferenza = 2*pi greco*r)
# Rettangolo (perimetro= base*2 + altezza*2)

#creare la funzione che permetta di essere ripetuta
def calcolo_perimetro():
#chiedere all'utente quale figura scegliere
    print("Programma che calcola il perimetro di una figura tra la seguenti:")
    print("Quadrato")
    print("Cerchio")
    print("Rettangolo")

#scelta della figura
    scelta = input("Quale figura scegli?:")

#poniamo le diverse condizioni
    #Quadrato
    if scelta == "Quadrato":
        lato = float(input("Scegli la lunghezza del lato:"))
        perimetro = lato*4
        print(f"Dato che il lato che hai scelto è {lato}, il perimetro sarà: {perimetro}")
    #Cerchio
    elif scelta == "Cerchio":
        raggio = float(input("scegli la lunghezza del raggio:"))
        circonferenza = raggio*2*math.pi
        print(f"Dato che il raggio è {raggio} la circonferenza sarà: {circonferenza}")
    #Rettangolo
    elif scelta == "Rettangolo":
        base = float(input("Scegli la base:"))
        altezza = float (input("Scegli l'altezza:"))
        perimetro = base*2 + altezza*2
        print(f"Data la base {base} e l'altezza {altezza} il perimetro sarà: {perimetro} ")
    else:
        print("Risposta non valida")

calcolo_perimetro()
