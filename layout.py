import os
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

from kivy.uix.image import AsyncImage

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition

KOREAN_FONT = os.getcwd() + '/fonts/Nanum-Gothic.ttf'

class RootWidget(BoxLayout):
    pass


class MainLayout(FloatLayout):
    """ 
    화면 상단에 이미지를 넣는 레이아웃
    
    """
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(MainLayout, self).__init__(**kwargs)

        with self.canvas.before: # 메인 레이아웃 배경 색상 지정(검정)
            Color(0, 0, 0, 1)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        
class SearchLayout(GridLayout):
    """ 
    검색을 할 수 있는 2cols을 가진 gridlayout 생성 
    
    """
    def __init__(self, **kwargs):
        super(SearchLayout, self).__init__(**kwargs)
        self.cols = 1
        self.input_txt = None
        self.inside = GridLayout() 
        self.inside.cols = 2
        
        self.inside.add_widget(Label(text='검색어 입력:  ', font_name=KOREAN_FONT))
        self.search_bar=TextInput(multiline=False, font_name=KOREAN_FONT)
        self.search_bar.bind(text=self.on_text)
        self.inside.add_widget(self.search_bar)
        
        self.add_widget(self.inside)
        
        self.submit = Button(text="검색하기", font_size=40, font_name=KOREAN_FONT)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
        # TODO: 검색을 입력했을 때 처리하는 콜백함수 

    def pressed(self, instance): # 콜백
        print(f"input_text: {self.input_txt}")
        print(f"instance: {instance}")
        
    def on_focus(self, instance, value):
        """ 
        TextInput에서 엔터를 쳐도 포커스를 잃지 않게 만든다.
        
        """
        self.submit.focus = True 
                
    def on_text(self, instance, value):
        print('The widget', instance, 'have:', value)    
        self.input_txt = value
        

class ScreenLayout(Screen):
    def __init__(self, **kwargs):
        super(ScreenLayout, self).__init__(**kwargs)
        
        root = BoxLayout(orientation='vertical')
        # root.add_widget(Label(text=self.name, font_size=50))
        m = MainLayout() # 메인 레이아웃 FloatLayout
            
        root.add_widget(m)
        m.add_widget(
            AsyncImage(
                source="images/meme.png",
                size_hint= (1, .5),
                pos_hint={'center_x':.5, 'center_y':.5}))
        
        s = SearchLayout()
        root.add_widget(s)
        # Add another layout to handle the navigation
        # and set the height of navigation to 20%
        # of the CustomScreen
        self.navig = BoxLayout(size_hint_y=0.2)

        # Create buttons with a custom text
        self.prev = Button(text='Previous')
        self.next = Button(text='Next')

        # Bind to 'on_release' events of Buttons
        self.prev.bind(on_release=self.switch_prev)
        self.next.bind(on_release=self.switch_prev)

        # Add buttons to navigation
        # and the navigation to layout
        self.navig.add_widget(self.prev)
        self.navig.add_widget(self.next)
        root.add_widget(self.navig)

        # And add the layout to the Screen
        self.add_widget(root)

    def switch_prev(self, *args):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = self.manager.previous()

    def switch_next(self, *args):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = self.manager.next()
        self.remove_widget(self.next)
        
    def remove_button(self, instance):
        self.remove_widget(instance)
 