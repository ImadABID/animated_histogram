from manim import *
import numpy

#config.background_color = GREEN
#config.background_opacity = 0

#HEGHT = 7
#WIDTH = 14.2

def random_uniform(nbr_choice, nbr_exp):
    Choices = numpy.random.randint(nbr_choice, size=nbr_exp)
    return Choices

class Hist(Scene):
    
    def construct(self):
        #your annimation param
        self.choices_logo_path=["logos/0.png","logos/1.png"]
        self.choices = random_uniform(len(self.choices_logo_path), 10)

        #inter params

        line_height_from_bottom = 1
        logo_size = 0.8
        segment_width = 1
        segment_d_height = 0.2
        
        #objects
        line_edge_x = segment_width*len(self.choices_logo_path)/2
        line = Line(line_edge_x*LEFT+(4-line_height_from_bottom)*DOWN,line_edge_x*RIGHT+(4-line_height_from_bottom)*DOWN)

        #annimation
        self.play(Create(line))
        self.wait()

        self.play_experience(0)

    def play_experience(self, i):
        logo = ImageMobject(self.choices_logo_path[self.choices[i]])
        self.play(FadeIn(logo), run_time=1)
        self.wait()