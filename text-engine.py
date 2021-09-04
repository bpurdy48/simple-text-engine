import pgzrun

WIDTH = 1000
HEIGHT = 800
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

message = "Hello. Press to space continue"
count = 0
color = "black"
color2 = "white"

text_box = Rect(0, 0, WIDTH, 260)
text_box.move_ip(0, HEIGHT - 260)

def draw():
    screen.fill("sky blue")
    screen.draw.filled_rect(text_box, color)
    screen.draw.textbox(str(message), text_box, color=color2 )

def on_key_up(key):
    global count, message, color, color2
    if key == keys.SPACE:
        count = count + 1
    if count == 1:
        message = "I've been waiting for you"

    if count == 2:
        message = "This is a basic text engine made in Pygame Zero by Ben."

    if count == 3:
        message = "It works surprisingly well!"
    if count == 4:
        message = "undefined"
    if count == 5:
        message = "That wasn't a real glitch"
    if count == 6:
        message = "That was a joke"
    if count == 7:
        color = "sky blue"
        color2 = "sky blue"
    if count == 8:
        color = "black"
        color2 = "white"
        message = "I'm back!"
    if count == 9:
        message = "Why don't you say anything"
pgzrun.go()