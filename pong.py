import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # for faster game without updating

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle() # capital Turtle is class name
paddle_a.speed(0) # speed of animation, not speed for moving
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # 5*20 1*20 
paddle_a.penup() # this game is without lines
paddle_a.goto(-350, 0) # position of paddle_a at the start of the game

# Paddle B
paddle_b = turtle.Turtle() # capital Turtle is class name
paddle_b.speed(0) # speed of animation, not speed for moving
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # 5*20 1*20 
paddle_b.penup() # this game is without lines
paddle_b.goto(350, 0) # position of paddle_a at the start of the game

# Ball
ball = turtle.Turtle() # capital Turtle is class name
ball.speed(0) # speed of animation, not speed for moving
ball.shape("square")
ball.color("white")
ball.penup() # this game is without lines
ball.goto(0, 0) # position of paddle_a at the start of the game
ball.dx = 0.25 # moves by 0.25 pixels
ball.dy = -0.25 # when x is positive then moves 0.25 pixels right, for y ball moves 0.25 pixels up 

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() # not visible on screen
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor() # from turtle module and returns y coordinate
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() 
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() # from turtle module and returns y coordinate
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() 
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen() # listen for keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # reverse the direction of the ball
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) # for playing sound in the background

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 # reverse the direction of the ball
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0) # ball in the center
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0) # ball in the center
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

