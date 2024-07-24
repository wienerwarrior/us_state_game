import turtle
import pandas

data = pandas.read_csv("50_states.csv")

# Turtle Setup
screen = turtle.Screen()
screen.title("US States Game")
screen.setup(width=725, height=500)

screen.setworldcoordinates(-362.5, -245.5, 362.5, 245.5)

img = "blank_states_img.gif"
screen.bgpic(img)

# Game State Setup
game_state = True
score_counter = 0
turtle.hideturtle()

def user_input(score_counter):
    user_answer = screen.textinput(f"Guess the State {score_counter}/50", "Name a State").title()
    return user_answer
def do_turtle_stuff(x, y):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.write(f"{state_name}")

while game_state & score_counter < 50:
    answer = user_input(score_counter)
    for name in data.state:
        if answer == name:
            score_counter += 1
            state_data = (data[data['state'] == answer])
            state_name = state_data.state.iloc[0]
            x_coor = state_data.x.iloc[0]
            y_coor = state_data.y.iloc[0]
            do_turtle_stuff(x_coor, y_coor)

    else:
        print("Try Again")


    def get_click(x, y):
        print(x, y)


    on_click = screen.onscreenclick(get_click)

    print(f"Name:{state_name}, X: {x_coor}, Y: {y_coor}")
    print(on_click)
turtle.mainloop()
