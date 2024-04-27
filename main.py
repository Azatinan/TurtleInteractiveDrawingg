import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def rotate_angle_right():
    turtle_instance.right(90)

def rotate_angle_left():
    turtle_instance.left(90)

def clear_screen():
    turtle_instance.clear()

def turtle_return_home():
    turtle_instance.home()

def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()


drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="space")
drawing_board.onkey(fun=rotate_angle_right, key="d")
drawing_board.onkey(fun=rotate_angle_left, key="a")
drawing_board.onkey(fun=clear_screen, key="k")
drawing_board.onkey(fun=turtle_return_home, key="l")
drawing_board.onkey(fun=turtle_pen_up, key="m")
drawing_board.onkey(fun=turtle_pen_down, key="n")


turtle.done()
