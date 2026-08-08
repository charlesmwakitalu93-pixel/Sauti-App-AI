from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
import webbrowser

Window.size = (360, 640)

class SautiAppAI(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = MDBoxLayout(
            orientation='vertical',
            padding=20,
            spacing=20,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        
        self.title_label = MDLabel(
            text="Sauti App AI",
            halign="center",
            font_style="H4",
            theme_text_color="Primary"
        )
        layout.add_widget(self.title_label)
        
        self.status_label = MDLabel(
            text="Karibu! Sauti ya AI na Google Cloud iko tayari.",
            halign="center",
            theme_text_color="Secondary"
        )
        layout.add_widget(self.status_label)
        
        self.play_btn = MDRaisedButton(
            text="Cheza Sauti ya AI (Uhalisia)",
            pos_hint={'center_x': 0.5},
            md_bg_color=(0.1, 0.5, 0.8, 1)
        )
        self.play_btn.bind(on_press=self.play_ai_voice)
        layout.add_widget(self.play_btn)
        
        self.youtube_btn = MDRaisedButton(
            text="Fungua YouTube (Sauti za Mtaani)",
            pos_hint={'center_x': 0.5},
            md_bg_color=(0.8, 0.1, 0.1, 1)
        )
        self.youtube_btn.bind(on_press=self.open_youtube)
        layout.add_widget(self.youtube_btn)
        
        self.add_widget(layout)

    def play_ai_voice(self, instance):
        self.status_label.text = "Inapakia sauti ya uhalisia..."

    def open_youtube(self, instance):
        webbrowser.open("https://www.youtube.com")

class SautiAppAIApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return SautiAppAI()

if __name__ == '__main__':
    SautiAppAIApp().run()
