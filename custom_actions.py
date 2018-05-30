from rasa_core.actions import Action
from rasa_core.events import SlotSet
from restaurants_api import RestaurantAPI

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		dispatcher.utter_message("looking for restaurants")
		restaurant_api = RestaurantAPI()
		query = {}
		if tracker.get_slot("cuisine") is not None:
			query['cuisine'] = tracker.get_slot("cuisine")
		if tracker.get_slot("location") is not None:
			query['location'] = tracker.get_slot("location")
		if tracker.get_slot("price") is not None:
			query['price'] = tracker.get_slot("price")

		restaurants = restaurant_api.search(query)
		return [SlotSet("matches", restaurants)]

class ActionSuggest(Action):
	def name(self):
		return 'action_suggest'

	def run(self, dispatcher, tracker, domain):
		if tracker.get_slot("matches") is not None:
			dispatcher.utter_message("here's what I found")
			dispatcher.utter_message("\n".join([ "- %s, %s cuisine in %s, economical class: %s" % (x['name'],x['cuisine'],x['location'],x['price']) for x in tracker.get_slot("matches")[:5]]))
			dispatcher.utter_message("is it ok for you? because I'm not going to find anything else")
		else:
			dispatcher.utter_message("I did not found any restaurant, please retry with less restrictions")

		return []
