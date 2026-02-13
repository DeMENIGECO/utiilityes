from .index import Index as ind
from .run32 import log

def error(message):
    ind.init.win("Errore")\
        .size(150, 300)
    
    ind.run_funct()\
        .text(message)\
        .render()
    
def info(message):
    ind.init.win("Informazione")\
        .size(150, 300)
    
    ind.run_funct()\
        .text(message)\
        .render()
    
def warning(message):
    ind.init.win("Attenzione!")\
        .size(150, 300)
    
    ind.run_funct()\
        .text(message)\
        .render()
        

def confirm(message):
    ind.init.win("Conferma?")\
        .size(150, 300)
    
    def si():
        log("Accetato!")

    def no():
        raise SystemExit
    
    ind.run_funct()\
        .text(message)\
        .button("Continua", action=si)\
        .button("Annulla", action=no)\
        .render()
    
