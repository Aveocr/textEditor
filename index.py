# IDE by denis


#verison python 3.7.0

#date 1 November 2019


from kivy.app import App


from kivy.uix.codeinput import CodeInput
from kivy.uix.textinput import TextInput 
from pygments.lexers import CythonLexer

from kivy.uix.widget import Widget 
from kivy.uix.label import Label 
from kivy.uix.button import Button 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


from os import system, popen
from os import getcwd

work = True
class Error(Widget):
	def build(self):
		pass

class AboutMe(Widget):
	def build(self):
		return Label(text="Привет, я создатель этой проги Денис! :3")

class IDE(App):
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

	def save(self, argc):
		try:
			with open(self.nameFile.text, "w") as file:
				result = "Yeahh. File saved"
				file.write(self.code.text)
		except FileNotFoundError:
			result = "Error: file not found"
		finally:
			self.check.text = result
	def build(self):
		root = BoxLayout(
			orientation="vertical",
			padding=5)
		self.nameFile = TextInput(
			text="%s/main.py" % getcwd(),
			size_hint=[1, .1],
			background_color=[77, 77, 77, 1]
			)
		root.add_widget(self.nameFile)
		button = GridLayout(cols = 4, size_hint=[1, .07])
		button.add_widget(
			Button(
				text="Open",
				on_press = self.openFile
				)
			)
		button.add_widget(
			Button(
				text="Compile",
				on_press=self.compile
				)
			)
		button.add_widget(
			Button(
				text="Save",
				on_press=self.save
				)
			)
		button.add_widget(
			Button(
				text="about me",
				on_press=AboutMe()
				)
			)
		root.add_widget(button)
		self.code = CodeInput(
			text = "1",
			lexer = CythonLexer(),
			)

		root.add_widget(self.code)

		self.check = TextInput(
				text="",
				size_hint=[1, .3],
				background_color=[77, 77, 77, 1]
			)
		root.add_widget(self.check)
		return root



if __name__ == '__main__':
	IDE().run()
else :

	Error().run() 
