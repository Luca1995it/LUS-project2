# LUS-project2
Second project of the LUS course.

Developed with rasa_core 0.9.3 and rasa_nlu 0.12.3

# HOW TO USE
- First of all, if you want to use the mongoDB database, please install it and \
launch it listening on port 27017. Otherwise, set ACTIVATE_REAL_DB in \
custom_actions.py to False.

- To automatically populate the DB (if you are using it), launch the following command:

```make populate_db```

- To train the bot on the Franken and Babi dataset, launch the following command:

```make build```

- To run the bot, launche the following command:

```make run```


# HOW TO EVALUATE
- To evaluate the NLU launch one of the following commands depending on the pipeline you want to evaluate:

```make evaluate-nlu-sklearn```

```make evaluate-nlu-mitie```

```make evaluate-nlu-mixed```

- To evaluate the policies, please select a Policy in bot.py, line 75, then run:

```make evaluate-core```
