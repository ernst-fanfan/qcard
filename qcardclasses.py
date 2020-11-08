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
        return "{}, {}, {}".format(self.name, self.subject, self.cards)
    
class Library():
    def __init__(self, owner):
        self.owner = owner
        self.collection = {}

    def get_owner(self):
        return self.owner

    def add_set(self, new_set):
        key = new_set.get_name()
        self.collection[key] = new_set

    def remove_set(self, set_to_remove):
        key = set_to_remove.get_name()
        self.collection.pop(key)

    def __repr__(self):
        return "{}, {}\n".format(self.owner, self.collection)

    
class Quiz():
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
