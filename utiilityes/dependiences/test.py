from build_dipendiences import Runners

rn = Runners()

config = (
    rn.run_d()
      .c_classlist_init()
      .c_classlist("Hello!")
      .c_classlist_font("Roboto")
      .debug()   # <-- ECCO IL DEBUG
      .build()
)

