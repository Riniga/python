# Start with: manim -pql mathanimation.py DrawCircle
from manim import *

class DrawCircle(Scene):
    def construct(self):
        # Create a circle
        circle = Circle(radius=2, color=BLUE)
        # Add a label
        label = Text("This is a Circle").next_to(circle, DOWN)
        
        # Create the animation
        self.play(Create(circle))  # Animate drawing the circle
        self.play(FadeIn(label))  # Animate fading in the label
        self.wait(2)  # Pause for 2 seconds
