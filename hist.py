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
        self.nbr_experience = 10
        self.choices = random_uniform(len(self.choices_logo_path), self.nbr_experience)
        print(self.choices)

        #inter params
        Param = {
            "line_height_from_bottom" : 1,
            "logo_size" : 0.8,
            "segment_width" : 1,
            "segment_d_height" : 0.2
        }

        #objects
        line_edge_x = Param["segment_width"]*len(self.choices_logo_path)/2
        line = Line(line_edge_x*LEFT+(4-Param["line_height_from_bottom"])*DOWN,line_edge_x*RIGHT+(4-Param["line_height_from_bottom"])*DOWN)

        #inter data
        self.histogram = numpy.zeros((len(self.choices_logo_path),), dtype=int)

        #annimation
        self.play(Create(line))
        self.wait()

        for i in range(self.nbr_experience):
            print(i)
            self.play_experience(i, Param, line_edge_x)

    def play_experience(self, i, Param, line_edge_x):

        logo = ImageMobject(self.choices_logo_path[self.choices[i]])
        logo.scale(Param["logo_size"]/logo.height)
        position_logo = (4-0.7)*UP
        logo.shift(position_logo)

        seg = Rectangle(height = Param["segment_d_height"], width = Param["segment_width"], fill_color=WHITE, fill_opacity=1, stroke_opacity=0)
        position_seg = (-4 + Param["line_height_from_bottom"] + Param["segment_d_height"] * self.histogram[self.choices[i]] + 0.5 * Param["segment_d_height"] ) * UP + (-line_edge_x + Param["segment_width"] * self.choices[i] + 0.5 * Param["segment_width"] )*RIGHT
        seg.shift(position_seg)

        self.play(FadeIn(logo), run_time=1)
        self.play(FadeOutAndShift(logo, position_seg-position_logo), FadeInFrom(seg, position_logo), run_time=1)
        self.wait()
        self.histogram[self.choices[i]] += 1