import tkinter as tk
from tkinter import ttk

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', password = "no"):
        super().__init__(master)
        __BGENTRY = "#fafafa"
        __FGENTRY = "#494b59"
        self.__PASSWORD = password
         
        self.placeholder = placeholder
        self.placeholder_color = color
        self['fg'] = __FGENTRY
        self['bg'] = __BGENTRY
        self.default_fg_color = self['fg']

        self['font'] = "roboto 10 normal"
        self['highlightthickness'] = 1
        self.configure(highlightbackground="#c5c7d7", highlightcolor="#c5c7d7")
        

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color
            if self.__PASSWORD == "yes":
                self['show'] = "*"

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()