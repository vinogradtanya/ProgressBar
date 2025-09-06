from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        main_layout = StackLayout()
        progressbar = ProgressBar(max = 100, value = 0, size_hint = (1, 0.2))

        main_layout.add_widget(progressbar)

        lbl = Label(text = str(int(progressbar.value)), size_hint = (1, 0.2))
        main_layout.add_widget(lbl)

        button = Button(text = '+', size_hint = (1, 0.2))

        def button_press(instance):
            progressbar.value += 1
            lbl.text = str(int(progressbar.value))

        button.bind(on_press = button_press)

        main_layout.add_widget(button)

        return main_layout

if __name__ == '__main__':
    MyApp().run()