import six
from builtins import input
from typing import Text

from rasa_core.channels.channel import UserMessage
from rasa_core import utils
from rasa_core.channels.console import ConsoleOutputChannel, ConsoleInputChannel
from rasa_core.interpreter import INTENT_MESSAGE_PREFIX
from speech2text import Speech2Text
from text2speech import Text2Speech

class SpeechOutputChannel(ConsoleOutputChannel):

	output_channel = Text2Speech()

	def send_text_message(self, recipient_id, message):
		print("Say: " + message)
		self.output_channel.say(message)


class SpeechInputChannel(ConsoleInputChannel):

	input_channel = Speech2Text()
	output_channel = Text2Speech()

	def _record_messages(self, on_message, max_message_limit=None):
		utils.print_color("Bot loaded. Type a message and press enter: ",
						  utils.bcolors.OKGREEN)
		self.output_channel.say("Bot loaded, Say something")
		num_messages = 0
		while max_message_limit is None or num_messages < max_message_limit:
			print("Getting new speech input")
			text = self.input_channel.get_next_sentence()
			while text is None:
				self.output_channel.say("Didn't understand, please retry")
				text = self.input_channel.get_next_sentence()
			print("Undersood:" + text)
			if six.PY2:
				# in python 2 input doesn't return unicode values
				text = text.decode("utf-8")
			if text == INTENT_MESSAGE_PREFIX + 'stop':
				return
			on_message(UserMessage(text, SpeechOutputChannel(), self.sender_id))
			num_messages += 1
