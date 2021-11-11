import turtle
import random


class PongObj:

    def __init__(self, _x=0, _y=0, _wid=1, _len=1) -> None:
        # initial position
        self.position = [0.0, 0.0]
        self.position[0] = _x
        self.position[1] = _y

        # drawn object
        self.shape = turtle.Turtle()
        self.shape.speed(0)
        self.shape.shape("square")
        self.shape.color("white")
        self.shape.shapesize(stretch_wid=_wid, stretch_len=_len)
        self.shape.penup()
        self.set_location(_x, _y)  # set object location

    def set_location(self, _x, _y):
        self.position[0] = _x
        self.position[1] = _y
        self.shape.goto(self.position[0], self.position[1])

    def update_coordinates(self):
        self.position[0] = self.shape.xcor()
        self.position[1] = self.shape.ycor()


class PongBall(PongObj):
    def __init__(self, _x=0, _y=0, _wid=1, _len=1, _dir=0.4):
        super().__init__(_x, _y, _wid, _len)
        self.max_direction = _dir
        self.direction = [0.0, 0.0]
        self.direction[0] = self.direction[1] = _dir
        random.seed()

    def border_check(self, max_height=290, max_width=380):
        """
        Check ball object with border of window
        """
        self.update_coordinates()
        # Y Coordinates
        if self.position[1] > max_height:
            self.set_location(self.position[0], max_height)
            self.direction[1] *= -1
            return False
        if self.position[1] < -1 * max_height:
            self.set_location(self.position[0], -1 * max_height)
            self.direction[1] *= -1
            return False
        # X Coordinates
        if self.position[0] > max_width:
            self.set_location(0, 0)
            self.direction[0] *= -1
            return True
        if self.position[0] < -1 * max_width:
            self.set_location(0, 0)
            self.direction[0] *= -1
            return True

    def paddle_check(self, _obj: PongObj):
        """
        Check if paddles are colliding with pong ball
        """
        x_mods = x_mod = 10
        if not self.is_left():  # if moving in the right direction
            x_mod = -10
        y_mod = 40

        # check if the ball object is touching the pong object
        if _obj.position[0] - x_mods < self.position[0] < _obj.position[0] and (
                _obj.position[1] + y_mod > self.position[1] > _obj.position[1] - y_mod
        ):
            # if so stop moving the ball and send it in the other direction
            self.set_location(_obj.position[0] + x_mod, self.position[1])
            self.direction[0] *= -1

    def is_left(self):
        return self.direction[0] < 0

    def update_pos(self):
        self.set_location(self.position[0] + self.direction[0],
                          self.position[1] + self.direction[1])

    def generate_direction(self):
        self.direction[1] = random.uniform(0.2, 0.6)
        self.direction[1] *= -1 if bool(random.getrandbits(1)) else self.direction[1]


class PongPaddle(PongObj):
    def __init__(self, name: str, _x=0, _y=0, _wid=5, _len=1):
        super().__init__(_x, _y, _wid, _len)
        self.score = 0
        self.name = name

    def object_up(self):
        self.position[1] += 20
        self.set_location(self.position[0], self.position[1])

    def object_down(self):
        self.position[1] -= 20
        self.set_location(self.position[0], self.position[1])
