# coding: utf-8

import os
import kivy
kivy.require('2.1.0')
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty

fontName = 'NanumGothic.ttf'


class Controller(FloatLayout):
    '''Create a controller that receives a custom widget from the kv lang file.

    Add an action to be called from the kv lang file.
    '''
    label_wid = ObjectProperty()
    info = StringProperty()
    def bttn01_clicked(self):
        layout = FloatLayout()
        button01 = Button(text = 'Button 01', size_hint =(.5, .0))
        layout.add_widget(button01)
        self.label_wid.text = 'clicked the button'
        self.info = 'New info text'

class ControllerApp(App):

    def build(self):
        return Controller(info = 'hello world')


if __name__ == '__main__':
    ControllerApp().run()