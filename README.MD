# **Software di una rubrica di contatti con Python <br>**


ContactEase Solutions mira a semplificare la gestione dei contatti telefonici per i propri utenti, sviluppando un software intuitivo e interattivo che ottimizza l’organizzazione e l’accesso alle informazioni personali. <br>

Gli utenti spesso trovano difficoltoso gestire e organizzare i loro contatti telefonici in modo efficiente. Esistono poche soluzioni semplici e intuitive che permettano di aggiungere, modificare, eliminare, visualizzare e cercare contatti in un unico luogo, direttamente dal terminale. <br>

ContactEase Solutions fornirà un’applicazione console interattiva che, grazie ai principi della programmazione orientata agli oggetti (OOP) in Python, permetterà una gestione dei contatti semplice e strutturata. Gli utenti potranno facilmente salvare e caricare i contatti in un formato file (ad esempio JSON), garantendo una gestione dati efficiente e sicura. <br>

### **Requisiti del Progetto:** <br>
**OOP in Python:** Implementare i concetti di OOP per una struttura solida e scalabile. <br>
**Struttura Dati:** Creare una struttura di dati efficiente per memorizzare i contatti. <br>
**Interfaccia Utente:** Sviluppare un’interfaccia da linea di comando interattiva e facile da usare.<br>

### **Funzionalità base:**
_- Aggiunta di un Contatto:_ Permettere l'inserimento di nuovi contatti. <br>
_- Visualizzazione dei Contatti:_ Mostrare tutti i contatti presenti. <br>
_- Modifica di un Contatto:_ Consentire la modifica dei dettagli dei contatti esistenti. <br>
_- Eliminazione di un Contatto:_ Rimuovere contatti dalla rubrica. <br>
_- Ricerca di un Contatto:_ Cercare contatti per nome o cognome. <br>
_- Salvataggio e Caricamento:_ Salvare i contatti in un file e caricarli all’avvio. <br>
_- Interfaccia Utente:_ L’interfaccia sarà basata su riga di comando, offrendo un menu principale con opzioni chiare per le varie operazioni, garantendo così una user experience fluida e accessibile anche per gli utenti meno esperti. <br>

### **Funzionalità extra:**
_- Gestione utenze:_ Permettere la login e registrazione degli utenti all'applicazione. Ogni utente potrà accedere esclusivamente alla propria lista di contatti

### **Struttura del Progetto:** <br>
Il progetto è organizzato in diversi package:
- data: contiene i file di salvataggio dei contatti e degli utenti
- models: contiene le classi che rappresentano gli oggetti del progetto
- ui: contiene le classi che gestiscono l'interfaccia utente
- controller: contiene le classi che gestiscono le logiche di CRUD e ricerca dell'applicazione. Questa modaltà è stata scelta per permettere un eventuale integrazione con una GUI o un modulo di frontend dedicato
- service: contiene le classi che gestiscono le logiche di business dall'applicazione