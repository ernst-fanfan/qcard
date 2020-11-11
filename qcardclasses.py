###################################################################################
#back end classes for qcared to work###############################################
#Python 3.9########################################################################
###################################################################################

import json
import random as rn

#to help json encoder process my classes
class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Library):
            return obj.library
        elif isinstance(obj, Set_of_Cards):
            return obj.prep_for_json()
        elif isinstance(obj, Card):
            return obj.prep_for_json()
        else:
            return json.JSONEncoder.default(self, obj)

#card manager
class Card():
    def __init__(self, question=None, answer=None):
        self.question = question
        self.answer = answer
        
    def get_question(self):
        return self.question
        
    def get_answer(self):
        return self.answer

    def set_question(self, question):
        self.question = question
        
    def set_answer(self, answer):
        self.answer = answer

    def prep_for_json(self):
        card = {'question': self.question, 'answer': self.answer}
        return card

    def load_card(self, json_card):
        self.__init__(question=json_card['question'], answer=json_card['answer'])

    def __repr__(self):#may need mod for jason DB
        return self.prep_for_json()
    
class Set_of_Cards():
    def __init__(self, name=None, subject=None, size=0, cards=None):
        self.name = name
        self.subject = subject
        self.size = size
        if cards == None:
            self.cards = []
        else:
            self.cards = cards
        
    def set_name(self, name):
        self.name  = name
        
    def set_subject(self, subject):
        self.subject = subject

    def set_size(self, num):
        self.size = num
        
    def set_cards(self, cards):
        self.cards = cards 
        
    def get_name(self):
        return self.name
        
    def get_subject(self):
        return self.subject
        
    def get_cards(self):
        return self.cards

    def get_size(self):
        return self.size
        
    #add card to set
    def add_card(self, card):
        index = self.get_size() + 1
        self.cards.append(card)
        self.set_size(index)
        
    #remove card from set
    def remove_card(self, card):
        self.cards.remove(card)

    def find_card(self, question=None, answer=None):
        if not question == None:
            for card in self.get_cards():
                if question == card.get_question():
                    return card
        elif not answer ==None:
            for card in self.get_cards():
                if answer == card.get_answer():
                    return card
        
    def merge_sets(self, new_set, name=None, subject=None):
        if not name == None:
            self.set_name(name)
        if not subject == None:
            self.set_subject(subject)

        index = self.get_size()
        new_cards = new_set.get_cards()
        
        cards = self.get_cards()
        cards = cards + new_cards
        self.set_size(len(cards))
        
    # def get_card_index(self, index):
    #     cards = self.get_cards()
    #     return cards[index]

    def __repr__(self):
        return "Set: {}, Subject: {}, Cards: {}".format(self.name, self.subject, self.cards)

class Library():
    def __init__(self, owner, size=0, library=None):
        if library == None:
            self.library = {'owner' : owner, 'size' : size,'library' : {}}
        else:
            self.library = {'owner' : owner, 'size' : size,'library' : library}

    def get_set(self, index):
        library = self.get_library()
        return library[index]

    def get_owner(self):
        return self.library['owner']

    def get_library(self):
        return self.library['library']

    def get_size(self):
        return self.library['size']

    def set_owner(self, owner):
        self.library['owner']  = owner

    def set_library(self, library):
        self.library['library'] = library

    def set_size(self, size):
        self.library['size'] = size

    def add_set(self, new_set):
        index = self.get_size() + 1
        library = self.get_library()
        new_set.set_index(index)
        library[index] = new_set
        self.set_size(index)

    def remove_set(self, index):
        library = self.get_library()
        library.pop(index)

    def merge_library(self, new_library):
        index = self.get_size()
        new_collection = new_library.get_library()
        for set_of_card in new_collection:
            index += 1
            set_of_card.set_index(index)

        library = self.get_library()
        library = library | new_collection
        self.set_size(index)

    def __repr__(self):
        return str(self.library)

    #File management
    def push_to_file(self):
        library = self
        with open("library.json", "w") as jfile:
            json.dump(library, jfile, cls=MyEncoder)
        self.library = None

    def pull_from_file(self):
        with open("Library.json") as jfile:
            data = json.load(jfile)
            self.set_size(data['size'])
            for key in data['library']:
                #rebuild set
                set_ = data['library'][key]
                extr_set = Set_of_Cards(index=set_['index'], name=set_['name'], subject=set_['subject'], size=set_['size'])
                
                for key2 in set_['cards']:
                    #rebuild card
                    card = set_['cards'][key2] 
                    extr_card = Card(index=card['index'], question=card['question'], answer=card['answer'])
                    extr_set.structure['cards'][key2] = extr_card

                self.library['library'][key] = extr_set
                
    
class Quiz():
    def __init__(self, set_, num = 10):
        self.set_ = set_
        self.kuiz = {}
        self.load_quiz(num)

    def load_quiz(self, num):
        ap = []
        size = self.set_.get_size()
        for i in range(num):
            c = rn.randint(1, size) 
            while c in ap:
                c = rn.randint(1, size)
            self.kuiz[i+1] = self.set_.get_card_index(c)
            ap.append(c)

    def __repr__(self):
        return str(self.kuiz)
    
class test(Quiz):
    pass
    
#test
card1 = Card(question="1+1", answer="2")
card2 = Card(question="1+2", answer="3")
card3 = Card(question="1+3", answer="4")
card4 = Card(question="1+4", answer="5")
# card5 = Card("1st President", "George Washignton")
# card6 = Card("46th President", "Joe Biden")
# card7 = Card("44th President", "Barrak Obama")
# card8 = Card("43rd President", "George W Bush jr")

set1 = Set_of_Cards(name="One table", subject="Adding")
# set2 = Set_of_Cards("Presidents", "History")

# print(set1)
# print()
# print(set2)
# print()

set1.add_card(card1)
set1.add_card(card2)
set1.add_card(card3)
set1.add_card(card4)
# set2.add_card(card5)
# set2.add_card(card6)
# set2.add_card(card7)
# set2.add_card(card8)

# print(set1)
# print()
# print(set2)
# print()




lib1 = Library("mee")
lib1.add_set(set1)
# lib1.add_set(set2)

print(lib1)
print()

# lib1.push_to_file()
# print(lib1)

# lib1 = Library("mee")
# lib1.pull_from_file()
# print(lib1)
# print()
# # print(lib1.get_library())
selected_set = lib1.get_set(1)
quiz1 = Quiz(selected_set, 3)
print(quiz1)
