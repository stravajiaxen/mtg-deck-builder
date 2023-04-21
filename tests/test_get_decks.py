import unittest

from builder.lists import *
import vcr
from operator import itemgetter
import time
test_card = top_commanders_2_years[0]

class MyTestCase(unittest.TestCase):

    def test_get_columns(self):
        print(my_cards.columns)
        print(set(my_cards["List name"]))

    # @vcr.use_cassette()
    def test_get_ideas(self):
        recs = {}
        used_set = my_cards
        for commander in set(top_commanders_2_years + top_commanders_today):
            recs[commander] = recommended_cards(used_set, commander)
        recs = {k: v for k, v in sorted(recs.items(), key=lambda x: x[1]["Price"], reverse=True)}
        for commander, info in recs.items():
            print(commander, "Price", info["Price"], "Number", info["Number"])

    def test_analyze(self):
        commander = "Najeela, the Blade-Blossom"
        #commander = "Ziatora, the Incinerator"
        used_set = my_cards #free_cards
        recs = recommended_cards(used_set, commander)
        cards = (used_set[used_set["Name"].isin(recs["Cards"])])
        cards = cards.drop_duplicates(subset=["Name"])
        for name, price in reversed(list(zip(cards["Name"], cards["Price"]))):
            print("1", name)


    def test_get_list(self):
        print(top_commanders_2_years)

    def test_get_cards(self):
        print(my_cards)

    def test_get_edhrec_url(self):
        print(get_edhrec_url(test_card))

    def test_get_edhrec_decklinks(self):
        print(get_edhrec_decklinks(test_card))

    def test_get_edhrec_decklist(self):
        decks = get_edhrec_decklinks(test_card)
        print(len(decks))
        deckname = decks[0]
        print(get_edhrec_decklist(deckname))

    def test_get_edhrec_commander_analysis(self):
        print(get_edhrec_commander_analysis(test_card))

if __name__ == '__main__':
    unittest.main()
