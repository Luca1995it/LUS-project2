#!/usr/bin/env python3

import pyttsx3 as pt

class Text2Speech:

	def say(self, text):
		engine = pt.init()
		engine.say(text)
		engine.runAndWait()
