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


def user_input(score):
    user_answer = screen.textinput(f"Guess the State {score}/50",
                                   "Name a State").title()
    return user_answer


def do_turtle_stuff(x, y):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.write(f"{state_name}")


def make_data_frame(state):
    need_to_learn = {'States To Learn': [state]}
    data_frame = pandas.DataFrame(need_to_learn)
    data_frame.to_csv("to_learn.csv", index=False)


all_states = data.state.to_list()
guessed_states = []
while game_state and score_counter < 50:
    temp_list = []
    for name in all_states:
        if name not in guessed_states:
            temp_list.append(name)
    print(len(temp_list))
    make_data_frame(temp_list)
    answer = user_input(score_counter)
    if answer == 'Exit':
        break
    for name in data.state:
        if answer == name:
            guessed_states.append(answer)
            score_counter += 1
            state_data = (data[data['state'] == answer])
            state_name = state_data.state.iloc[0]
            x_coor = state_data.x.iloc[0]
            y_coor = state_data.y.iloc[0]
            do_turtle_stuff(x_coor, y_coor)

    # print(f"Name:{state_name}, X: {x_coor}, Y: {y_coor}")

turtle.mainloop()



