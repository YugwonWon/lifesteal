# coding: utf-8

import os
import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage


from kivy.properties import ObjectProperty, StringProperty

fontName = 'NanumGothic.ttf'

class RootWidget(BoxLayout):
    pass


class MainLayout(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(MainLayout, self).__init__(**kwargs)

        with self.canvas.before:
            Color(0, 0, 0, 1)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        
class SearchLayout(GridLayout):

    def __init__(self, **kwargs):
        super(SearchLayout, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Search Meme: '))
        self.meme=TextInput(multiline=False)
        self.add_widget(self.meme)
        # TODO: 검색을 입력했을 때 처리하는 콜백함수 

class MainApp(App):

    def build(self):
        root = RootWidget()
        root.orientation = 'vertical'
        m = MainLayout()
        root.add_widget(m)
        m.add_widget(
            AsyncImage(
                source="images/meme.png",
                size_hint= (1, .5),
                pos_hint={'center_x':.5, 'center_y':.5}))
        s = SearchLayout()
        root.add_widget(s)

        return root

if __name__ == '__main__':
    MainApp().run()