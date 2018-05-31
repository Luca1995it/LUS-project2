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

############################## NLU PART ########################################

FOLDS=5

train-nlu:
	python bot.py train-nlu

evaluate-nlu:
	python -m rasa_nlu.evaluate \
	--data data/franken_data.json \
	--config nlu_model_config.yml \
	--mode crossvalidation \
	--folds $(FOLDS) \
	--verbose

# SKLEARN
train-nlu-sklearn:
	python -m rasa_nlu.train \
	--config config_nlu/sklearn.yml \
	--data data/franken_data.json \
	--path models/nlu

evaluate-nlu-sklearn:
	python -m rasa_nlu.evaluate \
	--data data/franken_data.json \
	--config config_nlu/sklearn.yml \
	--mode crossvalidation \
	--folds $(FOLDS) \
	--verbose

#MITIE
train-nlu-mitie:
	python -m rasa_nlu.train \
	--config config_nlu/mitie.yml \
	--data data/franken_data.json \
	--path models/nlu

evaluate-nlu-mitie:
	python -m rasa_nlu.evaluate \
	--data data/franken_data.json \
	--config config_nlu/mitie.yml \
	--mode crossvalidation \
	--folds $(FOLDS) \
	--verbose

#MIXED
train-nlu-mixed:
	python -m rasa_nlu.train \
	--config config_nlu/mixed.yml \
	--data data/franken_data.json \
	--path models/nlu

evaluate-nlu-mitie:
	python -m rasa_nlu.evaluate \
	--data data/franken_data.json \
	--config config_nlu/mixed.yml \
	--mode crossvalidation \
	--folds $(FOLDS) \
	--verbose

######################### CORE PART ############################################

train-core:
	python bot.py train-dialogue

evaluate-core:
	python -m rasa_core.evaluate \
	--stories data/babi_stories.md \
	--max_stories 1000 \
	--core models/dialogue \
	--nlu models/nlu/default/current

######################## BUILD & RUNNING #######################################

build: train-nlu train-core

all: build run

populate-db:
	python populate_database.py

run:
	python bot.py run
