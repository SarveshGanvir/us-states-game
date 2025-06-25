import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coordinates(x,y):
#     print(x,y)# this function takes X & Y as input, and then it prints those out
# turtle.onscreenclick(get_mouse_click_coordinates)#onscreenclick() is an event listener so it's going to listen when the
#                                                 # mouse clicks, and then it's going to call our function

data = pd.read_csv("50_states.csv")
guessed_states = []
# print(data["state"].values)
# print(Guess)

def st_turtle(X, Y,name):
    st = turtle.Turtle()
    st.hideturtle()
    st.penup()
    st.goto(X, Y)
    st.write(name, align="center", font=("Arial", 8, "normal"))

missing_states = data.state.to_list()

def working():
    while len(guessed_states) < 50:
        guess = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                 prompt="What's another state's name?").title()
        if guess == "Exit":
            # Convert the list to a DataFrame
            df = pd.DataFrame(missing_states, columns=["State"])

            # Save to CSV
            df.to_csv("missing_states.csv", index=False)
            break

        if guess in data["state"].values and guess not in guessed_states:
            guessed_states.append(guess)
            var = data[data.state == guess]
            X = var.x.item()
            Y = var.y.item()
            st_turtle(X, Y, guess)
            missing_states.remove(guess)

working()





turtle.mainloop()# opposite of exitonclick
