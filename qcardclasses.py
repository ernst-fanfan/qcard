###################################################################################
#back end classes for qcared to work###############################################
#Python 3.9########################################################################
###################################################################################

import json

#card manager
class Card():
    def __init__(self, question=None, answer=None):
        if not question == None:
            self.content ['question'] = question
            self.content ['answer'] = answer
            self.content ['index'] = None
        
    def get_question(self):
        return self.content['question']
        
    def get_answer(self):
        return self.content['answers']
        
    def get_index(self):
        return self.content['index']

    def set_question(self, question):
        self.content['questions'] = question
        
    def set_answer(self, answer):
        self.content['answer'] = answer

    def set_index(self, index):
        self.content['index'] = index
        
    def __repr__(self):#may need mod for jason DB
        return self.content
    
class Set_of_Cards():
    def __init__(self, name=None, subject=None, cards=None):
        self.structure['name'] = name
        self.structure['subject'] = subject
        self.structure['size'] = 0
        if cards == None:
            self.structure['cards'] = {}
        
    def set_name(self, name):
        self.structure['name'] = name
        
    def set_subject(self, subject):
        self.structure['subject'] = subject

    def set_size(self, num):
        self.structure['size'] = num
        
    # Not sure if I will need this
    # def set_cards(self, cards):
    #     self.cards = cards 
        
    def get_name(self):
        return self.structure['name']
        
    def get_subject(self):
        return self.structure['subject']
        
    def get_cards(self):
        return self.structure.['cards']

    def get_size(self):
        return self.structure['size']
        
    #add card to set
    def add_card(self, card):
        index = self.get_size() + 1
        card.set_index(index)
        self.structure['cards'] [index]= card
        self.set_size(index)
        
    #remove card from set
    def remove_card(self, card):
        key = card.get_index()
        self.cards.pop(key)

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
        for card in new_set:
            index += 1
            card.set_index(index)

        self.cards = self.cards | new_set.get_cards()
        self.set_size(index)
        
    def __repr__(self):
        return self.structure

class Library():
    def __init__(self, owner):
        self.owner = owner
        self.collection = {}

    def get_owner(self):
        return self.owner

    def add_set(self, new_set):
        key = new_set.get_name()
        value = {"subject" : new_set.get_subject(), "cards" : new_set.get_cards()}
        self.collection[key] = value

    def remove_set(self, set_to_remove):
        key = set_to_remove.get_name()
        self.collection.pop(key)

    def __repr__(self):
        return "{}, {}\n".format(self.owner, self.collection)

    #File management
    def push_to_file(self):
        to_dump = {self.owner : self.collection}
        with open("library.json", "w") as jfile:
            json.dump(to_dump, jfile)
        self.collection = None

    def pull_from_file(self):
        with open("Library.json") as jfile:
            data = json.load(jfile)
        self.collection = data[self.owner]
    
class Quiz():
    def __init__(self, new_set):
        self.new_set 
        self.kuiz = {}

    def load_quiz(self, num = 10):
        #loop num times and 
        #random select
        #load random
        pass
    
class test(Quiz):
    pass
    
#test
card1 = Card("1+1", "2")
card2 = Card("1+2", "3")
card3 = Card("1+3", "4")
card4 = Card("1+4", "5")

set1 = Set_of_Cards("One table", "Adding")
set1.add_card(card1)
set1.add_card(card2)
set1.add_card(card3)
set1.add_card(card4)

#set1.remove_card(card1)
card5 = Card("1st President", "George Washignton")
card6 = Card("46th President", "Joe Biden")
card7 = Card("44th President", "Barrak Obama")
card8 = Card("43rd President", "George W Bush jr")

set2 = Set_of_Cards("Presidents", "History")
set2.add_card(card5)
set2.add_card(card6)
set2.add_card(card7)
set2.add_card(card8)

lib1 = Library("mee")
lib1.add_set(set1)
lib1.add_set(set2)

print(lib1)

lib1.push_to_file()
print(lib1)

lib1.pull_from_file()
print(lib1)

