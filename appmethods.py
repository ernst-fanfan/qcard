import json
import qcardclasses

#to help json encoder process my classes
class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Library):
            return obj.prep_for_json()
        elif isinstance(obj, Deck):
            return obj.prep_for_json()
        elif isinstance(obj, Card):
            return obj.prep_for_json()
        else:
            return json.JSONEncoder.default(self, obj)
#File management
def save_library(library):
    with open("decks.json", "w") as jfile:
        json.dump(library, jfile, cls=MyEncoder)

def open_library():
    with open("decks.json") as jfile:
        j_library = json.load(jfile)
        l_library = Library(owner=j_library['owner'], size=j_library['size']) 
        l_library.load_decks(j_library['decks']) 
    return l_library