from manim import *
import numpy

#config.background_color = GREEN
#config.background_opacity = 0

#HEGHT = 7
#WIDTH = 14.2

def random_uniform(nbr_choice, nbr_exp):
    Choices = numpy.random.randint(nbr_choice, size=nbr_exp)
    return Choices

def random_gauss(nbr_choice, sigma, nbr_exp):
    randGauss = numpy.random.normal(loc=nbr_choice/2, scale=sigma, size=nbr_exp)
    Choices = []
    for val in randGauss:
        Choices += [int(val)]
    
    return Choices

class Hist(Scene):
    
    def construct(self):
        #your annimation param
        self.choices_logo_path=["logos/0.png","logos/1.png","logos/2.png","logos/3.png","logos/4.png"]
        self.nbr_experience = 20
        self.anim_runtime = 0.2
        #self.choices = random_uniform(len(self.choices_logo_path), self.nbr_experience)
        self.choices = random_gauss(len(self.choices_logo_path), 1, self.nbr_experience)

        #inter params
        Param = {
            "line_height_from_bottom" : 1,
            "logo_size" : 0.8,
            "segment_width" : 1,
            "segment_d_height" : 0.1
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

        seg = Rectangle(height = Param["segment_d_height"], width = Param["segment_width"], fill_color=WHITE, fill_opacity=1, stroke_opacity=0.2, stroke_color = RED)
        position_seg = (-4 + Param["line_height_from_bottom"] + Param["segment_d_height"] * self.histogram[self.choices[i]] + 0.5 * Param["segment_d_height"] ) * UP + (-line_edge_x + Param["segment_width"] * self.choices[i] + 0.5 * Param["segment_width"] )*RIGHT
        seg.shift(position_seg)

        self.play(FadeIn(logo), run_time=self.anim_runtime)

        if(self.histogram[self.choices[i]] == 0):
            logo_x = ImageMobject(self.choices_logo_path[self.choices[i]])
            logo_x.scale(Param["logo_size"]/logo_x.height)
            logo_x.shift((4-0.5*Param["logo_size"]-0.1)*DOWN + (-line_edge_x + Param["segment_width"] * self.choices[i] + 0.5 * Param["segment_width"] )*RIGHT)
            self.play(FadeOutAndShift(logo, position_seg-position_logo), FadeInFrom(seg, position_logo), FadeIn(logo_x), run_time=self.anim_runtime)
        else:
            self.play(FadeOutAndShift(logo, position_seg-position_logo), FadeInFrom(seg, position_logo), run_time=self.anim_runtime)

        self.histogram[self.choices[i]] += 1