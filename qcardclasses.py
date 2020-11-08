###################################################################################
#back end classes for qcared to work###############################################
#Python 3.9########################################################################
###################################################################################

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
        
    def __repr__(self):#may need mod for jason DB
        message = "{}, {}".format(self.question, self.answer)
        return message
    
class Set_of_Cards():
    def __init__(self, name=None, subject=None, cards=None):
        self.name = name
        self.subject = subject
        if cards == None:
            self.cards = {}
        
    def set_name(self, name):
        self.name = name
        
    def set_subject(self, subject):
        self.subject
        
    def set_cards(self, cards):
        self.cards = cards 
        
    def get_name(self):
        return self.name
        
    def get_subject(self):
        return self.subject
        
    def get_cards(self):
        return self.cards
        
    #add card to set
    def add_card(self, card):
        key = card.get_question()
        self.cards[key] = card
        
    #remove carsd to set
    def remove_card(self, card):
        key = card.question
        self.cards.pop(key)
        
    def merge_sets(self, new_set, name=None, subject=None):
        if not name == None:
            self.set_name(name)
        if not subject == None:
            self.set_subject(subject)
        self.cards = self.cards | new_set.get_cards()
        
    def __repr__(self):
        msg = "{}, {}, {}".format(self.name, self.subject, self.cards)
        return msg
    
class Library():
    def __init__(self, owner):
        self.owner = owner
        self.collection = {}

    def add_set(self, new_set):
        key = new_set.get_name()
        self.collection[key] = new_set

    def remove_set(self, set_to_remove):
        key = set_to_remove.get_name()
        self.collection.pop(key)
    
class Quiz():
    pass
    
class test(Quiz):
    pass
    
#test
card1 = Card("1+1", "2")
card2 = Card("1+2", "3")
print (card1)
print(card2)
set1 = Set_of_Cards("One table", "Adding")
set1.add_card(card1)
set1.add_card(card2)
print(set1)
set1.remove_card(card1)
print(set1)