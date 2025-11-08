#Importing libraries
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.textinput import TextInput
from Instructions import *

#Classes
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        #Each individual screen must be added with its own unique name and class name
        sm.add_widget(Screen1(name = "first"))
        sm.add_widget(Screen2(name = "second"))
        #sm.add_widget(Screen3(name = "scr3"))   

        #The screen manager is the final visual product on screen
        return sm   

#Add all 3 screens as this one without kwargs
class Screen1(Screen):
    def __init__(self, name = "first"): #Second parameter becomes name = "first/second/etc"
        super().__init__(name = name) #name=name
        #Creating widgets
        vl = BoxLayout(orientation = "vertical", padding = 8, spacing = 40)
        instructions = Label(text = screen1_instructions, pos_hint = {"center_x" : 0.5, "center_y" : 0.5})
        hl = BoxLayout(orientation = "horizontal", size_hint = (1,.15), padding = 8, spacing = 8)
        name = Label(text = screen1_name, pos_hint = {"x" : 1})
        name_input = TextInput(text = "aa", pos_hint = {"x" : 1}, halign = "left", focus = True, multiline = False)
        hl2 = BoxLayout(orientation = "horizontal", size_hint = (1,.15), padding = 8, spacing = 8)
        age = Label(text = screen1_age, size_hint = (.5,1), pos_hint = {"x" : 1})
        age_input = TextInput(text = "bb", size_hint = (.5,1), pos_hint = {"x" : 0, "center_y" : 0.5}, halign = "left", focus = True, multiline = False)
        btn = Button(text = screen1_button, size_hint = (.2,.2), pos_hint = {"center_x" : 0.5, "center_y" : 0.5})

        #Event handling
        btn.on_press = self.next

        #Placing widgets
        vl.add_widget(instructions)
        vl.add_widget(hl)
        hl.add_widget(name)
        hl.add_widget(name_input)
        vl.add_widget(hl2)
        hl2.add_widget(age)
        hl2.add_widget(age_input)
        vl.add_widget(btn)

        #Final layout must be added as a widget to each individual screen
        self.add_widget(vl)
    
    def next(self):
        self.manager.transition.direction = "left"
        self.manager.current = "second"


class Screen2(Screen):
    def __init__(self, name = "second"): #Second parameter becomes name = "first/second/etc"
        super().__init__(name = name) #name=name
        #Button creation
        btn_2 = Button(text = "This is the second screen")

        #Testing widgets on second screen
        self.add_widget(btn_2)

#Main Code
app = MyApp()
app.run()