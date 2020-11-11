#test
card1 = Card(question="1+1", answer="2")
card2 = Card(question="1+2", answer="3")
card3 = Card(question="1+3", answer="4")
card4 = Card(question="1+4", answer="5")
# card5 = Card("1st President", "George Washignton")
# card6 = Card("46th President", "Joe Biden")
# card7 = Card("44th President", "Barrak Obama")
# card8 = Card("43rd President", "George W Bush jr")

set1 = Deck(name="One table", subject="Adding")
# set2 = Deck("Presidents", "History")

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




lib1 = decks("mee")
lib1.add_set(set1)
# lib1.add_set(set2)

print(lib1)
print()

# lib1.push_to_file()
# print(lib1)

# lib1 = decks("mee")
# lib1.pull_from_file()
# print(lib1)
# print()
# # print(lib1.get_decks())
selected_set = lib1.get_set(1)
quiz1 = Quiz(selected_set, 3)
print(quiz1)
