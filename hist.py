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

class Segment(Rectangle):
    def ponderation(self, sca, shi_up):
        self.stretch_to_fit_height(self.height*sca)
        self.shift(shi_up * UP)
        return self

class Hist(Scene):
    
    def construct(self):
        #your annimation param
        self.choices_logo_path=["logo/BDA.png","logo/BDE.png","logo/clubee.png","logo/Eirbot.png","logo/enseirb.png", "logo/Vost.png", "logo/zik.png", "logo/eirspace.png"]
        self.nbr_experience = 100
        self.anim_runtime_0 = 0.5
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
        self.hist_objects = len(self.choices_logo_path) * [None]

        #annimation
        self.play(Create(line))
        self.wait()

        for i in range(self.nbr_experience):
            self.play_experience(i, Param, line_edge_x)
        
        self.play_ponderation()

    def play_experience(self, i, Param, line_edge_x):

        run_time = self.anim_runtime_0/(1.1**i)

        logo = ImageMobject(self.choices_logo_path[self.choices[i]])
        logo.scale(Param["logo_size"]/logo.height)
        position_logo = (4-0.7)*UP
        logo.shift(position_logo)

        seg = Segment(height = Param["segment_d_height"], width = Param["segment_width"], fill_color=WHITE, fill_opacity=1, stroke_opacity=0.2, stroke_color = RED)
        position_seg = (-4 + Param["line_height_from_bottom"] + Param["segment_d_height"] * self.histogram[self.choices[i]] + 0.5 * Param["segment_d_height"] ) * UP + (-line_edge_x + Param["segment_width"] * self.choices[i] + 0.5 * Param["segment_width"] )*RIGHT
        seg.shift(position_seg)

        self.play(FadeIn(logo), run_time=run_time)

        if(self.histogram[self.choices[i]] == 0):
            logo_x = ImageMobject(self.choices_logo_path[self.choices[i]])
            logo_x.scale(Param["logo_size"]/logo_x.height)
            logo_x.shift((4-0.5*Param["logo_size"]-0.1)*DOWN + (-line_edge_x + Param["segment_width"] * self.choices[i] + 0.5 * Param["segment_width"] )*RIGHT)
            self.play(FadeOutAndShift(logo, position_seg-position_logo), FadeInFrom(seg, position_logo), FadeIn(logo_x), run_time=run_time)
        else:
            self.play(FadeOutAndShift(logo, position_seg-position_logo), FadeInFrom(seg, position_logo), run_time=run_time)

        self.histogram[self.choices[i]] += 1
        if(self.hist_objects[self.choices[i]] == None):
            self.hist_objects[self.choices[i]] = [seg]
        else :
            self.hist_objects[self.choices[i]] += [seg]

    def play_ponderation(self):
        def h(x):
            return -numpy.log(x)

        txt_scale = 0.2
        txt_up_padding = 0.5


        animations_proba = []
        animations_h = []
        animations_multi = []
        animations = []

        for i in range(len(self.hist_objects)):
            if self.hist_objects[i] == None :
                continue

            p = len(self.hist_objects[i])/self.nbr_experience

            shift_to = self.hist_objects[i][len(self.hist_objects[i])-1].get_center() + txt_up_padding * UP

            proba_txt = Text("p = "+str(p))
            proba_txt.scale(txt_scale)
            proba_txt.shift(shift_to)

            str_h_p = str(h(p))
            if(len(str_h_p)>4):
                str_h_p = str_h_p[0:4]

            h_txt = Text("h("+str(p)+")="+str_h_p)
            h_txt.scale(txt_scale)
            h_txt.shift(shift_to)

            multi_txt = Text("x"+str(str_h_p))
            multi_txt.scale(txt_scale)
            multi_txt.shift(shift_to)

            animations_proba += [Write(proba_txt)]
            animations_h += [ReplacementTransform(proba_txt, h_txt)]
            animations_multi += [ReplacementTransform(h_txt, multi_txt)]

            for j in range(len(self.hist_objects[i])):
                animations += [ApplyMethod(self.hist_objects[i][j].ponderation, h(p), 0.5*self.hist_objects[i][j].height*(h(p)-1) + j*(h(p)-1)*self.hist_objects[i][j].height), FadeOut(multi_txt)]
        
        self.play(*animations_proba, run_time=2)
        self.play(*animations_h, run_time=2)
        self.play(*animations_multi, run_time=2)
        self.play(*animations, run_time=6)

class Weight_func_condi(Scene):
    def construct(self):
        cond1 = Tex("$h(\\mathbb P(x)=0) = 0$")
        cond2 = Tex("$h(\\mathbb P(x)=1) = 0$")
        cond3 = Tex("$h(\\mathbb P(x)\\mathbb P(y)) = h(\\mathbb P(x)) + h(\\mathbb P(y))$")

        conditions = VGroup(cond1, cond2, cond3).arrange(DOWN, buff=0.4)
        self.play(Write(conditions))
        self.wait()

class minse_log(Scene):
    def construct(self):
        text = Tex("$-log$")
        self.play(FadeInFrom(text, 4 * DOWN), run_time = 3)
        self.wait()