import datetime 
def assistente_virtuale():
    print("Ciao sono il tuo assistente virtuale, puoi farmi diverse domande:")
    print("1 Data di oggi")
    print("2 Orario")
    print("3 Il mio nome")
    comando_virtuale = input("Scegli la domanda 1, 2 o 3: ")  
    if comando_virtuale == "1":        
            oggi = datetime.date.today()          
            risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")
            print(risposta)   
    elif comando_virtuale == "2":        
            ora_attuale = datetime.datetime.now().time()         
            risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")
            print(risposta)    
    elif comando_virtuale == "3":        
            risposta = "Mi chiamo Assistente Virtuale"
            print(risposta)    
    else:       
        risposta = "Non ho capito la tua domanda." 
        print(risposta) 

    while True:
        comando_utente = input("Vuoi farmi un'altra domanda? (Si o No): ")    
        if comando_utente == "No":       
            print("Arrivederci!")
            break
        elif comando_utente == "Si":        
            input(assistente_virtuale())
        else:
             print("Comando non riconosciuto")
             break 
    
assistente_virtuale()