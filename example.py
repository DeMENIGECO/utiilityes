from utiilityes import Index as ind

if __name__ == "__main__":
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
