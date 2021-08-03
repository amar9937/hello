from kivy.app import App
from kivy.uix.button import Label
	
class CalcApp(App):
	def build(self):
		return Label(text='Hello')

if __name__ == '__main__':
	CalcApp().run()