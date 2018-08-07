import json
import difflib
from difflib import SequenceMatcher # Return ration
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower() #Converting to lower cases to avoid error.
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0: #A list object
        yn = input("Did you mean %s instead? enter Y if yes, or N if no." % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist."
        else:
            return "We didn't understand your query."

    else:
        return "This word doesn't exist. Please, check it again." #Output when there is no such a word in dictionary, to avoid error.

word = input("Enter word: ")

#Optimalization to more user friendly output we delete print(translate(word)) and put instead:
output = translate(word)
#Implementing a condition
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
