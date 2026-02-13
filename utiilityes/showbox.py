from .index import Index as ind
from .run32 import log

def error(message):
    ui = ind()
    ui.init.win("Errore")\
      .size(300, 150)

    ui.run_funct()\
      .text(message)\
      .render()

def info(message):
    ui = ind()
    ui.init.win("Informazione")\
      .size(300, 150)

    ui.run_funct()\
      .text(message)\
      .render()

def warning(message):
    ui = ind()
    ui.init.win("Attenzione!")\
      .size(300, 150)

    ui.run_funct()\
      .text(message)\
      .render()

def confirm(message):
    ui = ind()
    ui.init.win("Conferma?")\
      .size(300, 150)

    def si():
        log("Accettato!")

    def no():
        raise SystemExit

    ui.run_funct()\
      .text(message)\
      .button("Continua", action=si)\
      .button("Annulla", action=no)\
      .render()


