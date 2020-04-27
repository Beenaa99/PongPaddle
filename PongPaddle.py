# PongPaddle Game in Python 3
# reference @TokyoEdTech
# Not using PyGame 

import turtle 

win = turtle.Screen()
win.title("PongPaddle by @Beenaa") 
win.bgcolor("black")
win.setup(width=1200, height=600)
win.tracer(0) #stops auto screen updating

score_one = 0
score_two = 0

#Paddle left
paddle_left = turtle.Turtle()
paddle_left.speed(0) # max speed
paddle_left.shape("square")
paddle_left.color("gold")
paddle_left.shapesize(stretch_wid=8, stretch_len= 1)
#paddle_left.penup()
paddle_left.goto(-550,0)

#Paddle Right
paddle_right = turtle.Turtle()
paddle_right.speed(0) # max speed
paddle_right.shape("square")
paddle_right.color("gold")
paddle_right.shapesize(stretch_wid=8, stretch_len= 1)
#paddle_right.penup()
paddle_right.goto(550,0)

#Ball
ball = turtle.Turtle()
ball.speed(0) # max speed
ball.shape("circle")
ball.color("royal blue")
ball.penup()
ball.goto(0,0)
ball.dx, ball.dy = 0.3, 0.3

#Score
pen = turtle.Turtle()
pen.speed(0)
pen.color("goldenrod")
pen.penup()
pen.goto(0, 240)
pen.write("Player One: 0  Player Two: 0", align="center", font=("Courier", 24, "normal"))


#Playing:
def paddle_left_up():
    y_left = paddle_left.ycor()
    y_left += 30
    paddle_left.sety(y_left)

def paddle_left_down():
    y_left = paddle_left.ycor()
    y_left -= 30
    paddle_left.sety(y_left)

def paddle_right_up():
    y_right = paddle_right.ycor()
    y_right += 30
    paddle_right.sety(y_right)

def paddle_right_down():
    y_right = paddle_right.ycor()
    y_right -= 30
    paddle_right.sety(y_right)

win.listen()
win.onkeypress(paddle_left_up, "7")
win.onkeypress(paddle_left_down, "1")
win.onkeypress(paddle_right_up, "9")
win.onkeypress(paddle_right_down, "3")

#Main
while True:
    win.update()

    #border:
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 590:
        ball.goto(0, 0)
        ball.dx *= -1
        score_one += 1
        pen.clear()
        pen.write("Player One: {}  Player Two: {}".format(score_one, score_two), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -590:
        ball.goto(0, 0)
        ball.dx *= -1
        score_two += 1
        pen.clear()
        pen.write("Player One: {}  Player Two: {}".format(score_one, score_two), align="center", font=("Courier", 24, "normal"))
        

    #Ball movements
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


# Paddle and ball collisions

    if (ball.xcor() > 540 and ball.xcor() < 550) and (ball.ycor() < paddle_right.ycor() + 70 and ball.ycor() > paddle_right.ycor() - 70):
        ball.setx(540)
        ball.dx *= -1

    if (ball.xcor() < -540 and ball.xcor() > -550) and (ball.ycor() < paddle_left.ycor() + 70 and ball.ycor() > paddle_left.ycor() - 70):
        ball.setx(-540)
        ball.dx *= -1



   