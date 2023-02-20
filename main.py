from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle

import time

from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

scoreboard = Scoreboard()
#
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 390:
        scoreboard.increase_score_p1()
        ball.reset()

    if ball.xcor() < -390:
        scoreboard.increase_score_p2()
        ball.reset()

            # r_paddle point
    if scoreboard.score_p1 == 5 or scoreboard.score_p2 == 5:
        scoreboard.game_over()
        game_is_on = False



#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     "press enter to begin game""ball moves"

screen.exitonclick()