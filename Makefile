help:
	@echo "--- populate-db"
	@echo "------- Populate the mongoDB database with some restaurants"
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
	@echo "--- evaluate-nlu-sklearn"
	@echo "------- Evaluate the performances of the NLU with sklearn pipeline"
	@echo "--- evaluate-nlu-mitie"
	@echo "------- Evaluate the performances of the NLU with mitie pipeline"
	@echo "--- evaluate-nlu-mixed"
	@echo "------- Evaluate the performances of the NLU with mixed pipeline"
	@echo "--- evaluate-core"
	@echo "------- Evaluate the performances of your policies predicting the next action"

############################ RUN SECTION #######################################

FOLDS=5

train-nlu:
	python bot.py train-nlu

train-core:
	python bot.py train-dialogue

build: train-nlu train-core

all: build run

populate-db:
	python populate_database.py

run:
	python bot.py run

######################## EVALUATION SECTION ####################################

##### CORE

init-data:
	python split_stories.py

evaluate-core: init-data
	python bot.py train-core

	python -m rasa_core.evaluate \
	--stories data/evaluate_babi_stories.md \
	--core models/dialogue


##### NLU PIPELINES

# SKLEARN
train-nlu-sklearn:
	python -m rasa_nlu.train \
	--config config_nlu/sklearn.yml \
	--data data/franken_data.json \
	--path models/nlu

evaluate-nlu-sklearn: train-nlu-sklearn
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

evaluate-nlu-mitie: train-nlu-mitie
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

evaluate-nlu-mixed: train-nlu-mixed
	python -m rasa_nlu.evaluate \
	--data data/franken_data.json \
	--config config_nlu/mixed.yml \
	--mode crossvalidation \
	--folds $(FOLDS) \
	--verbose
