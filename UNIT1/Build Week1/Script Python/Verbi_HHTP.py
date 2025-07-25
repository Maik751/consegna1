
#Presento il programma all'utente
print("Ciao! Tramite questo programma potrai analizzare quali opzioni sono attive su un determinato server HTTP!")
print("Per procedere mi servirà l'indirizzo IPv4 del server da analizzare.")

#importo libreria requests per le richieste http
import requests

#importo libreria ipaddress per il controllo dell'input dell'IP
import ipaddress

#importo libreria ping per testare connessione con il server
from ping3 import ping

#creo la funzione per verificare la validità dell'indirizzo IP inserito
def valid_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

#creo ciclo while
while True:

    #chiedo all'utente se vuole procedere
    volontà = input("Ti va di procedere?(Rispondere solamente si o no) ")

    #Se vuole procedere controllo chiedo l'ip e ne controllo la correttezza
    if volontà.lower() == "si" or volontà.lower() == "sì":
        IP = input("Grandioso! Inserisci qui di seguito l'ipv4 del server da analizzare: ").strip()
        
        #se l'ip non è valido chiedo di riprovare ad inserirlo
        if not valid_ipv4(IP):
            print("L'indirizzo IP inserito non è valido. Riprovare.\n")
            continue
        
        #provo a pingare l'ip dato dall'utente per verificare che sia in rete
        if ping(IP, timeout=2) is None:
            #se non risponde al ping avviso l'utenter e chiedo nuovamente se vuole procedere
            print(f"Il server {IP} non risponde al ping, assicurarsi che sia connesso in rete.")
            continue
        else:
            #altrimenti avviso che il ping è riuscito e procedo con il codice
            print(f"Il server {IP} ha risposto al ping!\n")

        #chiedo all'utente se vuole analizzare una path specifica del webserver
        path = input("Se si vuole, inserire di seguito il path da analizzare (es. /phpMyAdmin) altrimenti lasciare vuoto: ").strip()

        #creo la variabile url su cui verrà effettuata la "scansione"
        url = f"http://{IP}{path}"

        #faccio un check della get request
        get = requests.get(url)
        #se positivo (cod. 200) stampo che l'option è disponibile
        if get.status_code == 200:
            print(f"GET option DISPONIBILE per", url)
        #altrimenti stampo che l'option non è disponibile e stampo anche lo status code per poter eventualmente approfondire il problema
        else:
            print(f"GET option NON DISPONIBILE per", url)
            print(get.status_code)

        #LO STESSO PROCEDIMENTO VIENE RIPETUTO ANCHE PER TUTTE LE ALTRE OPZIONI
        post = requests.post(url)
        #print(post)
        if post.status_code == 200:
            print(f"POST option DISPONIBILE per", url)
        else:
            print(f"POST option NON DISPONIBILE per", url)
            print(post.status_code)


        put = requests.put(url)
        #print(put)
        if put.status_code == 200:
            print(f"PUT option DISPONIBILE per", url)
        else:
            print(f"PUT option NON DISPONIBILE per", url)
            print(put.status_code)


        delete = requests.delete(url)
        #print(delete)
        if delete.status_code == 200:
            print(f"DELETE option DISPONIBILE per", url)
        else:
            print(f"DELETE option NON DISPONIBILE per", url)
            print(delete.status_code)

        #Testate tutte le opzioni interrompo il programma
        break
        
    #Se l'utente non vuole proseguire, lo saluto
    elif volontà.lower() == "no":
        print("Peccato, sarà per la prossima volta! Buona Giornata!")
        exit()

    #Per qualsiasi altro input gli faccio ripetere l'inserimento della risposta
    else:
        print("Mi spiace non comprendo l'input inserito, si prega di riprovare")