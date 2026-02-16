from .index import Index

def log(message: str):
    print(message)

def log_inui(message: str):
    ui = Index()
    ui.init.win("Log").size(300, 150)
    ui.run_funct().text(str(message)).render()

def multiple_log_inui(*objects):
    ui = Index()
    ui.init.win("Logs").size(300, 200)
    f = ui.run_funct()
    for obj in objects:
        f.text(str(obj))
    f.render()


