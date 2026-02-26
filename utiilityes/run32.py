from .index import Index

_current_ui = None  # riferimento globale


def _new_ui():
    global _current_ui

    # Se esiste una finestra precedente la chiudiamo
    if _current_ui is not None:
        try:
            _current_ui.close()   # deve esistere in Index
        except:
            pass

    _current_ui = Index()
    return _current_ui


def log(message: str):
    print(message)


def log_inui(message: str):
    ui = _new_ui()
    ui.init.win("Log").size(300, 150)
    ui.run_funct().text(str(message)).render()


def multiple_log_inui(*objects):
    ui = _new_ui()
    ui.init.win("Logs").size(300, 200)
    f = ui.run_funct()
    for obj in objects:
        f.text(str(obj))
    f.render()


