## 1* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 2* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "bombay"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 3* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "bombay", "people": "four"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 4* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 5* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "rome", "people": "eight"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 6* greet
 - utter_ask_howcanhelp
* inform{"people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 7* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 8* greet
 - utter_ask_howcanhelp
* inform{"price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 9* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 10* greet
 - utter_ask_howcanhelp
* inform{"location": "london"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 11* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "madrid", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 12* greet
 - utter_ask_howcanhelp
* inform{"price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 13* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "london"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 14* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "four", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 15* greet
 - utter_ask_howcanhelp
* inform{"location": "rome", "people": "eight", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 16* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "paris"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 17* greet
 - utter_ask_howcanhelp
* inform{"location": "london"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 18* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "paris", "price": "moderate"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 19* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "people": "two"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 20* greet
 - utter_ask_howcanhelp
* inform{"price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 21* greet
 - utter_ask_howcanhelp
* inform{"location": "rome"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 22* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "people": "six", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 23* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "people": "six", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 24* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "paris", "price": "moderate"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 25* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "people": "six"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 26* greet
 - utter_ask_howcanhelp
* inform{"location": "london"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 27* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "madrid"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 28* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "paris"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 29* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 30* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 31* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 32* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "rome"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 33* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 34* greet
 - utter_ask_howcanhelp
* inform{"people": "two", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 35* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 36* greet
 - utter_ask_howcanhelp
* inform{"location": "london", "people": "eight", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 37* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "bombay", "people": "two"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 38* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "london"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 39* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 40* greet
 - utter_ask_howcanhelp
* inform{"people": "six", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 41* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "madrid", "people": "six"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 42* greet
 - utter_ask_howcanhelp
* inform{"price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 43* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "london"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 44* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 45* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 46* greet
 - utter_ask_howcanhelp
* inform{"location": "london"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 47* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "madrid", "people": "six"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 48* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "people": "four", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 49* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 50* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "four", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 51* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 52* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "madrid", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 53* greet
 - utter_ask_howcanhelp
* inform{"people": "four", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 54* greet
 - utter_ask_howcanhelp
* inform{"people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 55* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 56* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "people": "six", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 57* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 58* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "people": "eight", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 59* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "four", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 60* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "london", "price": "expensive"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 61* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "london", "price": "moderate"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 62* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "people": "eight", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 63* greet
 - utter_ask_howcanhelp
* inform{"location": "london", "people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 64* greet
 - utter_ask_howcanhelp
* inform{"location": "rome"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 65* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 66* greet
 - utter_ask_howcanhelp
* inform{"location": "paris"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 67* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "madrid", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 68* greet
 - utter_ask_howcanhelp
* inform{"people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 69* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "madrid"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 70* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 71* greet
 - utter_ask_howcanhelp
* inform{"price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 72* greet
 - utter_ask_howcanhelp
* inform{"people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 73* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 74* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "rome", "price": "moderate"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 75* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 76* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 77* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 78* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 79* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 80* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "rome", "price": "expensive"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 81* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "rome", "people": "two"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 82* greet
 - utter_ask_howcanhelp
* inform{"price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 83* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "paris", "price": "expensive"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 84* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 85* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 86* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "people": "two", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 87* greet
 - utter_ask_howcanhelp
* inform{"location": "rome"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 88* greet
 - utter_ask_howcanhelp
* inform{"people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 89* greet
 - utter_ask_howcanhelp
* inform{"location": "london", "people": "six", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 90* greet
 - utter_ask_howcanhelp
* inform{"location": "paris"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 91* greet
 - utter_ask_howcanhelp
* inform{"location": "rome", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 92* greet
 - utter_ask_howcanhelp
* inform{"price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 93* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "people": "four"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 94* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "bombay"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 95* greet
 - utter_ask_howcanhelp
* inform{"people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 96* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 97* greet
 - utter_ask_howcanhelp
* inform{"people": "eight", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 98* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 99* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 100* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "people": "four", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 101* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "four"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 102* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "people": "eight", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 103* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 104* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "london", "price": "moderate"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 105* greet
 - utter_ask_howcanhelp
* inform{"location": "rome", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 106* greet
 - utter_ask_howcanhelp
* inform{"people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 107* greet
 - utter_ask_howcanhelp
* inform{"people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 108* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 109* greet
 - utter_ask_howcanhelp
* inform{"people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 110* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "london", "people": "two"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 111* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "bombay", "people": "four"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 112* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "people": "eight", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 113* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "people": "six"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 114* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 115* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "eight", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 116* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "paris", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 117* greet
 - utter_ask_howcanhelp
* inform{"location": "rome", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 118* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "people": "eight", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 119* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 120* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "people": "six", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 121* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "people": "two", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 122* greet
 - utter_ask_howcanhelp
* inform{"price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 123* greet
 - utter_ask_howcanhelp
* inform{"people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 124* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 125* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "bombay"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 126* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "people": "eight", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 127* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 128* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "people": "six", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 129* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "people": "four"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 130* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "bombay", "people": "six"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 131* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 132* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "paris", "people": "six"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 133* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 134* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "paris", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 135* greet
 - utter_ask_howcanhelp
* inform{"location": "paris"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 136* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "london"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 137* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 138* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 139* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 140* greet
 - utter_ask_howcanhelp
* inform{"people": "four", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 141* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "six", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 142* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "rome", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 143* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 144* greet
 - utter_ask_howcanhelp
* inform{"location": "paris"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 145* greet
 - utter_ask_howcanhelp
* inform{"people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 146* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "paris"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 147* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "rome", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 148* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "madrid"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 149* greet
 - utter_ask_howcanhelp
* inform{"price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 150* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "four", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 151* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "london", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 152* greet
 - utter_ask_howcanhelp
* inform{"people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 153* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "london", "price": "expensive"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 154* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 155* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "rome", "people": "eight"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 156* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "paris", "price": "moderate"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 157* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 158* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "madrid", "people": "four"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 159* greet
 - utter_ask_howcanhelp
* inform{"location": "paris"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 160* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "paris", "people": "eight"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 161* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "paris", "people": "two"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 162* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 163* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 164* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 165* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 166* greet
 - utter_ask_howcanhelp
* inform{"location": "rome"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 167* greet
 - utter_ask_howcanhelp
* inform{"people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 168* greet
 - utter_ask_howcanhelp
* inform{"location": "rome", "people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 169* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "bombay", "price": "expensive"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 170* greet
 - utter_ask_howcanhelp
* inform{"people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 171* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "four", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 172* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "people": "six", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 173* greet
 - utter_ask_howcanhelp
* inform{"people": "eight", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 174* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 175* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "paris", "people": "two"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 176* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 177* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "london", "people": "four"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 178* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 179* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 180* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "people": "eight"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 181* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "london", "people": "six"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 182* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 183* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "four", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 184* greet
 - utter_ask_howcanhelp
* inform{"price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 185* greet
 - utter_ask_howcanhelp
* inform{"people": "eight", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 186* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 187* greet
 - utter_ask_howcanhelp
* inform{"people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 188* greet
 - utter_ask_howcanhelp
* inform{"people": "eight", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 189* greet
 - utter_ask_howcanhelp
* inform{"people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 190* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 191* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 192* greet
 - utter_ask_howcanhelp
* inform{"location": "london", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 193* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 194* greet
 - utter_ask_howcanhelp
* inform{"location": "paris"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 195* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 196* greet
 - utter_ask_howcanhelp
* inform{"people": "four", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 197* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "paris", "price": "moderate"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 198* greet
 - utter_ask_howcanhelp
* inform{"price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 199* greet
 - utter_ask_howcanhelp
* inform{"location": "rome", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 200* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 201* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "six", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 202* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "london"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 203* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "paris", "people": "four"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 204* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 205* greet
 - utter_ask_howcanhelp
* inform{"price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 206* greet
 - utter_ask_howcanhelp
* inform{"people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 207* greet
 - utter_ask_howcanhelp
* inform{"location": "rome"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 208* greet
 - utter_ask_howcanhelp
* inform{"price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 209* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "rome", "price": "expensive"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 210* greet
 - utter_ask_howcanhelp
* inform{"location": "paris"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 211* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 212* greet
 - utter_ask_howcanhelp
* inform{"location": "paris"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 213* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 214* greet
 - utter_ask_howcanhelp
* inform{"people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 215* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "bombay"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 216* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "rome", "people": "two"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 217* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "bombay"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 218* greet
 - utter_ask_howcanhelp
* inform{"location": "paris"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 219* greet
 - utter_ask_howcanhelp
* inform{"people": "four", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 220* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 221* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "two"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 222* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "two", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 223* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "people": "six", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 224* greet
 - utter_ask_howcanhelp
* inform{"people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 225* greet
 - utter_ask_howcanhelp
* inform{"price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 226* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "six", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 227* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 228* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "people": "four", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 229* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 230* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 231* greet
 - utter_ask_howcanhelp
* inform{"price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 232* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 233* greet
 - utter_ask_howcanhelp
* inform{"price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 234* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "two", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 235* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "four", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 236* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 237* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 238* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 239* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 240* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 241* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "four", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 242* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "madrid", "price": "moderate"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 243* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 244* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "bombay", "people": "six"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 245* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 246* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "madrid"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 247* greet
 - utter_ask_howcanhelp
* inform{"price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 248* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "madrid", "people": "six"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 249* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 250* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 251* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "paris"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 252* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 253* greet
 - utter_ask_howcanhelp
* inform{"price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 254* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "people": "six", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 255* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "bombay", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 256* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "london", "people": "four"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 257* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 258* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 259* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "people": "four"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 260* greet
 - utter_ask_howcanhelp
* inform{"price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 261* greet
 - utter_ask_howcanhelp
* inform{"people": "six", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 262* greet
 - utter_ask_howcanhelp
* inform{"location": "rome", "people": "eight", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 263* greet
 - utter_ask_howcanhelp
* inform{"people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 264* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "madrid", "people": "four"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 265* greet
 - utter_ask_howcanhelp
* inform{"people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 266* greet
 - utter_ask_howcanhelp
* inform{"location": "paris"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 267* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 268* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "london", "price": "expensive"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 269* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "rome", "price": "moderate"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 270* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "bombay", "people": "eight"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 271* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "people": "four", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 272* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 273* greet
 - utter_ask_howcanhelp
* inform{"location": "london", "people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 274* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 275* greet
 - utter_ask_howcanhelp
* inform{"people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 276* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "eight", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 277* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 278* greet
 - utter_ask_howcanhelp
* inform{"location": "london", "people": "four", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 279* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 280* greet
 - utter_ask_howcanhelp
* inform{"people": "six", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 281* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "six"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 282* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 283* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "people": "four"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 284* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 285* greet
 - utter_ask_howcanhelp
* inform{"people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 286* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "people": "four"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 287* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 288* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 289* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "madrid", "price": "moderate"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 290* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 291* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 292* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "people": "six"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 293* greet
 - utter_ask_howcanhelp
* inform{"location": "rome", "people": "eight", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 294* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "eight"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 295* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "london", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 296* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "paris", "price": "moderate"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 297* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 298* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "six", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 299* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 300* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 301* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "people": "six", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 302* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 303* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 304* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "paris", "price": "moderate"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 305* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "london", "people": "two"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 306* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "london", "people": "four"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 307* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 308* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 309* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "paris", "price": "expensive"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 310* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "people": "two"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 311* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 312* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 313* greet
 - utter_ask_howcanhelp
* inform{"people": "eight", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 314* greet
 - utter_ask_howcanhelp
* inform{"people": "four", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 315* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 316* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "people": "six", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 317* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "four", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 318* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "six"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 319* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 320* greet
 - utter_ask_howcanhelp
* inform{"location": "london"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 321* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "six", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 322* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "four"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 323* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "six"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 324* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "four", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 325* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "four", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 326* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "six"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 327* greet
 - utter_ask_howcanhelp
* inform{"location": "london", "people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 328* greet
 - utter_ask_howcanhelp
* inform{"location": "rome", "people": "eight", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 329* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 330* greet
 - utter_ask_howcanhelp
* inform{"people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 331* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 332* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "rome", "people": "two"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 333* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 334* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "six", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 335* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 336* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "paris"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 337* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "paris"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 338* greet
 - utter_ask_howcanhelp
* inform{"people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 339* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 340* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "london", "price": "moderate"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 341* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "people": "six"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 342* greet
 - utter_ask_howcanhelp
* inform{"location": "paris"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 343* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 344* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "london", "people": "two"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 345* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "bombay", "price": "moderate"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 346* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 347* greet
 - utter_ask_howcanhelp
* inform{"location": "london", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 348* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 349* greet
 - utter_ask_howcanhelp
* inform{"people": "two", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 350* greet
 - utter_ask_howcanhelp
* inform{"people": "eight", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 351* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 352* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 353* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 354* greet
 - utter_ask_howcanhelp
* inform{"price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 355* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 356* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 357* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "eight", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 358* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 359* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "bombay", "people": "two"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 360* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "two", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 361* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "london"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 362* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "london", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 363* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "paris", "people": "eight"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 364* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 365* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 366* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "people": "two", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 367* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "london", "people": "four"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 368* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 369* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 370* greet
 - utter_ask_howcanhelp
* inform{"price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 371* greet
 - utter_ask_howcanhelp
* inform{"price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 372* greet
 - utter_ask_howcanhelp
* inform{"location": "rome"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 373* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "bombay"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 374* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 375* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 376* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "people": "six", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 377* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "four"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 378* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 379* greet
 - utter_ask_howcanhelp
* inform{"location": "paris"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 380* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 381* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 382* greet
 - utter_ask_howcanhelp
* inform{"people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 383* greet
 - utter_ask_howcanhelp
* inform{"people": "eight", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 384* greet
 - utter_ask_howcanhelp
* inform{"people": "eight", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 385* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 386* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "paris", "price": "expensive"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 387* greet
 - utter_ask_howcanhelp
* inform{"location": "london", "people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 388* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 389* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "people": "four", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 390* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 391* greet
 - utter_ask_howcanhelp
* inform{"location": "rome", "people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 392* greet
 - utter_ask_howcanhelp
* inform{"price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 393* greet
 - utter_ask_howcanhelp
* inform{"location": "rome"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 394* greet
 - utter_ask_howcanhelp
* inform{"people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 395* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "madrid", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 396* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 397* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 398* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "people": "six", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 399* greet
 - utter_ask_howcanhelp
* inform{"people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 400* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 401* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "madrid", "price": "expensive"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 402* greet
 - utter_ask_howcanhelp
* inform{"people": "eight", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 403* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "paris", "people": "six"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 404* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 405* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "six", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 406* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "madrid", "people": "six"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 407* greet
 - utter_ask_howcanhelp
* inform{"people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 408* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 409* greet
 - utter_ask_howcanhelp
* inform{"price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 410* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 411* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 412* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 413* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "bombay"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 414* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "bombay", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 415* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 416* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "six", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 417* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "people": "four"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 418* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "bombay"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 419* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "madrid", "price": "moderate"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 420* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "paris", "people": "four"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 421* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "paris", "people": "four"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 422* greet
 - utter_ask_howcanhelp
* inform{"location": "rome", "people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 423* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "london", "people": "four"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 424* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "london", "people": "two"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 425* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 426* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 427* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 428* greet
 - utter_ask_howcanhelp
* inform{"location": "rome", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 429* greet
 - utter_ask_howcanhelp
* inform{"location": "paris"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 430* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 431* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "madrid", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 432* greet
 - utter_ask_howcanhelp
* inform{"people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 433* greet
 - utter_ask_howcanhelp
* inform{"people": "eight", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 434* greet
 - utter_ask_howcanhelp
* inform{"people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 435* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 436* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 437* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 438* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 439* greet
 - utter_ask_howcanhelp
* inform{"price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 440* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 441* greet
 - utter_ask_howcanhelp
* inform{"people": "two", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 442* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "madrid", "people": "eight"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 443* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 444* greet
 - utter_ask_howcanhelp
* inform{"people": "four", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 445* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "rome", "price": "moderate"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 446* greet
 - utter_ask_howcanhelp
* inform{"people": "six", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 447* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 448* greet
 - utter_ask_howcanhelp
* inform{"location": "paris"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 449* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 450* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "people": "four", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 451* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "madrid", "people": "two"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 452* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 453* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 454* greet
 - utter_ask_howcanhelp
* inform{"price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 455* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 456* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "eight", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 457* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "people": "eight", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 458* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "two", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 459* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 460* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 461* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "people": "six", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 462* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 463* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 464* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 465* greet
 - utter_ask_howcanhelp
* inform{"people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 466* greet
 - utter_ask_howcanhelp
* inform{"location": "paris"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 467* greet
 - utter_ask_howcanhelp
* inform{"price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 468* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 469* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "people": "four", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 470* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "paris", "price": "moderate"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 471* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "people": "eight", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 472* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "four", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 473* greet
 - utter_ask_howcanhelp
* inform{"location": "rome", "people": "six", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 474* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 475* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 476* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 477* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "madrid", "price": "expensive"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 478* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 479* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "eight"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 480* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "rome"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 481* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 482* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "paris"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 483* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 484* greet
 - utter_ask_howcanhelp
* inform{"location": "london"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 485* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 486* greet
 - utter_ask_howcanhelp
* inform{"people": "eight", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 487* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 488* greet
 - utter_ask_howcanhelp
* inform{"people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 489* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 490* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 491* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "people": "two"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 492* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "madrid", "people": "eight"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 493* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 494* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "rome", "people": "four"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 495* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "london", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 496* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 497* greet
 - utter_ask_howcanhelp
* inform{"location": "london", "people": "six", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 498* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "people": "four", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 499* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "eight", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 500* greet
 - utter_ask_howcanhelp
* inform{"people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 501* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "london"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 502* greet
 - utter_ask_howcanhelp
* inform{"location": "rome", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 503* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 504* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "madrid", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 505* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "london"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 506* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "london"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 507* greet
 - utter_ask_howcanhelp
* inform{"location": "london", "people": "four", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 508* greet
 - utter_ask_howcanhelp
* inform{"people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 509* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 510* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 511* greet
 - utter_ask_howcanhelp
* inform{"location": "rome", "people": "eight", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 512* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "people": "eight", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 513* greet
 - utter_ask_howcanhelp
* inform{"people": "four", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 514* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "rome", "people": "two"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 515* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 516* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "paris", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 517* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "people": "eight", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 518* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "london", "price": "expensive"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 519* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 520* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 521* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "people": "eight", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 522* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "paris", "price": "moderate"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 523* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 524* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "two", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 525* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "six"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 526* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 527* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "london", "price": "expensive"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 528* greet
 - utter_ask_howcanhelp
* inform{"people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 529* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "madrid", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 530* greet
 - utter_ask_howcanhelp
* inform{"people": "four", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 531* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 532* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "paris"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 533* greet
 - utter_ask_howcanhelp
* inform{"people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 534* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 535* greet
 - utter_ask_howcanhelp
* inform{"location": "london", "people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 536* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "people": "eight", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 537* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 538* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "paris", "people": "eight"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 539* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "people": "six", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 540* greet
 - utter_ask_howcanhelp
* inform{"people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 541* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 542* greet
 - utter_ask_howcanhelp
* inform{"people": "four", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 543* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 544* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "paris"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 545* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "people": "four"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 546* greet
 - utter_ask_howcanhelp
* inform{"people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 547* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "london", "people": "two"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 548* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 549* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "two"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 550* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 551* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 552* greet
 - utter_ask_howcanhelp
* inform{"people": "four", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 553* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 554* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "six", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 555* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "paris", "people": "four"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 556* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 557* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 558* greet
 - utter_ask_howcanhelp
* inform{"people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 559* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "people": "eight", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 560* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 561* greet
 - utter_ask_howcanhelp
* inform{"location": "london", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 562* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "paris", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 563* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "madrid", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 564* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 565* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "madrid", "people": "six"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 566* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 567* greet
 - utter_ask_howcanhelp
* inform{"people": "four", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 568* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "six", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 569* greet
 - utter_ask_howcanhelp
* inform{"location": "paris"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 570* greet
 - utter_ask_howcanhelp
* inform{"location": "london"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 571* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "rome"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 572* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "people": "four"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 573* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "two", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 574* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 575* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "rome", "people": "eight"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 576* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 577* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 578* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "people": "eight", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 579* greet
 - utter_ask_howcanhelp
* inform{"location": "london", "people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 580* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "london", "people": "six"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 581* greet
 - utter_ask_howcanhelp
* inform{"people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 582* greet
 - utter_ask_howcanhelp
* inform{"people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 583* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "london"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 584* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "rome", "people": "four"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 585* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 586* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "four", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 587* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 588* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 589* greet
 - utter_ask_howcanhelp
* inform{"people": "eight", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 590* greet
 - utter_ask_howcanhelp
* inform{"people": "six", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 591* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 592* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "paris", "people": "two"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 593* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 594* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "location": "bombay", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 595* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 596* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 597* greet
 - utter_ask_howcanhelp
* inform{"location": "london", "people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 598* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "madrid"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 599* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "bombay", "people": "two"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 600* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "eight", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 601* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "two", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 602* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "london"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 603* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "madrid"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 604* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "people": "two", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 605* greet
 - utter_ask_howcanhelp
* inform{"location": "paris"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 606* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 607* greet
 - utter_ask_howcanhelp
* inform{"people": "four", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 608* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 609* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "two"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 610* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "four"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 611* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 612* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "six", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 613* greet
 - utter_ask_howcanhelp
* inform{"price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 614* greet
 - utter_ask_howcanhelp
* inform{"people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 615* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "two", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 616* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 617* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "six", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 618* greet
 - utter_ask_howcanhelp
* inform{"price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 619* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "bombay"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 620* greet
 - utter_ask_howcanhelp
* inform{"people": "two", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 621* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 622* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "london"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 623* greet
 - utter_ask_howcanhelp
* inform{"location": "london", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 624* greet
 - utter_ask_howcanhelp
* inform{"location": "rome", "people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 625* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 626* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "people": "four", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 627* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "rome", "people": "two"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 628* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "people": "two"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 629* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 630* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "six", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 631* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "six", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 632* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "people": "six", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 633* greet
 - utter_ask_howcanhelp
* inform{"location": "london"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 634* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "london", "people": "two"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 635* greet
 - utter_ask_howcanhelp
* inform{"location": "london", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 636* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 637* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 638* greet
 - utter_ask_howcanhelp
* inform{"location": "rome", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 639* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "people": "six"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 640* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 641* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "bombay"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 642* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "six", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 643* greet
 - utter_ask_howcanhelp
* inform{"location": "london"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 644* greet
 - utter_ask_howcanhelp
* inform{"people": "four", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 645* greet
 - utter_ask_howcanhelp
* inform{"location": "london", "people": "six", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 646* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "madrid"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 647* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 648* greet
 - utter_ask_howcanhelp
* inform{"location": "paris", "people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 649* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 650* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 651* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "people": "eight", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 652* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "people": "two", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 653* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 654* greet
 - utter_ask_howcanhelp
* inform{"location": "london", "people": "six", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 655* greet
 - utter_ask_howcanhelp
* inform{"location": "paris"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 656* greet
 - utter_ask_howcanhelp
* inform{"people": "four", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 657* greet
 - utter_ask_howcanhelp
* inform{"price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 658* greet
 - utter_ask_howcanhelp
* inform{"location": "london", "people": "six", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 659* greet
 - utter_ask_howcanhelp
* inform{"people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 660* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "bombay", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "indian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 661* greet
 - utter_ask_howcanhelp
* inform{"location": "rome", "people": "six", "price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 662* greet
 - utter_ask_howcanhelp
* inform{"location": "paris"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 663* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 664* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "people": "eight"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 665* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "rome"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 666* greet
 - utter_ask_howcanhelp
* inform{"people": "eight"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 667* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "rome", "people": "two"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 668* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 669* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "indian", "location": "london"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 670* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 671* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 672* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "people": "six", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 673* greet
 - utter_ask_howcanhelp
* inform{"people": "two", "price": "moderate"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou

## 674* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid", "people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "british"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 675* greet
 - utter_ask_howcanhelp
* inform{"location": "madrid"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 676* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 677* greet
 - utter_ask_howcanhelp
* inform{"location": "rome", "people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 678* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 679* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "british", "location": "paris"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "six"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 680* greet
 - utter_ask_howcanhelp
* inform{"people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 681* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "people": "four"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 682* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "location": "bombay", "people": "four"}
 - utter_on_it
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 683* greet
 - utter_ask_howcanhelp
* inform{"location": "rome"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 684* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 685* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 686* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "rome"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_price
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 687* greet
 - utter_ask_howcanhelp
* inform{"price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_location
* inform{"location": "london"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 688* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian", "people": "four", "price": "cheap"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "madrid"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 689* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "people": "two"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "italian"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 690* greet
 - utter_ask_howcanhelp
* inform{"location": "rome", "people": "two", "price": "expensive"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "spanish"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 691* greet
 - utter_ask_howcanhelp
* inform{"location": "bombay", "people": "six"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "italian"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 692* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "paris", "price": "moderate"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 693* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "eight", "price": "moderate"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_moreupdates
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 694* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "french", "people": "eight"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"price": "expensive"}
 - utter_ask_moreupdates
* inform{"people": "six"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 695* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "italian"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "paris"}
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_price
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"location": "rome"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 696* greet
 - utter_ask_howcanhelp
* inform{"people": "four"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "french"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_price
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 697* greet
 - utter_ask_howcanhelp
* inform{"price": "cheap"}
 - utter_on_it
 - utter_ask_cuisine
* inform{"cuisine": "indian"}
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_numpeople
* inform{"people": "two"}
 - utter_ask_moreupdates
* inform{"location": "london"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 698* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "people": "six", "price": "expensive"}
 - utter_on_it
 - utter_ask_location
* inform{"location": "bombay"}
 - utter_ask_moreupdates
* inform{"price": "cheap"}
 - utter_ask_moreupdates
* inform{"cuisine": "french"}
 - utter_ask_moreupdates
* inform{"people": "two"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

## 699* greet
 - utter_ask_howcanhelp
* inform{"cuisine": "spanish", "location": "paris", "price": "cheap"}
 - utter_on_it
 - utter_ask_numpeople
* inform{"people": "eight"}
 - utter_ask_moreupdates
* inform{"price": "moderate"}
 - utter_ask_moreupdates
* inform{"cuisine": "british"}
 - utter_ask_moreupdates
* inform{"people": "four"}
 - utter_ask_moreupdates
* deny
 - utter_ack_dosearch
 - action_search_restaurants
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* deny
 - utter_ack_findalternatives
 - action_suggest
* affirm
 - utter_ack_makereservation
* thankyou
 - utter_goodbye

