from browser import document, html, window

elements = []

def add(obj):
    document <= obj.el

def add_key_down_handler(func):
    def handler(ev):
        class Event:
            def __init__(self, ev):
                self.key = ev.key
        func(Event(ev))
    document.bind("keydown", handler)

class Rectangle:
    def __init__(self, w, h):
        self.el = html.DIV()
        self.el.style.width = str(w) + "px"
        self.el.style.height = str(h) + "px"
        self.el.style.position = "absolute"
        self.el.style.border = "2px solid #3a3a3c"

    def set_position(self, x, y):
        self.el.style.left = str(x) + "px"
        self.el.style.top = str(y) + "px"

    def set_color(self, color):
        self.el.style.backgroundColor = color

    def set_border_color(self, color):
        self.el.style.borderColor = color

    def set_border_width(self, width):
        self.el.style.borderWidth = str(width) + "px"

class Text:
    def __init__(self, text):
        self.el = html.DIV(text)
        self.el.style.position = "absolute"

    def set_text(self, text):
        self.el.text = text

    def set_position(self, x, y):
        self.el.style.left = str(x) + "px"
        self.el.style.top = str(y) + "px"

    def set_color(self, color):
        self.el.style.color = color

    def set_font(self, font):
        self.el.style.font = font

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.el = html.HR()
        self.el.style.position = "absolute"
        self.el.style.left = str(x1) + "px"
        self.el.style.top = str(y1) + "px"
        self.el.style.width = str(x2-x1) + "px"

    def set_color(self, color):
        self.el.style.borderColor = color
