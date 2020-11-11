###################################################################################
#back end classes for qcared to work###############################################
#Python 3.9########################################################################
###################################################################################

import random as rn

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
    
class Deck():
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

    def prep_for_json(self):
        j_deck = {'name': self.name, 'subject': self.subject, 'card': self.cards}
        return j_deck

    def load_cards(self, j_deck):
        for j_card in j_deck:
            l_card = Card(question=json_card['question'], answer=json_card['answer'])
            self.add_card(l_card)

    def __repr__(self):
        return self.prep_for_json()

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

    def remove_deck(self, deck):
        decks = self.get_decks()
        decks.remove(deck)

    def merge_libraries(self, new_library):
        new_decks = new_library.get_decks()
        self.decks += new_decks
        self.set_size(len(self.decks))

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
    
