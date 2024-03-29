# IDE by denis
#verison python 3.7.0
#date 1 November 2019
from kivy.app import App


from kivy.uix.codeinput import CodeInput
from kivy.uix.textinput import TextInput
from pygments.lexers import CythonLexer

from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView

from kivy.uix.dropdown import DropDown



from os import system, popen, getcwd

class IDE(App):

	langLexer = CythonLexer()

	def build(self):
		root = BoxLayout(orientation="vertical", padding=5)
		self.nameFile = TextInput(text="%s/main.py" % getcwd(), size_hint=[1, .1], background_color=[77, 77, 77, 1], multiline = False)
		root.add_widget(self.nameFile)



		button = GridLayout(cols = 4, size_hint=[1, .07])
		## The drop menu starts here

		dropmenu = DropDown()
		buttonForFile = Button(text="Save", size_hint_y=None, height=40, on_press=self.saveFile)
		dropmenu.add_widget(buttonForFile)
		buttonForFile = Button(text="Open", size_hint_y=None, height=40, on_press=self.openFile)
		dropmenu.add_widget(buttonForFile)


		mainbutton = Button(text="File", size_hint=(1, .07))
		mainbutton.bind(on_release=dropmenu.open)
		button.add_widget(mainbutton)

		## The drop menu ends here
		button.add_widget(Button(text="Compile", on_press=self.compile))
		button.add_widget(Button(text="clean",on_press=self.clean))
		root.add_widget(button)
		self.code = CodeInput(text = "", lexer = CythonLexer(),
)
		button.add_widget(Button(text="about me", on_press=self.aboutme))

		root.add_widget(self.code)

		self.check = TextInput(text="", size_hint=[1, .3],background_color=[77, 77, 77, 1])
		root.add_widget(self.check)
		return root

	def openFile(self, argc):
		try:
			with open(self.nameFile.text) as file:
				self.code.text = file.read()
		except FileNotFoundError:
			self.check.text = "Error: file not found"

	def compile(self, argc, result=""):
		try:
			with open(self.nameFile.text, "w") as file:
				file.write(self.code.text)
		except FileNotFoundError:
				result = "Error: file not found"
		else:
			system("python3 %s" % self.nameFile.text)
			for string in popen("python3 %s" % self.nameFile.text): #'%s' % self.nameFile.text):
				result+=string
		finally:
			self.check.text = result

	def saveFile(self, argc):
		try:
			with open(self.nameFile.text, "w") as file:
				result = "Yeahh. File saved"
				file.write(self.code.text)
		except FileNotFoundError:
			result = "Error: file not found"
		finally:
			self.check.text = result

	def clean(self, argc):
		self.check.text = ""

	def aboutme(self, argc):
		view = ModalView(size_hint=(None, None), size= (320, 240))
		box = GridLayout(cols = 1, size_hint=(.33, 1))
		box.add_widget(Image(source='icon/about.png', size_hint=(.9, .8)))
		box.add_widget(Label(text="Привет, создатель этой проги Денис! :3"))
		box.add_widget(Label(text="Спасибо сайту: https://icons8.ru"))
		view.add_widget(box)
		return view.open()

if __name__ == '__main__':
	IDE().run()
