print("A module uses dependencies")

class Runners:

    def __init__(self):
        # Stato interno per validazione
        self.state = {
            "run_d": False,
            "classlist_init": False,
            "font_set": False
        }

        # Dati configurati
        self.font = None
        self.content_list = []
        self.log = []  # Log interno delle operazioni

    # -------------------------
    # Funzione interna di validazione
    # -------------------------
    def _require(self, key, message):
        if not self.state[key]:
            raise RuntimeError(message)

    # -------------------------
    # Metodi Fluent API
    # -------------------------

    def run_d(self):
        self.state["run_d"] = True
        self.log.append("run_d() eseguito")
        return self
    
    def c_classlist_init(self):
        self._require("run_d", "Errore: devi chiamare run_d() prima di c_classlist_init().")
        self.state["classlist_init"] = True
        self.log.append("c_classlist_init() eseguito")
        return self

    def c_classlist_font(self, font):
        self._require("classlist_init", "Errore: devi chiamare c_classlist_init() prima di impostare il font.")

        font_lib = {
            'Roboto':'FONT.Roboto',
            'SesfsMainia':'FONT.SesfsMainia',
            'Microsoft Fake Yahei':'FONT.Microsoft+Fake+Yahei',
            'Source':'FONT.Source'
        }

        if font not in font_lib:
            raise ValueError(
                f"Font '{font}' non esiste. Usa: {', '.join(font_lib.keys())}"
            )

        self.font = font_lib[font]
        self.state["font_set"] = True
        self.log.append(f"Font impostato: {font}")
        return self
    
    def c_classlist(self, content):
        self._require("classlist_init", "Errore: devi chiamare c_classlist_init() prima di c_classlist().")
        print(content)
        self.content_list.append(content)
        self.log.append(f"c_classlist() → '{content}'")
        return self

    # -------------------------
    # Metodo finale opzionale
    # -------------------------
    def build(self):
        self.log.append("build() chiamato")
        return {
            "initialized": self.state["classlist_init"],
            "font": self.font,
            "content": self.content_list
        }

    # -------------------------
    # Metodo DEBUG
    # -------------------------
    def debug(self):
        # Codici ANSI
        RESET = "\033[0m"
        BOLD = "\033[1m"

        CYAN = "\033[36m"
        GREEN = "\033[32m"
        YELLOW = "\033[33m"
        MAGENTA = "\033[35m"

        print(f"\n{MAGENTA}{BOLD}=== DEBUG Runners ==={RESET}")

        # Stato interno
        print(f"{CYAN}Stato interno:{RESET}")
        for k, v in self.state.items():
            color = GREEN if v else YELLOW
            print(f"  {color}{k}: {v}{RESET}")

        # Font
        print(f"\n{CYAN}Font selezionato:{RESET}")
        font_display = self.font if self.font else "Nessun font impostato"
        print(f"  {YELLOW}{font_display}{RESET}")

        # Contenuti
        print(f"\n{CYAN}Contenuti aggiunti:{RESET}")
        if self.content_list:
            for c in self.content_list:
                print(f"  - {YELLOW}{c}{RESET}")
        else:
            print(f"  {YELLOW}(vuoto){RESET}")

        # Log
        print(f"\n{CYAN}Log operazioni:{RESET}")
        if self.log:
            for entry in self.log:
                print(f"  • {GREEN}{entry}{RESET}")
        else:
            print(f"  {YELLOW}(nessuna operazione registrata){RESET}")

        print(f"{MAGENTA}{BOLD}====================={RESET}\n")
        return self

