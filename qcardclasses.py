###################################################################################
#back end classes for qcared to work###############################################
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
    pass
    
class Library():
    pass
    
class Quiz():
    pass
    
class test(Quiz):
    pass