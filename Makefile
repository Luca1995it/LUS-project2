help:
	@echo "--- train-nlu"
	@echo "------- Train the natural language understanding using Rasa NLU."
	@echo "--- train-core"
	@echo "------- Train a dialogue model using Rasa core."
	@echo "--- build"
	@echo "------- Train both NLU and Core"
	@echo "--- run"
	@echo "------- Run the bot on the trained NLU and Core"
	@echo "--- all"
	@echo "------- Train and run"
	@echo "--- evaluate-nlu"
	@echo "------- Evaluate the performances of the NLU tool"
	@echo "--- evaluate-core"
	@echo "------- Evaluate the performances of your policies predicting the next action"

run:
	python bot.py run

train-nlu:
	python bot.py train-nlu

train-core:
	python bot.py train-dialogue

build: train-nlu train-core

all: build run

evaluate-nlu:
	python -m rasa_nlu.evaluate \
	--data data/franken_data.json \
	--config nlu_model_config.yml \
	--mode crossvalidation \
	--folds 5 \
	--verbose


evaluate-core:
	python -m rasa_core.evaluate \
	--stories data/babi_stories.md \
	--max_stories 1000 \
	--core models/dialogue \
	--nlu models/nlu/default/current
