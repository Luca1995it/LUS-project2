from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import warnings

from policy import RestaurantPolicy
from rasa_core import utils
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.events import SlotSet
from rasa_core.featurizers import (
	MaxHistoryTrackerFeaturizer,
	BinarySingleStateFeaturizer)
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.sklearn_policy import SklearnPolicy
from rasa_core.policies.augmented_memoization import AugmentedMemoizationPolicy
from rasa_core.policies.ensemble import SimplePolicyEnsemble
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from speech_channel import SpeechInputChannel

logger = logging.getLogger(__name__)

# set to false to use the standard ConsoleInputChannel
SPEECH_ON = True

def train_dialogue(domain_file="restaurant_domain.yml",
				   model_path="models/dialogue",
				   training_data_file="data/babi_stories.md"):
	agent = Agent(domain_file,[MemoizationPolicy(max_history=3),
								RestaurantPolicy()])

	training_data = agent.load_data(training_data_file)
	agent.train(
			training_data,
			epochs=400,
			batch_size=100,
			validation_split=0.2
	)

	agent.persist(model_path)
	return agent


def train_core(domain_file="restaurant_domain.yml",
				   model_path="models/dialogue",
				   training_data_file="data/train_babi_stories.md"):

	policies_array = [
		[MemoizationPolicy(max_history=3)],                                               #gut
		[MemoizationPolicy(max_history=5)],                                               #gut
		[AugmentedMemoizationPolicy()],                                                   #gut
		[RestaurantPolicy()],                                                             #gut
		[KerasPolicy()],                                                                  #gut
		[FallbackPolicy()],                                                               #gut
		[FallbackPolicy(core_threshold=0.5)],                                             #gut
		[SklearnPolicy(scoring=['accuracy','f1'])],                                       #gut
		[MemoizationPolicy(max_history=3), RestaurantPolicy()],                           #gut
		[AugmentedMemoizationPolicy(), RestaurantPolicy()],                               #gut
		[MemoizationPolicy(max_history=3), KerasPolicy()],                                #gut
		[AugmentedMemoizationPolicy(), KerasPolicy()],                                    #gut
		[MemoizationPolicy(max_history=3), SklearnPolicy(scoring=['accuracy','f1'])],     #gut
		[AugmentedMemoizationPolicy(), SklearnPolicy(scoring=['accuracy','f1'])],         #gut
		[MemoizationPolicy(max_history=3), KerasPolicy(), SklearnPolicy()],               #gut
		[MemoizationPolicy(max_history=3), RestaurantPolicy(), SklearnPolicy()],          #gut
		[AugmentedMemoizationPolicy(), RestaurantPolicy(), SklearnPolicy(scoring=['accuracy','f1'])]  #gut
	]

	index_policies = -4
	print("Training policies: [%s]" % ",".join([x.__class__.__name__ for x in policies_array[index_policies]]))
	agent = Agent(domain_file,policies_array[index_policies])

	training_data = agent.load_data(training_data_file)
	agent.train(
			training_data,
			epochs=400,
			batch_size=100,
			validation_split=0.2
	)

	agent.persist(model_path)
	return agent


def train_nlu():
	from rasa_nlu.training_data import load_data
	from rasa_nlu import config
	from rasa_nlu.model import Trainer

	training_data = load_data('data/franken_data.json')
	trainer = Trainer(config.load("nlu_model_config.yml"))
	trainer.train(training_data)
	model_directory = trainer.persist('models/nlu/',
									  fixed_model_name="current")

	return model_directory


def run(serve_forever=True):
	interpreter = RasaNLUInterpreter("models/nlu/default/current")
	agent = Agent.load("models/dialogue", interpreter=interpreter)

	if serve_forever:
		if SPEECH_ON:
			agent.handle_channel(SpeechInputChannel())
		else:
			agent.handle_channel(ConsoleInputChannel())

	return agent


if __name__ == '__main__':
	utils.configure_colored_logging(loglevel="INFO")

	parser = argparse.ArgumentParser(
			description='starts the bot')

	parser.add_argument(
		'task',
		choices=["train-nlu", "train-dialogue", "train-core", "run"],
		help="what the bot should do - e.g. run or train?"
	)

	task = parser.parse_args().task

	# decide what to do based on first parameter of the script
	if task == "train-nlu":
		train_nlu()
	elif task == "train-dialogue":
		train_dialogue()
	elif task == "train-core":
		train_core()
	elif task == "run":
		run()
