from rasa_core.actions import Action
from rasa_core.actions.forms import EntityFormField, FormAction
from rasa_core.events import SlotSet
from restaurants_api import RestaurantAPI

# set to false to avoid installing and using MongoDB
ACTIVATE_REAL_DB = True

class ActionSearchRestaurants(FormAction):
	def name(self):
		return 'action_search_restaurants'

	RANDOMIZE = True

	@staticmethod
	def required_fields():
		return [
			EntityFormField("cuisine", "cuisine"),
			EntityFormField("location", "location"),
			EntityFormField("price", "price")
		]

	def submit(self, dispatcher, tracker, domain):
		dispatcher.utter_message("looking for restaurants")
		if ACTIVATE_REAL_DB:
			restaurant_api = RestaurantAPI()
			restaurants = restaurant_api.search(
				tracker.get_slot("cuisine"),
				tracker.get_slot("location"),
				tracker.get_slot("price")
			)
			return [SlotSet("matches", restaurants)]
		else:
			return [SlotSet("matches", ["peppo's pizza party"])]


class ActionSuggest(Action):
	def name(self):
		return 'action_suggest'

	def run(self, dispatcher, tracker, domain):
		if tracker.get_slot("matches") is not None:
			dispatcher.utter_message("here's what I found")
			#dispatcher.utter_message("\n".join([ "- %s, %s cuisine in %s, economical class: %s" % (x['name'],x['cuisine'],x['location'],x['price']) for x in tracker.get_slot("matches")[:5]]))
			dispatcher.utter_message(",".join(tracker.get_slot("matches")))
			dispatcher.utter_message("is it ok for you? because I'm not going to find anything else")
		else:
			dispatcher.utter_message("I did not found any restaurant, please retry with less restrictions")

		return []
