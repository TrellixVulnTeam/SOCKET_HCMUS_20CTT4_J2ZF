import kivy
kivy.require('2.0.0')
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '320')
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from button import *


class clientWindow(ScreenManager):
    pass

class connectServer(Screen):
    pass

class progressConnect(Screen):
    pass

class log(Screen):
    pass

class logIn(Screen):
    pass

class signUp(Screen):
    pass

class queryCovid(Screen):
    pass

Builder.load_file("connectServer.kv")
Builder.load_file("progressConnect.kv")
Builder.load_file("log.kv")
Builder.load_file("logIn.kv")
Builder.load_file("signUp.kv")
Builder.load_file("queryCovid.kv")

class clientApp(App):
    processConnectValue = .8
    def build(self):
        global screen_manager
        screen_manager = clientWindow()
        Builder.load_file("clientScreen.kv")
        screen_manager.add_widget(signUp())
        screen_manager.add_widget(connectServer())
        screen_manager.add_widget(progressConnect())
        screen_manager.add_widget(log())
        screen_manager.add_widget(logIn())
        screen_manager.add_widget(queryCovid())
        return screen_manager

    def toLog(self):
        Clock.schedule_once(self.updateprocessValue, .5)
        Clock.schedule_once(self.progressToLog, .5)
    
    def updateprocessValue(self):
        current = self.ids.progress_bar.value
        self.ids.progress_bar.value = self.processConnectValue

    def progressToLog(self):
        if self.ids.progress_bar.value == 1:
            screen_manager.current = "log"
        

# run
clientApp().run()