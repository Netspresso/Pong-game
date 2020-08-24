'''Simple Pong game in Python 3'''

import turtle

wn = turtle.Screen()
wn.title("Pong by Marszal")
wn.bgcolor("black")
wnHeight = 600
wnWidth = 800
wn.setup(width=wnWidth, height=wnHeight)
wn.tracer(0)

# Score
scoreA = 0
scoreB = 0

#Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-wnWidth / 2 + 40, 0)

#Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(wnWidth / 2 - 50, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A:0  Player B:0",
          align='center',
          font=('Courier', 24, 'normal'))


#Functions
def paddleAUp():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)


def paddleBUp():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)


def paddleADown():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)


def paddleBDown():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddleAUp, "w")
wn.onkeypress(paddleBUp, "Up")
wn.onkeypress(paddleADown, "s")
wn.onkeypress(paddleBDown, "Down")

#Main game loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > wnHeight / 2 - 10:
        ball.sety(wnHeight / 2 - 10)
        ball.dy *= -1

    if ball.ycor() < -wnHeight / 2 + 10:
        ball.sety(-wnHeight / 2 + 10)
        ball.dy *= -1

    if ball.xcor() > wnWidth / 2:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(scoreA, scoreB),
                  align='center',
                  font=('Courier', 24, 'normal'))

    if ball.xcor() < -wnWidth / 2:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(scoreA, scoreB),
                  align='center',
                  font=('Courier', 24, 'normal'))

    # paddle and ball collisions
    if ball.xcor() > wnWidth / 2 - 60 and ball.xcor() < wnWidth / 2 - 50 and (
            ball.ycor() < paddleB.ycor() + 40
            and ball.ycor() > paddleB.ycor() - 40):
        ball.dx *= -1

    if ball.xcor() < -wnWidth / 2 + 60 and ball.xcor(
    ) < -wnWidth / 2 + 50 and (ball.ycor() < paddleA.ycor() + 40
                               and ball.ycor() > paddleA.ycor() - 40):
        ball.dx *= -1