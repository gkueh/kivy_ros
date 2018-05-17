import sys
sys.path.append("/home/gkuehner/catkin_ws/src/kivy_ros/scripts")

from kivy_client_2 import kivy_button_client

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from ros_sub import kivy_listener
from kivy.clock import Clock
import sys

x = True

class testScreen(App):
	def build(self):
		a = Button(text='Off')
		

		def onOff(button):
			global x
			resp = kivy_button_client(x)
			if resp == True:
				button.text = "Off"
				x = True
				print("Button is Off")
			elif resp == False:
				button.text = "On"
				x = False
				print("Button is On")

		a.bind(on_press=onOff)

		return a


# class butt(Button):
# 	x = True
# 	def updateButt(self. *args):
# 		resp = kivy_button_client(x)

# 		if resp == True:
# 			self.text = "On"
# 		elif resp == False:
# 			self.text = "Off"

# class Time(Label):
# 	def updateTime(self, *args):
# 		msg = kivy_listener()

# 		self.text = msg.data

# class kivy_ros(App):
# 	def build(self):
# 		t = butt()
# 		Clock.schedule_interval(t.updateTime, 1)

# 		return(t)


if __name__ == "__main__":
	# kivy_ros().run()
	testScreen().run()
