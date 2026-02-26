from .index import Index
from .run32 import log
from .run32 import _current_ui  # importiamo il riferimento
from .run32 import _new_ui      # importiamo la funzione


def error(message: str):
    ui = _new_ui()
    ui.init.win("Errore").size(300, 150)
    ui.run_funct().text(str(message)).render()


def info(message: str):
    ui = _new_ui()
    ui.init.win("Informazione").size(300, 150)
    ui.run_funct().text(str(message)).render()


def warning(message: str):
    ui = _new_ui()
    ui.init.win("Attenzione").size(300, 150)
    ui.run_funct().text(str(message)).render()


def confirm(message: str):
    ui = _new_ui()
    ui.init.win("Conferma").size(300, 150)

    def si():
        log("Confermato")

    def no():
        raise SystemExit

    ui.run_funct()\
      .text(str(message))\
      .button("Continua", action=si)\
      .button("Annulla", action=no)\
      .render()



