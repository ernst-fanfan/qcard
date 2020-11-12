from qcardclasses import Card, Deck, Library
import appmethods as app
#test
card1 = Card(question="1+1", answer="2")
card2 = Card(question="1+2", answer="3")
card3 = Card(question="1+3", answer="4")
card4 = Card(question="1+4", answer="5")
card5 = Card("1st President", "George Washignton")
card6 = Card("46th President", "Joe Biden")
card7 = Card("44th President", "Barrak Obama")
card8 = Card("43rd President", "George W Bush jr")

deck1 = Deck(name="One table", subject="Adding")
deck2 = Deck("Presidents", "History")

deck1.add_card(card1)
deck1.add_card(card2)
deck1.add_card(card3)
deck1.add_card(card4)
deck2.add_card(card5)
deck2.add_card(card6)
deck2.add_card(card7)
deck2.add_card(card8)

lib1 = Library("mee")
lib1.add_deck(deck1)
lib1.add_deck(deck2)

# print(card1)
# print()
# print(deck1)
# print()
# print(deck2)
# print()
# print(lib1)
# print()

app.save_library(lib1)
lib2 = app.open_library("library.json")
# print(lib2)

lib2.merge_libraries(lib1)
# print(lib2)

deck1.merge_decks(deck2, 'Adding and Presidents', 'Math and History')
print(deck1)
