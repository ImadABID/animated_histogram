from manimlib import *

#HEGHT = 7
#WIDTH = 14.2

def random_uniform(nbr_choice):
    Choices = []
    return Choices

class Hist(Scene):
    CONFIG = {
        "camera_config": {
            "background_opacity": 0,
        },
    }
    
    def construct(self):
        #params
        line_height_from_bottom = 1

        #objects
        line = Line(7.1*LEFT+(4-line_height_from_bottom)*DOWN,7.1*RIGHT+(4-line_height_from_bottom)*DOWN)

        #annimation
        self.play(ShowCreation(line))
        self.wait()