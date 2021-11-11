import turtle


class Pen:
    def __init__(self, _x=0, _y=260):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(_x, _y)
        self.pen.color("white")
        self.font = tuple(("Courier",) + (24,) + ("normal",))

    def set_font(self, _str, _i=0):
        f = list(self.font)
        f[_i] = _str
        self.font = tuple(f)

    def write(self, text, _align="center"):
        self.pen.clear()
        self.pen.write(text, align=_align, font=self.font)

