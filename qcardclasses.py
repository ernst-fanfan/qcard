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

    def __repr__(self):#may need mod for jason DB
        return str(self.prep_for_json())
    
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
        
    def merge_decks(self, new_set, name=None, subject=None):
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
        return str(self.prep_for_json())

class Library():
    def __init__(self, owner, size=0, decks=None):
        self.owner = owner
        self.size = size
        
        if decks == None:
            self.decks = []
        else:
            self.decks = decks

    # def get_decks(self, index):
    #     decks = self.get_decks()
    #     return decks[index]

    def get_owner(self):
        return self.owner

    def get_decks(self):
        return self.decks

    def get_size(self):
        return self.size

    def set_owner(self, owner):
        self.owner  = owner

    def set_decks(self, decks):
        self.decks = decks

    def set_size(self, size):
        self.size = size

    def add_deck(self, new_deck):
        decks = self.get_decks()
        decks.append(new_deck)
        self.set_size(len(decks))

    def remove_deck(self, deck):
        decks = self.get_decks()
        decks.remove(deck)

    def merge_libraries(self, new_library):
        new_decks = new_library.get_decks()
        self.decks += new_decks
        self.set_size(len(self.decks))

    def prep_for_json(self):
        j_library = {'owner': self.owner, 'size': self.size, 'decks': self.decks}
        return j_library

    def load_decks(self, j_library):
        for j_deck in j_library:
            l_deck = j_deck(name=j_library['name'], subject=j_library['subject'], size=j_library['size'])
            l_deck.load_cards(j_deck['cards'])
            self.add_deck(l_deck)

    def __repr__(self):
        return str(self.prep_for_json())
    
# class Quiz():
#     def __init__(self, set_, num = 10):
#         self.set_ = set_
#         self.kuiz = {}
#         self.load_quiz(num)

#     def load_quiz(self, num):
#         ap = []
#         size = self.set_.get_size()
#         for i in range(num):
#             c = rn.randint(1, size) 
#             while c in ap:
#                 c = rn.randint(1, size)
#             self.kuiz[i+1] = self.set_.get_card_index(c)
#             ap.append(c)

#     def __repr__(self):
#         return str(self.kuiz)
    
# class test(Quiz):
#     pass
    
