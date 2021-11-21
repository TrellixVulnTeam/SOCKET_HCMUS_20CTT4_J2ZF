from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.utils import rgba

class HoverButton(Button):
    def __init__(self, **kwargs):
        # Call the initialization function of the parent class
        super(HoverButton, self).__init__(**kwargs)
        # Set the control to fill horizontally and set the height vertically
        self.size_hint = (1, None)
        self.height = 48
        # binding[subscribe]Event handling method of mouse position change
        Window.bind(mouse_pos=self.on_mouse_pos)

    # Mouse position processing method
    def on_mouse_pos(self, *args):
        # Determine whether the control is in root In root control
        if not self.get_root_window():
            return
        # Get mouse position data
        pos = args[1]
        # Check whether the mouse position is in the control
        if self.collide_point(*pos):
            # If on a control, the style method entered by the mouse is called
            Clock.schedule_once(self.mouse_entering, 0)
        else:
            # If on a control, the style method of mouse out is called
             Clock.schedule_once(self.mouse_leaving, 0)
    
    def mouse_leaving(self, *args):
        # Reset background and mouse style
        self.background_color = [11/255, 13/255, 26/255, 1]
        Window.set_system_cursor('arrow')
        # self.background_normal: rgba(11/255, 13/255, 26/255, 0.8)
    def mouse_entering(self, *args):   
        self.background_color = [92/255, 94/255, 97/255, 1]
        Window.set_system_cursor('hand')