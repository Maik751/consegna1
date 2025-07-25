import os
import socket
import ipaddress

print("Questo programma scansionerà le porte aperte di un determinato dispositivo")
while True:
    volontà = input("Mi servirà un l'indirizzo IPv4 che vuoi scansionare. Vuoi procedere? (si o no)")
    if volontà.lower() == "si" or volontà.lower() == "sì":
        target = input("Inserisci un indirizzo IP: ")
        #response = os.system("ping -c 4 " + target)
        try:
            ipaddress.IPv4Address(target)    
            response = os.system("ping -c 1 " + target)
            if response == 0:
                print("Connesso")
            else:
                print("Non raggiungibile")
                continue   
            break
        except ValueError:
            print("Inserisci un IP valido. Riprova.")
    elif volontà.lower() == "no" :
        print("Va bene, arrivederci!")
    else:
        print("Non capisco il tuo input,riprova")

while True:
        ##ping all'ip dell'input
    portrange = input("Inserisci un range di porte (es.1-1024): ")
    try:
        porte = portrange.split("-")
        if len(porte) != 2:
            raise ValueError
        low_port = int(portrange.split("-")[0])
        high_port = int(portrange.split("-")[1])
        if not (1 <= low_port <= 65535 and 1 <= high_port <= 65535 and low_port <= high_port):
            raise ValueError
        break
    except ValueError:  
        print(f"Errore: Formato range porte non valido. Metti prima il valore più basso. Riprova.")

print(f"\nScan di {target} dalla porta {low_port} alla porta {high_port}")    

lista_chiusi= []
for port in range(low_port, high_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if(status == 0):
        print("*** Port", port, "- OPEN ***")
        if port == 23:
            print("Attenzione porta 23 vulnerabile, preferire ssh porta 22")
        elif port == 80:
            print("Attenzione meglio utilizzare porta 443")
        elif port == 21:
            print("Porta 21 non sicura, usare le porte 989 e 990 per connessioni sicure")
        elif port == 25:
            print("Porta 25 soggetta a spam e attacchi, si consiglia di utilizzare la 465")
        elif port == 139:
            print("Particolare attenzione alla 139, configurare correttamente")
        elif port == 445:
            print("Aggiornare la versione e configurare bene il firewall")
        elif port == 513:
            print(" Configurare con attenzione, disabilitare se non necessaria")
        elif port == 514:
            print("Configurare e proteggere adeguatamente")
    else:
        lista_chiusi.append(port)
        s.close()
risposta = input("Vuoi vedere anche le porte chiuse? Y/N ")  
if risposta.lower()== "y":
    print(lista_chiusi)
else:
    print("Arrivederci")