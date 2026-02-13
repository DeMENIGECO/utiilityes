
**utiilityes** è una piccola libreria Python pensata per creare GUI moderne e semplici, basate su SDL2.  
L’obiettivo è offrire un’interfaccia fluida, leggibile e immediata, senza dover scrivere codice complesso.

---

## ✨ Caratteristiche

- API semplice e leggibile
- Creazione rapida di finestre e pulsanti
- Sistema di callback per gestire eventi
- Stile moderno basato su SDL2
- Include un file `example.py` pronto all’uso

---

## 📦 Installazione

Dopo la pubblicazione su PyPI, sarà possibile installare la libreria con:
pip install utiilityes


---

## 🚀 Esempio di utilizzo

Puoi trovare un esempio completo nel file `example.py` incluso nel pacchetto.

Ecco un estratto:

```python
from utiilityes import Index as ind

if __name__ == "__main__":
    def saluto():
        print("Hai cliccato SALUTA!")

    def esci():
        print("Esco...")
        raise SystemExit

    ui = ind.Index()

    ui.init.win("Example")\
          .size(600, 400)

    ui.run_funct()\
      .text("Benvenuto nella GUI SDL2!")\
      .button("Saluta", action=saluto)\
      .button("Esci", action=esci)\
      .render()
```


## Licenza

Questo progetto è distribuito sotto licenza Apache 2.0. Vedi il file LICENSE per i dettagli.
## Versioni obsolete, nuove e accettabili

**Ecco le versioni obsolete, nuove e accettabili**. Le obsolete non si devono usare, le nuove sono le ultime, le accettabili versioni passate ma non obsolete.

- 0.1.0 -> Obsoleta
- 0.2.0 -> Obsoleta
- 0.2.1 -> Obsoleta
- 0.2.2 -> Obsoleta
- 0.2.3 -> Obsoleta
- 0.2.4 -> Accettabile
- 0.2.5 -> Accettabile
- 0.2.6 -> Accettabile
- 0.2.7 -> Accettabile
- 0.2.8b -> BETA con errori


