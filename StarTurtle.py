import turtle as t

# Setup
s = t.getscreen()
s.bgcolor("black")
t.left(90)
t.speed(0)
length = 10
angle = 144
t.fillcolor("blue")

# Movement Functions
def t_right(angle):
    t.pencolor("blue")
    t.right(angle)
    t.dot(3)

def t_forward(length):
    t.pencolor("red")
    t.forward(length)

def t_left(angle):
    t.pencolor('green')
    t.left(angle)
    t.dot(3)

def t_backward(length):
    t.pencolor('purple')
    t.backward(length)

# Main loop to draw and fill shapes
while True:
    t.begin_fill()  # Start filling before the shape
    for _ in range(5):  # Draw a 5-pointed star
        t_forward(length)
        t_right(angle)
    t.end_fill()  # End fill after the shape
    length += 10  # Gradually increase the length
    t.left(36)  # Rotate slightly for the next star