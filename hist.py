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
        #your annimation param
        nbr_choice = 2

        #inter params

        line_height_from_bottom = 1
        segment_width = 1
        segment_d_height = 0.2
        
        #objects
        line_edge_x = segment_width*nbr_choice/2
        line = Line(line_edge_x*LEFT+(4-line_height_from_bottom)*DOWN,line_edge_x*RIGHT+(4-line_height_from_bottom)*DOWN)

        #annimation
        self.play(ShowCreation(line))
        self.wait()