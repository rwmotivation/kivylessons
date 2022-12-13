from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window


Window.clearcolor=(1,1,1,1)


class Welcome_To_Clean_Revolution_AppApp(App):
    def build(self):
          label = Label(text="Clean Revolution", font_size="100sp", bold=True,italic=True,color=(1,0,0,1))
          return label

Welcome_To_Clean_Revolution_AppApp().run()