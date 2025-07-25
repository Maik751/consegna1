
import socket
import ipaddress


#creo la funzione per verificare la validità dell'indirizzo IP inserito
def valid_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

print("Ciao! Questo software resta in ascolto su una porta, in attesa di una connessione tcp")
print("Se ti va puoi fornirmi la relativa porta su cui restare in ascolto")

while True:

    volontà = input("Ti va di proseguire? (y/n)")

    if volontà.lower().strip() == "y":
        
        try:
            port = int(input("Fantastico! Procedi dunque a fornirmi la porta su cui mettermi in ascolto: ").strip())
            if not (1 <= port <= 65535):
                print("La porta deve essere compresa tra 1 e 65535.")
                continue
            
        except ValueError:
            print("Devi inserire un numero.")
            continue


        HOST = '0.0.0.0'  # Ascolta su tutte le interfacce disponibili

        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((HOST, port))
            server.listen(1)

            print(f"🟢 Server in ascolto su {HOST}:{port}...")

            conn, addr = server.accept()
            print(f"Connessione stabilita con {addr[0]}:{addr[1]}")

            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Ricevuto: {data.decode().strip()}")
                conn.sendall(b"Messaggio ricevuto\n")

            conn.close()
            print("Connessione chiusa.")
            break

        except Exception as e:
            print(f"Errore durante la creazione del server: {e}")
            continue

    elif volontà.lower().strip() == "n":
        print("D'accordo, alla prossima! Buon proseguimento!")
        exit()

    else:
        print("Mi spiace ma l'input inserito non è corretto, si prega di riprovare.")