class Screen():

    def __init__(self, weight, high):
        self.weight = weight
        self.high = high

    def show(self, image):
        print("Show:", image)

    def get_size(self):
        print("weight:", self.weight, ". high:", self.high)


usual_screen = Screen(100, 100)
usual_screen.show("Cartoon")
usual_screen.get_size()

class Mobile(Screen):
    def __init__(self, weight, high):
        super().__init__(weight, high)

    def application(self, inst, telega):
        print("Application:", inst, telega)

    def model(self, model):
        print("Model", model)

screen = Mobile(50, 50)
screen.application("INSTAGRAM", "TELEGRAM")
screen.model("Iphone")