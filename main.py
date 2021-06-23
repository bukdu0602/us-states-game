import pandas
import turtle
from state_name import assign_state

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


current_score = 0
game_is_on = True
while game_is_on:
    data = pandas.read_csv("50_states.csv")
    state_list = data["state"].tolist()
    how_many = len(state_list)
    print(how_many)
    if current_score > 0:
        answer_state = screen.textinput(title=f"{current_score}/50", prompt="What's another state's name?")
    else:
        answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    answer_state = answer_state.capitalize()

    a = data[data["state"] == answer_state]
    to_dict = a.to_dict()
    x_y_key = list(to_dict["state"].keys())
    current_score += 1




    assigning = assign_state()
    assigning.assign((to_dict["x"][x_y_key[0]], to_dict["y"][x_y_key[0]]), f"{to_dict['state'][x_y_key[0]]}")


screen.exitonclick()
