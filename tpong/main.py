
if __name__ != '__main__':
    from .obj import *
    from .pen import *
    from .const import *
else:
    from obj import *
    from pen import *
    from const import *


def game_loop():
    window = turtle.Screen()
    window.title("Pong 2021 by the Random Developer")
    window.bgcolor("black")
    window.setup(width=SCR_WIDTH, height=SCR_HEIGHT)
    window.tracer(0)

    scoreboard = Pen()
    paddle_a = PongPaddle("Player A", -350, 0)
    paddle_b = PongPaddle("Player B", 350, 0)
    ball = PongBall()

    window.listen()
    window.onkeypress(paddle_a.object_up, "w")
    window.onkeypress(paddle_a.object_down, "s")
    window.onkeypress(paddle_a.object_up, "W")
    window.onkeypress(paddle_a.object_down, "S")
    window.onkeypress(paddle_b.object_up, "Up")
    window.onkeypress(paddle_b.object_down, "Down")

    scoreboard.write(f"{paddle_a.name}: {paddle_a.score}  {paddle_b.name}: {paddle_b.score}")

    while True:
        window.update()

        ball.update_pos()

        # check if the ball has reached a left or right border
        # if it has touched a border, determine which paddle scored
        # add to the score and update the screen
        if ball.border_check():
            if ball.is_left():
                paddle_a.score += 1
                scoreboard.write(f"{paddle_a.name}: {paddle_a.score}  {paddle_b.name}: {paddle_b.score}")
                ball.generate_direction()
            else:
                paddle_b.score += 1
                scoreboard.write(f"{paddle_a.name}: {paddle_a.score}  {paddle_b.name}: {paddle_b.score}")
                ball.generate_direction()

        # if the paddle did not hit a left or right border make sure it did not hit a paddle
        # checks based on position
        else:
            if ball.is_left():
                ball.paddle_check(paddle_a)
            else:
                ball.paddle_check(paddle_b)


if __name__ == '__main__':
    game_loop()
