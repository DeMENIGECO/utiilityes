from .index import Index as ind

def log(message):
    print(message)

def log_inui(message):
    ui = ind()
    ui.run_funct()\
      .text(message)\
      .render()

def multiple_log(*objects):
    for obj in objects:
        print(obj)

def multiple_log_inui(*objects):
    ui = ind()
    f = ui.run_funct()
    for obj in objects:
        f.text(str(obj))
    f.render()

def example():
    def saluto():
        print("Hai cliccato SALUTA!")

    def esci():
        print("Esco...")
        raise SystemExit

    ui = ind()

    ui.init.win("Example")\
      .size(600, 400)

    ui.run_funct()\
      .text("Benvenuto nella GUI SDL2!")\
      .button("Saluta", action=saluto)\
      .button("Esci", action=esci)\
      .render()
