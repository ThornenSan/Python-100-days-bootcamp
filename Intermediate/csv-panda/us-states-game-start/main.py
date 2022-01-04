import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data['state'].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # save all the missing states in csv file
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        # create new turtle object
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # get x and y coordinate of the state
        state_data = data[data.state == answer_state]
        # write state name on map
        t.goto(x=int(state_data.x), y=int(state_data.y))
        t.write(state_data.state.item(), font=('Arial', 13, 'normal'))
