# coding: utf-8

import os
import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.image import AsyncImage

from layout import RootWidget, MainLayout, SearchLayout 

        
class MainApp(App):

    def build(self):
        root = RootWidget() # 메인 화면의 기본 위젯
        root.orientation = 'vertical' # 위젯 모양 속성
        
        m = MainLayout() # 메인 레이아웃 FloatLayout
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