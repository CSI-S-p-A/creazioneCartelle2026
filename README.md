# Creazione Cartelle ENCAP (2026)
In questo readme ho scritto principalmente le procedure di base per modificare e espandere il codice, non per l'effettivo uso.

## Git
Per la gestione del codice e l'update dello script ho usato un programma si chiama "git". E' lo standard nella scrittura di codice da robe semplici a progetti mega complessi. 

Serve principalmente per salvare delle "fotografie" del codice a vari instanti, in modo tale da non perdere progressi se si fa qualche cavolata.

Si puo' usare in vari modi, la versione piu' "pura" e' attraverso comandi da terminale.
Io personalmente uso un tool alternativo da terminale che si chiama "lazygit" e che ho installato anche sul desktop remoto.

Io ti consiglio pero' di usare la scheda "Source Control" di Visual Studio Code se stai usando gia' quello come editor.

![alt text](readme_resources/source_control.jpg "Title")

In git i progetti vengono chiamate "Repository" (repo per abbreviare) e possono essere tenute "in locale" se restano solo sul tuo pc o "in remoto" se vengono uploadate su un sito esterno come GitHub.com.

### Comandi

I comandi principali di cui ti interessa sono:
- git pull

Quando ci sono delle modifiche nella repo in remoto che vuoi vengano "scaricate" nei tuoi file su cui vuoi lavorare. In VSCode c'e' questo tasto che esegue un pull se premuto
![alt text](readme_resources/git_pull.jpg "Title")
- git add [nome_file]

Quando hai fatto delle modifiche ai file e vuoi selezionare di quali file vuoi fare la "fotografia" (VSCode lo fa automaticamente quando fai il commit).

- git commit -m "[messaggio]"

Una volta che hai selezionato i file, puoi fare effettivamente la "fotografia" al progetto con questo comando. Ogni commit ha anche un messaggio obbligatorio in cui si spiega brevemente quello che si e' fatto.

In VSCode basta andare nella schermata di source control, scrivere il messaggio di commit nella casella di testo e premere il pulsante "Commit".

- git push

Il "commit" salva i file nel progetto in locale sul tuo PC. Se vuoi fare l'upload di quello che hai committato su GitHub devi fare questo passaggio in piu'.

Su VSCode c'e' il pulsante per il push nella stessa riga di quello per il pull.

## UV

In Python per la gestione delle dipendenze si usa una cosa chiamata "virtual enviroment", che permette di installare i pacchetti solo nella cartella specifica del progetto in cui stiamo lavorando, invece che in tutto il PC.

Per l'installazione dei paccheti invece si usa un tool che si chiama "pip", che cerca su internet il pachetto che gli richiedi e lo installa (o localmente o nel virtual enviroment).

Per facilitarmi tutto questo processo ho deciso di usare un tool che si chiama "UV" che sostituisce entrambi gli strumenti.

