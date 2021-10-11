from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Brick
from scoreboard import Scoreboard
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Breakout!")
screen.tracer(0)


def lay_bricks():
    bricks = []
    xcor = -380
    ycor = 30
    for i in range(11):
        new_brick = Brick((xcor, ycor), "yellow", 1)
        bricks.append(new_brick)
        xcor += 75
    xcor = -380
    ycor = 60
    for i in range(11):
        new_brick = Brick((xcor, ycor), "yellow", 1)
        bricks.append(new_brick)
        xcor += 75
    xcor = -380
    ycor = 90
    for i in range(11):
        new_brick = Brick((xcor, ycor), "green", 3)
        bricks.append(new_brick)
        xcor += 75
    xcor = -380
    ycor = 120
    for i in range(11):
        new_brick = Brick((xcor, ycor), "green", 3)
        bricks.append(new_brick)
        xcor += 75
    xcor = -380
    ycor = 150
    for i in range(11):
        new_brick = Brick((xcor, ycor), "orange", 5)
        bricks.append(new_brick)
        xcor += 75
    xcor = -380
    ycor = 180
    for i in range(11):
        new_brick = Brick((xcor, ycor), "orange", 5)
        bricks.append(new_brick)
        xcor += 75
    xcor = -380
    ycor = 210
    for i in range(11):
        new_brick = Brick((xcor, ycor), "red", 7)
        bricks.append(new_brick)
        xcor += 75
    xcor = -380
    ycor = 240
    for i in range(11):
        new_brick = Brick((xcor, ycor), "red", 7)
        bricks.append(new_brick)
        xcor += 75
    print(len(bricks))
    return bricks


paddle = Paddle((0, -250))
ball = Ball()
bricks = lay_bricks()
scoreboard = Scoreboard()

screen.listen()
screen.getcanvas().bind('<Left>', paddle.move_left)
screen.getcanvas().bind('<Right>', paddle.move_right)
screen.getcanvas().winfo_pointerx()
screen.getcanvas().bind('<Motion>', paddle.move_cursor)


game_is_on = True
sleep_amount = 0.05
bricks_collected = 0
first_time = True
four_bricks = False
twelve_bricks = False
orange_hit = False
red_hit = False

while game_is_on and scoreboard.lives > 0:

    time.sleep(sleep_amount)
    screen.update()
    ball.move()

    # Collision with Top Wall
    if ball.ycor() > 280:
        if first_time:
            paddle.size_half()
            first_time = False
        ball.bounce_y()

    # Collision with Left and Right walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Collision with Paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -230:
        ball.bounce_y()

    # Collision with Ground
    if ball.ycor() < -300:
        scoreboard.lose_life()
        ball.restart()
        paddle.restart()
        time.sleep(2)

    # Collision with Brick
    for brick in bricks:
        if ball.distance(brick) < 30:
            ball.bounce_y()
            points = brick.get_value()
            scoreboard.score_points(points)
            if not orange_hit and points == 5:
                sleep_amount *= .8
                print('got faster')
                orange_hit = True
            if not red_hit and points == 7:
                sleep_amount *= .8
                print('got faster')
                red_hit = True
            brick.destroy()
            bricks_collected += 1
            print(f'bricks collected: {bricks_collected}')

    if not four_bricks and bricks_collected == 4:
        four_bricks = True
        sleep_amount *= .8
        print('got faster')

    if not twelve_bricks and bricks_collected == 12:
        twelve_bricks = True
        sleep_amount *= .8
        print('got faster')

    if bricks_collected == 88:
        scoreboard.win()

for brick in bricks:
    brick.destroy()
    screen.update()
    time.sleep(0.001)
scoreboard.lose()

screen.exitonclick()
