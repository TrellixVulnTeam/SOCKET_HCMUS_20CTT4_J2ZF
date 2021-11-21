from kivy.uix.scatter import Scatter
from kivy.app import App
from kivy.graphics.svg import Svg
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
#from IPython.display import SVG

Builder.load_string("""
<SvgWidget>:
    do_rotation: False
<FloatLayout>:
    canvas.before:
        Color:
            rgb: (1, 1, 1)
        Rectangle:
            pos: self.pos
            size: self.size
""")

#SVG(filename="../testchess/boards/board_0.1.7.svg") 
class SvgWidget(Scatter):

    def __init__(self, filename, **kwargs):
        super(SvgWidget, self).__init__(**kwargs)
        with self.canvas:
            svg = Svg(filename)
        self.size = svg.width, svg.height


class SvgApp(App):

    def build(self):
        self.root = FloatLayout()

        filename = ".\img\covid.svg"
        svg = SvgWidget(filename, size_hint=(None, None), pos_hint={'center_x': 0.5, 'top': 1})
        self.root.add_widget(svg)
        svg.scale = 2


if __name__ == '__main__':
    SvgApp().run()