(Si puo' usare solo da terminale e bisogna essere nella stessa cartella del progetto)

I comandi che vi servono sono:
- uv add [nome pacchetto]

Per installare un pacchetto
- uv remove [nome pacchetto]

Per disinstallarlo

- uv run .\main.py

Per far partire lo script (in questo caso main.py) e installare automaticamente eventuali pacchetti che non sono gia' installati.

# Qt
Qt e' un framework che si usa per fare applicaioni con interfaccia. Si puo' usare con vari linguaggi di programmazione e con varie implementazioni. Quella che ho usato io si chiama "pyside6", ed e' un implentazione open source per python. 
Ho installato il pacchetto con UV (uv add pyside6).

Io sconsiglio vivamente di andare a toccare nello specifico il codice relativo a Qt e soprattutto di andare a modificare il file in cui ho definito la UI.

Nel caso pero' sia strettamente necessario ti dico quali sono le procedure che ti permettono di farlo.

Il programma per editare la ui si chiama "Qt Designer" e lo puoi trovare nel seguente percorso:
```bash
/.venv/Lib/site-packages/PySide6/designer.exe
```
Se non vedi la cartella ".venv" nella cartella del progetto prova o a far partire il programma una volta con uv run, oppure abilita la visualizzazione delle cartelle nascoste (cerca su Google come fare).

Una volta aperto il programma puoi aprire il file "window.ui" che si trova nella cartella del progetto premendo sul tasto "Open".

![alt text](readme_resources/qt_designer.jpg "Title")

Il programma e' abbastanza complesso e se devi effettivamente fare delle modifiche pesanti conviene che guardi qualche tutorial. 

La cosa base e' trascinare componenti dalla toolbar a sinstra e trascinarle nella schermata. Le proprieta' dell'oggetto si possono modificare nella tabella di sinistra. 

Alcune cose sono intuitive ma fallo a tuo rischio e pericolo.

Dopo aver fatto le modifiche salva quello che hai fatto in un file (io consiglio di fare salva con nome e di non sovrascrivere il mio window.ui).

Una volta che hai il file, questo non viene letto automaticamente da python, va convertito in .py.

Il modo per farlo e' il seguente:
- Entra in un terminale situato all'interno della cartella del progetto
- Attiva manualmente il virtual enviroment (altrimenti non funziona)

Per attivarlo incolla il seguente comando nel terminale e premi invio:
```bash
.\.venv\Scripts\activate
```
Sai che il virtual enviroment e' stato attivato dal fatto che prima della cartella di lavoro nel terminale c'e' il nome del progetto:
![alt text](readme_resources/venv.jpg "Title")

A questo punto incolla e fai partire questo comando:
```bash
pyside6-uic window_new.ui -o window.py
```
Dove "window_new" e' il nome che hai dato al file .ui che hai salvato da Designer, mentre "window.py" e' il file python di output. E' importante che il nome dell'output rimanga window.py, altrimenti non verra' riconosciuto dal main.py e dagli altri file.

## Aggiungere o Modificare Test/Parametri/Robustness
Il programma e' stato scritto in modo tale che non sia necessario andare troppo a toccare il codice, le principali modifiche si possono fare modificando i file database ".json" presenti nella cartella del test.

### JSON
I file json sono dei file che permettono di rappresentare informazioni in maniera abbastanza leggibile. Non serve sapere molto e l'internet nel caso e' pieno di informazioni, espongo i concetti piu' importanti ma che puoi facilmente dedurre guardando tu stesso i file.

In un json puoi rappresentare liste (array) che sono contenute da parentesi quadre "[ ]" e separate da virgole, numeri interi, numeri reali, stringhe (contentue nelle virgolette), booleani (vero o falso) e sequenze di coppie chiave/valore contenute da parentesi graffe "{ }", associate dai due punti ":" e separate da delle virgole.

Un oggetto completo e' la composizione di tutte queste cose.

Questo e' ad esempio il file "test_types.json" che contiene la lista di test che vengono mostrati nella prima schermata dove ci solo le due

```json
{
  "test_list": [
    {
      "type": "AEBC",
      "tests": ["CCRs", "CCRm", "CCRb", "CCFhos", "CCFhol", "CCFtap", "CCCscp"]
    },
    { "type": "AEBM", "tests": ["CMRs", "CMRb", "CMFtap", "CMCscp"] },
    {
      "type": "AEBP",
      "tests": [
        "CPLA",
        "CPTA",
        "CPNA",
        "CPFA",
        "CPNCO",
        "CPMRCm",
        "CPMRCs",
        "CPMFC"
      ]
    },
    {
      "type": "AEBB",
      "tests": ["CBLA", "CBTA", "CBNA", "CBFA", "CBNAO", "CBDA"]
    },
    {
      "type": "LSS",
      "tests": ["ELK-RE", "ELK-ON", "ELK-OV"]
    }
  ]
}
```
Come si puo' vedere c'e' la chiave "test_list" che e' associata alla lista di oggetti formati dalle chiavi "type" e "test".

Alla chiave "type" e' associata la stringa del nome del test e alla chiave "tests" e' associata una lista di stringhe con i nomi dei test che fanno parte di quel tipo.

Se dovessi aggiungere un nuovo tipo di test dovrei inserire una virgola dopo la penultima parentesi graffa e incollare un oggetto di questo tipo:
```json
{
  "type":"NEWTYPE",
  "tests":["TEST1","TEST2","TEST2"]
}
```
Editor (Come VSCode) hanno sempre una modalita' di visualizzazione dei json che permette di capire l'organizzazione delle varie strutture e che ti segnalano errori nel caso fai errori di notazione.

Il mio consiglio e' quello di copiare quello che c'e' gia' e di inventarsi il meno possibile, stando attenti ai vari dettagli come maiuscole, minuscole, tipo di valore (cosa e' una stringa, cosa e' un numero etc...).

Un errore comune ad esempio e' trattare un valore come una stringa e di mettere sempre le virgolette:
```json
{
  "key1": false,
  "key2": "false",
  "key3": 32,
  "key4": "32"
}
```
Le chiavi sono sempre stringe, mentre il valore puo' anche non esserlo, e se si sbaglia il programma non riesce correttamente a leggerlo dal file.

Ora spiego un po' piu' nel dettaglio come gestire la modifica dei vari json.

### Aggiungere un Test
E' difficile che sia necessario aggiungere un'intero tipo di test, la cosa piu' probabile e' che ci sia bisogno di aggiungere uno specifico test che magari e' stato introdotto dopo o mi sono dimenticato di aggiungere.

Le due cose principali sono: 
- aggiungere il test nell file "test_types.json"

basta inserire il nome del test come stringa alla fine dell'array del tipo specifico.

- aggiungere il file [nome_test].json (tutto minuscolo) nella cartella "test_json".

Per le informazioni all'interno conviene copiare il contenuto di un'altro test con variabili simili e modificare solo lo stretto necessario.

Nello specifico questi sono i due tipi di parametri che possono essere all'interno di un test:

Questo e' l'esempio di una variabile che e' sempre fissa per il tipo di test e non ha bisogno di essere inserita dall'utente.

- "key" e' il parametro piu' importante e definisce il nome identificativo del test.
- "user_input" identifica se c'e' bisogno dell'input dell'utente e quindi di creare la UI nel programma e di piu' scelte.
- "value" e' il valore effettivo, se il valore e' vuoto (come la target_speed in un test di linee) si usa la stringa "NOVALUE"

```json
   {
      "key": "target_speed",
      "user_input": false,
      "value": 10.0
    },
```
Nel caso invece "user_input" = true, c'e' bisogno di piu' informazioni:

- "display_name" e' il nome che viene mostrato nella schermata di selezione dei parametri a sinistra del menu' a tendina
- "default" e' il valore predefinito del menu' a tendina ("default" va SEMPRE messo se il parametro e' variabile)
- "options" contiene la lista di oggetti che contengono i valori possibili
  - "value" e' il valore effettivo che verra' poi messo nell'MME
  - "label" e' la scritta che e' presente nel menu' a tendina per selezionare il valore corrispondente. La scritta poi comparira' nella tabella dopo che e' stato aggiunto il test e nel nome della cartella del test
  

```json
{
      "key": "long_speed_VUT",
      "display_name": "VUT Speed",
      "user_input": true,
      "default": 10.0,
      "options": [
        { "value": 10.0, "label": "10 kph" },
        { "value": 20.0, "label": "20 kph" },
        { "value": 30.0, "label": "30 kph" },
        { "value": 40.0, "label": "40 kph" },
        { "value": 50.0, "label": "50 kph" },
        { "value": 60.0, "label": "60 kph" },
        { "value": 70.0, "label": "70 kph" },
        { "value": 80.0, "label": "80 kph" }
      ]
    },
```

La lista di parametri per ogni test e' sempre la stessa e' ogni parametro e' necessario per completare il file MME.

### Modificare/Aggiungere Robustness
Le robustness sono presenti nel file robustness.json. La struttura del file e' molto simile a quello dei vari test. La differenza principale e' che ci sono tre "livelli":
Type, Layer e Parameter.

Alcune robustness hanno solo il type, altre il type e il layer e altre ancora hanno tutti e tre i parametri.

### TODO

Nel codice ho aggiunto alcuni commenti che iniziano con "TODO" in cui ho messo modifiche al codice che mi sono venute in mente e non sono riuscito a fare.
Alcune sono assolutamente necessarie per le funzionalita' del software, altre invece sono piu' aggiornamenti di quality of life.

Notare bene che non sono assolutamente le uniche modifiche da fare, il protocollo e' cambiato piu' volte da quando ho iniziato il progetto ed e' probabile che cambiera' ancora.

La cosa migliore da fare e' guardare il codice (o inizialmente l'output del programma se non si vuole subito entrare nel dettaglio) e verificare che questo rispetti TUTTE le specifiche espresse nel protocollo.
