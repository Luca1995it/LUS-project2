# Requires PyAudio, PySpeech and SpeechRecognition

import speech_recognition as sr

class Speech2Text:

	def __init__(self):
		self.r = sr.Recognizer()

	def get_next_sentence(self):
		# Record Audio

		with sr.Microphone() as source:
			print("Listening....")
			audio = self.r.listen(source)

		# Speech recognition using Google Speech Recognition
		try:
			# for testing purposes, we're just using the default API key
			# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
			# instead of `r.recognize_google(audio)`
			return self.r.recognize_google(audio)
		except sr.UnknownValueError:
			return None
		except sr.RequestError as e:
			return None
