"""Esercizio 1 Abbiamo la stringa: nome_scuola = "Epicode"
 Stampare ogni carattere della stringa, uno su ogni riga, utilizzando un costrutto while."""

nome_scuola="Epicode"
count= 0 #inizializazzione
while count < len(nome_scuola):#mentre
    print(nome_scuola[count])
    count += 1


#Esercizio Stampare a video tutti i numeri da 0 a 20 utilizzando il costrutto while. Utilizzeremo: un ciclo while la funzione print() una variabile, che dovrà essere inizializzata una procedura di incremento

conta = 0

while conta <= 20:
    print("sono al", conta)
    conta += 1
#Esercizio Calcolare e stampare tutte le prime 10 potenze di 2 (e.g., 2⁰, 2¹, 2², …) utilizzando un ciclo while.
base=2
potenzamax = 10
esponente = 0

while esponente <= 10:
    x = base ** esponente
    print("le potenze di  due", [x])
    esponente += 1

#Calcolare e stampare tutte le prime N potenze di 2 utilizzando un ciclo while, domandando all'utente di inserire N.


numero = int(input("Inserisci un numero: "))
potenza = 0

while potenza< numero:
    print(2**potenza)
    potenza += 1


#Calcolare e stampare tutte le potenze di 2 minori di 25000.
    

num = 2
esponente = 0
massimo = 2500

while num**esponente < massimo:
    print(num**esponente)
    esponente += 1

#Abbiamo due liste, una di studenti e una di corsi: studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"] 
    #corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend"]
    #Aggiungere i dati mancanti alla lista corsi, 
    #sapendo che Emma segue Data Analyst Faith segue Backend Grace segue Frontend Henry segue Cybersecurity 
    #Aggiungeremo i dati mancanti uno alla volta con il metodo per appendere in coda alle liste,
    # poi verificheremo che sono della stessa lunghezza e se lo sono stamperemo la lista corsi. 
    #Se alcuni dati sono già presenti non vanno aggiunti di nuovo

listastu = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
listacorsi = ["Cybersecurity",  "Backend", "Frontend", "Data Analyst", "Backend"]

listacorsi.append("Data Analyst (Emma)")  
listacorsi.append("Backend (Faith)")       
listacorsi.append("Frontend (Grace)")      
listacorsi.append("Cybersecurity (Henry)") 

if len(listastu) == len(listacorsi):
    print("Le liste sono della stessa lunghezza.")
else:
    print("Le liste hanno lunghezze diverse.")

    print("Lista Corsi:", listacorsi)




     #Scriviamo un programma che chiede in input all'utente una stringa e visualizza i primi 3 caratteri, seguiti da 3 punti di sospensione e quindi gli ultimi 3 caratteri (Stavolta facciamo attenzione a tutti i casi particolari, ovvero implementare soluzioni ad hoc per stringhe di lunghezza inferiore a 6 caratteri)

insertutente=input("inserisci un texto")

lunghezzatxt= len(insertutente)

if lunghezzatxt < 6:
    print("La stringa è troppo corta.devi inserire almeno 6 caratteri grazie ")
else:
    # Stampiamo i primi 3 caratteri, seguiti da 3 punti di sospensione, e infine gli ultimi 3 caratteri
   
    print("Il risultato è:", insertutente[0:4]+ "... " + insertutente[-3:])
    

#Memorizza e stampa tutti i divisori di un numero dato in input. Esempio: • input: 150 • output: [2, 3, 5, 5]

numeri = int(input("Inserisci un numero: "))

divisore = 1

while divisore <= numeri:
    if numeri % divisore == 0:
        print(divisore)
    divisore += 1


    #Calcolare (ma non stampare) le prime N potenze di K; ognuna di esse andrà memorizzata in coda a una lista. Alla fine, stampare la lista risultante. Proviamo con diversi valori di K, oppure facciamola inserire all'utente.
K = int(input("Inserisci un numero per K: "))
N= int(input("Inserisci il numero di potenze N: "))

# Inizializziamo una variabile per memorizzare le potenze di K
Listak = []
esponente = 0
while esponente < N:
    potenza = K ** esponente
    Listak.append(potenza)
    esponente += 1
