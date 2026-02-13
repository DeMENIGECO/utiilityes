import os
import ctypes
import sdl2
import sdl2.ext
import sdl2.sdlttf as sdlttf


def get_default_font():
    if os.name == "nt":
        path = "C:/Windows/Fonts/arial.ttf"
        if os.path.exists(path):
            return path
    elif os.name == "posix":
        path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        if os.path.exists(path):
            return path
    return None


class Init:
    def __init__(self):
        self.window_title = "Untitled"
        self.window_width = 400
        self.window_height = 300

    def win(self, title):
        self.window_title = title
        return self

    def size(self, w, h):
        self.window_width = w
        self.window_height = h
        return self


class GUIElement:
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y


class Button(GUIElement):
    def __init__(self, text, x, y, action=None):
        super().__init__(text, x, y)
        self.action = action
        self.width = 150
        self.height = 40


class Index:
    def __init__(self):
        self.init = Init()
        self.elements = []
        self.next_y = 20

    def run_funct(self):
        return self

    def text(self, text):
        self.elements.append(GUIElement(text, 20, self.next_y))
        self.next_y += 40
        return self

    def button(self, label, action=None):
        self.elements.append(Button(label, 20, self.next_y, action))
        self.next_y += 60
        return self

    def render(self):
        sdl2.ext.init()
        sdlttf.TTF_Init()

        font_path = get_default_font()
        if not font_path:
            raise RuntimeError("Nessun font TTF trovato.")

        font = sdlttf.TTF_OpenFont(font_path.encode(), 20)
        if not font:
            raise RuntimeError("Impossibile aprire il font.")

        window = sdl2.ext.Window(
            self.init.window_title,
            size=(self.init.window_width, self.init.window_height)
        )
        window.show()

        renderer = sdl2.SDL_CreateRenderer(window.window, -1, 0)

        running = True
        while running:
            for event in sdl2.ext.get_events():
                if event.type == sdl2.SDL_QUIT:
                    running = False

                if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
                    mx, my = event.button.x, event.button.y
                    for el in self.elements:
                        if isinstance(el, Button):
                            if (el.x <= mx <= el.x + el.width and
                                el.y <= my <= el.y + el.height):
                                if el.action:
                                    el.action()

            sdl2.SDL_SetRenderDrawColor(renderer, 30, 30, 30, 255)
            sdl2.SDL_RenderClear(renderer)

            for el in self.elements:
                # --- BUTTON ---
                if isinstance(el, Button):
                    sdl2.SDL_SetRenderDrawColor(renderer, 70, 70, 200, 255)
                    rect = sdl2.SDL_Rect(el.x, el.y, el.width, el.height)
                    sdl2.SDL_RenderFillRect(renderer, rect)

                    surface = sdlttf.TTF_RenderText_Blended(
                        font, el.text.encode(), sdl2.SDL_Color(255, 255, 255)
                    )
                    texture = sdl2.SDL_CreateTextureFromSurface(renderer, surface)

                    # FIX: usare puntatori ctypes
                    w = ctypes.c_int()
                    h = ctypes.c_int()
                    sdl2.SDL_QueryTexture(texture, None, None,
                                          ctypes.byref(w), ctypes.byref(h))

                    dst = sdl2.SDL_Rect(el.x + 10, el.y + 10, w.value, h.value)
                    sdl2.SDL_RenderCopy(renderer, texture, None, dst)

                    sdl2.SDL_FreeSurface(surface)
                    sdl2.SDL_DestroyTexture(texture)

                # --- TEXT ---
                else:
                    surface = sdlttf.TTF_RenderText_Blended(
                        font, el.text.encode(), sdl2.SDL_Color(255, 255, 255)
                    )
                    texture = sdl2.SDL_CreateTextureFromSurface(renderer, surface)

                    w = ctypes.c_int()
                    h = ctypes.c_int()
                    sdl2.SDL_QueryTexture(texture, None, None,
                                          ctypes.byref(w), ctypes.byref(h))

                    dst = sdl2.SDL_Rect(el.x, el.y, w.value, h.value)
                    sdl2.SDL_RenderCopy(renderer, texture, None, dst)

                    sdl2.SDL_FreeSurface(surface)
                    sdl2.SDL_DestroyTexture(texture)

            sdl2.SDL_RenderPresent(renderer)

        sdlttf.TTF_Quit()
        sdl2.ext.quit()
        return self
