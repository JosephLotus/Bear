from turtle import Turtle
FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.penup()
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-10, 260)
        self.write(f"Help Bear cross the road! Level: {self.level}", move=True, align=ALIGNMENT, font=FONT)

    def game_over_text(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=True, align=ALIGNMENT,
                   font=FONT)

    def player_scores(self):
        self.level += 1
        self.refresh()