print("Le prime ",N , "Potenze di:",K,"sono",Listak)
  
    #Abbiamo una lista con i guadagni degli ultimi 12 mesi: guadagni = 
#[100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50] 
#usando un costrutto while, calcolare la media dei guadagni e stamparla a video.
Listaguadagni=[100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50] 
Sommaguadagni=0                   #perche stiamo x sommare i guadagni da 0 
contatore=0  #perche iniziamo dal primo mese


while contatore < len(Listaguadagni): 
    Sommaguadagni = Sommaguadagni+Listaguadagni[contatore] # Aggiungiamo il guadagno corrente alla somma. #guadagni mensili, uno alla volta, nella variabile 
    #listaguadagni contatore significa "prendi l'elemento nella lista guadagni che si trova alla posizione xcontatore indicato 0
    contatore += 1

media_guadagni = Sommaguadagni / len(Listaguadagni)
#Ora che abbiamo la somma tota dividiamo questa somma per il numero totale di mesi per ottenere la media.

print("La media guadagni  degli ultimi 12 mesi è: ", media_guadagni)
#Abbiamo una lista di codici fiscali: lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"] • 
#trovare i codici fiscali che contengono "95", metterli in una lista, e
# alla fine stamparla; • inoltre, per ognuno di essi, stampare a video i caratteri 
#relativi al nome e quelli relativi al cognome
lISTACF=["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]
lista95 = []

# Iteriamo attraverso ogni codice fiscale nella lista
for cf in lISTACF:
    # Verifichiamo se la stringa "95" è presente nel codice fiscale
    if "95" in cf:
        # Se sì, aggiungiamo il codice fiscale alla lista cf_con_95
       lista95.append(cf)

# Stampiamo la lista risultante
print(" I Codici fiscali che hanno  il 95:", lista95)
#Abbiamo tre liste della stessa lunghezza, dove ogni elemento nella medesima posizione 
#si riferisce ai dati dello stesso studente: 
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"] 
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend", "Frontend", "Cybersecurity"] 
edizioni = [1, 2, 3, 2, 2, 1, 3, 3] 
studentiprimaedizione = []
indice = 0
while indice < len(studenti):
    if edizioni[indice] == 1:
        # Se l'edizione è 1, aggiungiamo  a studenti primaedizione[]
        studentiprimaedizione.append(studenti[indice])
    indice += 1
print("Studenti che frequentano  il corso con la prima edizione:", studentiprimaedizione)
   


   
    #Abbiamo una lista di stringhe di prezzi in dollari, che erroneamente sono stati scritti con il simbolo dell'euro: prezzi = ["100 €", "200 €", "500 €", "10 €", "50 €", "70 €"] cambiare il simbolo dell'euro (€) in quello del dollaro ($) per ogni stringa nella lista; il risultato sarà memorizzato in un'altra lista.
   
dollariprezzi=["100 €", "200 €", "500 €", "10 €", "50 €", "70 €"]
cambiareSimbolosollari=[]
cont=0

while cont < len(dollariprezzi):
    if "€" in dollariprezzi[cont]:
        pezzodollaro= dollariprezzi[cont].replace("€", "$")
        cambiareSimbolosollari.append(pezzodollaro)
    cont += 1

print("Nuova lista in dollari:", cambiareSimbolosollari)
 #Abbiamo una lista di studenti: studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry", "Isabelle", "John"] vogliamo dividere gli studenti in due squadre per un campionato di Uno nel seguente modo: selezioneremo i nomi in posizione pari per un squadra, e i nomi in posizione dispari per l'altra. Creiamo due liste per ogni squadra, e alla fine visualizziaone.
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry","Isabele","Jhon"]

primasquadrapar=[]
secondasquadradis=[]
indice=0

indice = 0
while indice < len(studenti):
    #estraiamo nome ogni volta singolarmente 
    Studente_name= studenti[indice]
    if indice % 2 == 0:
        
        primasquadrapar.append(Studente_name)
    else:
        # Posizione dispari, aggiungi alla squadra_dispari
        secondasquadradis.append(Studente_name)
    
    
    indice += 1
print("Squadra Pari:", primasquadrapar,"squadradispari", secondasquadradis)